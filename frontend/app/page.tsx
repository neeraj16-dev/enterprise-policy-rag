import fs from 'fs';
import path from 'path';
import ChatClient from './ChatClient';

export default function Page() {
  const corpusDir = 'f:/enterprise_rag/corpus';
  let pdfs: string[] = [];
  
  try {
    if (fs.existsSync(corpusDir)) {
      pdfs = fs.readdirSync(corpusDir).filter(f => f.toLowerCase().endsWith('.pdf'));
    }
  } catch(e) {
    console.error('Failed to read corpus directory:', e);
  }
  
  return <ChatClient pdfs={pdfs} />;
}
