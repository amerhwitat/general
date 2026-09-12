const axios=require('axios'); const dns=require('node:dns').promises;
const EMAIL_REGEX=/(?<![\w.+-])([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)(?![\w.-])/g;
async function fetchPage(url){try{const u=new URL(url);if(!['http:','https:'].includes(u.protocol))return {html:'',finalUrl:''};const res=await axios.get(url,{timeout:10000,maxContentLength:5000000,headers:{'User-Agent':'ChimeraEmailExtractor/1.0'}});return {html:String(res.data),finalUrl:res.request?.res?.responseUrl||url};}catch{return {html:'',finalUrl:''};}}
function extractEmails(html){return [...new Set([...html.matchAll(EMAIL_REGEX)].map(m=>m[1].replace(/^[.,;:<>\[\](){}\"]+|[.,;:<>\[\](){}\"]+$/g,'').toLowerCase()))];}
function extractPageTitle(html){const m=html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);return m?m[1].replace(/<[^>]+>/g,'').replace(/\s+/g,' ').trim():'';}
async function validateEmail(email){const p=email.split('@');if(p.length!==2)return false;try{return (await dns.resolveMx(p[1])).length>0;}catch{return false;}}
module.exports={fetchPage,extractEmails,extractPageTitle,validateEmail};
