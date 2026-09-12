export function normalizeEmail(value){const e=value.trim().toLowerCase();return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e)?e:null;}
export function extractEmails(html){const s=new Set();for(const m of html.matchAll(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi)){const e=normalizeEmail(m[0]);if(e)s.add(e)}return [...s];}
