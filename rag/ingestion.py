import os
import glob
import re
from pathlib import Path
from typing import List, Dict, Any
import pymupdf4llm
from langchain_core.documents import Document


def extract_policy_metadata(filename: str, first_page_text: str) -> Dict[str, Any]:
    """
    Extracts policy-level metadata such as reference ID, policy title,
    and category directly from the file name and document header.
    """
    clean_name = Path(filename).stem.replace("TechV-Flash_", "").replace("_", " ")

    # Regex extraction for document reference IDs (e.g., HR-POL-002, IT-SEC-001)
    doc_ref_match = re.search(r"\b([A-Z]{2,4}-[A-Z]{2,4}-\d{3})\b", first_page_text)
    doc_ref = doc_ref_match.group(1) if doc_ref_match else "UNKNOWN-REF"

    # Category derivation
    category = "General"
    lower_name = clean_name.lower()
    if any(k in lower_name for k in ["leave", "hr", "benefits", "attendance", "recruitment", "exit"]):
        category = "Human Resources"
    elif any(k in lower_name for k in ["security", "privacy", "data", "it"]):
        category = "IT & Security"
    elif any(k in lower_name for k in ["conduct", "harassment", "disciplinary"]):
        category = "Legal & Compliance"
    elif any(k in lower_name for k in ["travel", "payroll", "expense", "compensation"]):
        category = "Finance & Operations"

    return {
        "policy_name": clean_name,
        "doc_ref": doc_ref,
        "category": category,
    }


def load_pdf_with_layout(corpus_dir: str = "corpus") -> List[Document]:
    """
    Loads all policy PDFs in corpus_dir, converts pages into Markdown to
    preserve tables and structural headings, and builds 1-based indexed Documents
    enriched with policy metadata and context prefixes.
    """
    documents: List[Document] = []
    pdf_paths = glob.glob(os.path.join(corpus_dir, "**/*.pdf"), recursive=True)

    if not pdf_paths:
        print(f"[!] Warning: No PDF files found in '{corpus_dir}'.")
        return documents

    print(f"Found {len(pdf_paths)} PDF(s) in '{corpus_dir}'. Extracting layout & tables...")

    for i, pdf_path in enumerate(sorted(pdf_paths), 1):
        filename = os.path.basename(pdf_path)
        normalized_source = Path(pdf_path).as_posix()
        print(f"[{i:02d}/{len(pdf_paths):02d}] Processing: {filename} ...", end=" ", flush=True)

        try:
            pages_data = pymupdf4llm.to_markdown(
                pdf_path,
                page_chunks=True,
                show_progress=False
            )

            if not pages_data:
                print("Skipped (Empty)")
                continue

            first_page_sample = pages_data[0].get("text", "")
            base_meta = extract_policy_metadata(filename, first_page_sample)
            total_pages = len(pages_data)

            for p in pages_data:
                # pymupdf4llm returns 0-based page index; convert to human-readable 1-based index
                page_zero_idx = p.get("metadata", {}).get("page", 0)
                page_number = page_zero_idx + 1
                raw_text = p.get("text", "").strip()

                if not raw_text:
                    continue

                # Context prefix ensures dense vector embeddings and BM25 retain identity
                prefixed_content = (
                    f"[Document: {base_meta['policy_name']} | Ref: {base_meta['doc_ref']} | Page: {page_number}]\n\n"
                    f"{raw_text}"
                )

                doc = Document(
                    page_content=prefixed_content,
                    metadata={
                        "source": normalized_source,
                        "filename": filename,
                        "policy_name": base_meta["policy_name"],
                        "doc_ref": base_meta["doc_ref"],
                        "category": base_meta["category"],
                        "page": page_number,
                        "total_pages": total_pages,
                    },
                )
                documents.append(doc)

            print(f"Done ({total_pages} pages)")

        except Exception as e:
            print(f"Failed! Error: {e}")

    print(f"Extraction complete. Successfully loaded {len(documents)} page documents.")
    return documents