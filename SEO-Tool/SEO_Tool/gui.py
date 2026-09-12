from __future__ import annotations
import threading
from pathlib import Path
from flask import Flask, jsonify, render_template_string, request
from .core import CrawlConfig, SeoCrawler

app=Flask(__name__)
HTML='''<!doctype html><html><head><meta charset="utf-8"><title>SEO-Tool</title><style>body{font-family:system-ui;margin:0;background:#111827;color:#e5e7eb}main{max-width:1200px;margin:auto;padding:28px}input,button{padding:12px;border-radius:8px;border:1px solid #374151;background:#1f2937;color:#fff}input{width:42%}button{cursor:pointer}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.card{background:#1f2937;padding:18px;border-radius:12px}.log{white-space:pre-wrap;background:#030712;padding:16px;min-height:160px}table{width:100%;border-collapse:collapse}td,th{padding:8px;border-bottom:1px solid #374151;text-align:left}</style></head><body><main><h1>SEO-Tool</h1><p>Authorized technical SEO, web research and document extraction workspace.</p><p><input id="url" placeholder="https://example.org"><input id="out" placeholder="Output directory" value="./seo-results"><button onclick="start()">Start scan</button></p><div class="grid"><div class="card"><b>Pages</b><div id="pages">0</div></div><div class="card"><b>Issues</b><div id="issues">0</div></div><div class="card"><b>Links</b><div id="links">0</div></div><div class="card"><b>Status</b><div id="status">idle</div></div></div><h2>Progress</h2><div class="log" id="log">Ready.</div></main><script>async function start(){const url=document.getElementById('url').value,out=document.getElementById('out').value;document.getElementById('status').textContent='running';const r=await fetch('/api/scan',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({url,output:out})});const j=await r.json();document.getElementById('pages').textContent=j.pages;document.getElementById('issues').textContent=j.issues;document.getElementById('links').textContent=j.links;document.getElementById('status').textContent=j.status;document.getElementById('log').textContent=JSON.stringify(j,null,2)}</script></body></html>'''

@app.get('/')
def index(): return render_template_string(HTML)

@app.post('/api/scan')
def scan():
    data=request.get_json(force=True); url=data.get('url','').strip(); out=data.get('output','./seo-results')
    if not url: return jsonify(error='url required'),400
    c=CrawlConfig(seed=url,output=Path(out),allow_onion=False)
    try:
        pages,issues=SeoCrawler(c).crawl()
        return jsonify(status='complete',pages=len(pages),issues=len(issues),links=len(SeoCrawler(c).links) if False else len(__import__('json').loads((Path(out)/'report.json').read_text()).get('links',[])),output=str(Path(out).resolve()))
    except Exception as e: return jsonify(status='error',error=str(e)),400

def main(): app.run(host='127.0.0.1',port=5088,debug=False)
if __name__=='__main__': main()
