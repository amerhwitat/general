const axios = require('axios');
const EMAIL_RE = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/g;
async function crawl(urls, progressCallback = () => {}, concurrency = 8) {
  const contacts = new Set(); let completed = 0; let index = 0;
  async function worker() { while (true) { const i = index++; if (i >= urls.length) return; const url = urls[i]; try { const u = new URL(url); if (!['http:','https:'].includes(u.protocol)) continue; const res = await axios.get(url,{timeout:10000,headers:{'User-Agent':'ChimeraEmailExtractor/1.0'},maxContentLength:5_000_000}); for (const e of (String(res.data).match(EMAIL_RE)||[])) contacts.add(e.toLowerCase()); } catch {} finally { completed++; progressCallback(completed, contacts.size); } } }
  await Promise.all(Array.from({length: Math.min(concurrency, Math.max(1,urls.length))}, worker)); return [...contacts];
}
module.exports = { crawl };
