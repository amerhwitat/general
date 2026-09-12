export type Contact={email:string;source_url:string;domain:string;title?:string;keywords?:string[];method?:string;discovered_at?:string};
export type CrawlProgress={pages:number;queued:number;emails:number;errors:number;rate:number;status:'running'|'paused'|'done'|'cancelled'};
export function normalizeEmail(value:string):string|null{const e=value.trim().toLowerCase(); return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e)?e:null;}
export function extractEmails(html:string):string[]{const out=new Set<string>(); for(const m of html.matchAll(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi)){const e=normalizeEmail(m[0]);if(e)out.add(e)} return [...out];}
