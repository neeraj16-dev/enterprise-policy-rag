import os
import re
from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from pathlib import Path


def clean_header_text(header: str) -> str:
    """Removes extra markdown bold/italic tags and trims whitespace."""
    if not header:
        return "General"
    cleaned = re.sub(r"[*_`]", "", header)
    return cleaned.strip()


def fixed_size_chunks(documents: List[Document]) -> List[Document]:
    """
    Splits documents by character count while preserving full metadata integrity.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_documents(documents)
    page_chunk_counters = {}

    final_chunks = []
    for chunk in chunks:
        meta = chunk.metadata.copy()
        filename_stem = Path(meta.get("source", "doc")).stem
        page = meta.get("page", 1)

        page_key = (filename_stem, page)
        chunk_idx = page_chunk_counters.get(page_key, 0)
        page_chunk_counters[page_key] = chunk_idx + 1

        meta["chunk_id"] = f"{filename_stem}_p{page}_c{chunk_idx:02d}"
        meta["section"] = meta.get("section", "General")

        chunk.metadata = meta
        final_chunks.append(chunk)

    return final_chunks


def structured_chunks(documents: List[Document]) -> List[Document]:
    """
    Splits policy documents along Markdown header boundaries, prevents table splitting
    by using balanced token sizes (1000 chars), prepends section headers for dense
    retrieval contextualization, and retains all policy metadata.
    """
    headers_to_split_on = [
        ("#", "Header_1"),
        ("##", "Header_2"),
        ("###", "Header_3"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False
    )

    # 1000 chars keeps typical policy tables (4-8 rows) within a single chunk
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", " ", ""]
    )

    final_chunks: List[Document] = []
    page_chunk_counters = {}

    for doc in documents:
        base_meta = doc.metadata.copy()
        raw_source = base_meta.get("source", "doc")
        filename_stem = os.path.splitext(os.path.basename(raw_source))[0]
        page = base_meta.get("page", 1)

        # 1. Structural split based on Markdown headings
        header_splits = markdown_splitter.split_text(doc.page_content)

        for split in header_splits:
            raw_section = (
                split.metadata.get("Header_3")
                or split.metadata.get("Header_2")
                or split.metadata.get("Header_1")
                or "General"
            )
            section_title = clean_header_text(raw_section)

            # 2. Chunking within section
            sub_chunks = text_splitter.split_text(split.page_content)

            for text in sub_chunks:
                text_clean = text.strip()
                if not text_clean:
                    continue

                page_key = (filename_stem, page)
                chunk_idx = page_chunk_counters.get(page_key, 0)
                page_chunk_counters[page_key] = chunk_idx + 1

                chunk_id = f"{filename_stem}_p{page}_c{chunk_idx:02d}"

                # Clone original document metadata and enrich
                chunk_meta = base_meta.copy()
                chunk_meta["chunk_id"] = chunk_id
                chunk_meta["section"] = section_title

                final_chunks.append(
                    Document(
                        page_content=text_clean,
                        metadata=chunk_meta
                    )
                )

    return final_chunks