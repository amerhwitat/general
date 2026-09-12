from __future__ import annotations
from pathlib import Path
import json, re

class DocumentExtractor:
    TEXT_EXT={'.txt','.md','.markdown','.html','.htm','.json','.csv','.xml','.yaml','.yml','.rst','.log','.css','.js','.ts','.py','.c','.cpp','.h','.hpp','.java','.go','.rs','.php','.rb','.sh','.ps1','.sql'}
    def extract(self,path:Path)->str:
        ext=path.suffix.lower()
        if ext in self.TEXT_EXT: return path.read_text(encoding='utf-8',errors='replace')
        if ext=='.pdf':
            try:
                from pypdf import PdfReader
                return '\n'.join((p.extract_text() or '') for p in PdfReader(str(path)).pages)
            except ImportError: return '[PDF adapter requires: pip install pypdf]'
        if ext=='.docx':
            try:
                from docx import Document
                return '\n'.join(p.text for p in Document(str(path)).paragraphs)
            except ImportError: return '[DOCX adapter requires: pip install python-docx]'
        return ''
    def save_text(self,path:Path,text:str):
        path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text,encoding='utf-8')


def extract_download(path:Path,output:Path):
    text=DocumentExtractor().extract(path); target=output/(path.stem+'.txt'); DocumentExtractor().save_text(target,text); return target
