import { readFileSync, writeFileSync } from 'node:fs';
import { request } from 'node:https';
const EMAIL=/[A-Z0-9._%+-]+\s*(?:@|\[at\]|\(at\))\s*[A-Z0-9.-]+\s*(?:\.|\[dot\]|\(dot\))\s*[A-Z]{2,}/gi;
const normalize=(x:string)=>x.toLowerCase().replace(/\s+/g,'').replace(/\[at\]|\(at\)/g,'@').replace(/\[dot\]|\(dot\)/g,'.');
function get(url:string):Promise<string>{return new Promise((resolve,reject)=>request(url,{headers:{'user-agent':'EmailKeywordCrawler/1.0'}},r=>{let b='';r.on('data',c=>b+=c);r.on('end',()=>resolve(b));r.on('error',reject)}).on('error',reject).end())}
async function main(){const args=process.argv.slice(2), urls=args.filter(x=>x.startsWith('http')), ks=args.flatMap((x,i)=>x==='--keyword'&&args[i+1]?[args[i+1].toLowerCase()]:[]); const out=new Map<string,string>(); for(const u of urls){try{const t=await get(u); if(ks.some(k=>t.toLowerCase().includes(k))) for(const m of t.match(EMAIL)||[]) out.set(normalize(m),u); console.log(JSON.stringify({event:'page',url:u,emails:out.size}))}catch(e){console.error(JSON.stringify({event:'error',url:u,error:String(e)}))}} writeFileSync('emails.csv','email,source_url\n'+[...out].map(([e,u])=>`"${e}","${u}"`).join('\n')); writeFileSync('emails.txt',[...out.keys()].join('\n'));}
main();
