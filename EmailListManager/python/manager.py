"""Local-first email list manager: lists, tags, consent/status, dedupe, import/export and AI-assisted segmentation."""
from __future__ import annotations
import csv, re, sqlite3
from pathlib import Path
from shared_ai import RNNLLM

EMAIL_RE=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
class EmailListManager:
    def __init__(self, db="email_lists.sqlite3", ai=None):
        self.db=Path(db); self.ai=ai or RNNLLM()
        with sqlite3.connect(self.db) as c:
            c.executescript('''CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY,email TEXT UNIQUE NOT NULL,name TEXT DEFAULT '',status TEXT DEFAULT 'active',consent TEXT DEFAULT 'unknown',source TEXT DEFAULT '',tags TEXT DEFAULT '',notes TEXT DEFAULT '');CREATE TABLE IF NOT EXISTS lists(id INTEGER PRIMARY KEY,name TEXT UNIQUE NOT NULL,description TEXT DEFAULT '');CREATE TABLE IF NOT EXISTS memberships(contact_id INTEGER,list_id INTEGER,UNIQUE(contact_id,list_id));''')
    def add(self,email,name='',list_name=None,consent='unknown',source='',tags=''):
        e=email.strip().lower()
        if not EMAIL_RE.match(e): return False
        with sqlite3.connect(self.db) as c:
            c.execute('INSERT OR IGNORE INTO contacts(email,name,consent,source,tags) VALUES(?,?,?,?,?)',(e,name,consent,source,tags))
            if list_name:
                c.execute('INSERT OR IGNORE INTO lists(name) VALUES(?)',(list_name,)); cid=c.execute('SELECT id FROM contacts WHERE email=?',(e,)).fetchone()[0]; lid=c.execute('SELECT id FROM lists WHERE name=?',(list_name,)).fetchone()[0]; c.execute('INSERT OR IGNORE INTO memberships VALUES(?,?)',(cid,lid))
        return True
    def import_csv(self,path,list_name=None):
        n=0
        with open(path,encoding='utf-8-sig',newline='') as f:
            for row in csv.DictReader(f): n += int(self.add(row.get('email',''),row.get('name',''),list_name,row.get('consent','unknown'),row.get('source',''),row.get('tags','')))
        return n
    def export_csv(self,path,status='active'):
        with sqlite3.connect(self.db) as c, open(path,'w',newline='',encoding='utf-8') as f:
            w=csv.writer(f); w.writerow(['email','name','status','consent','source','tags','notes']); w.writerows(c.execute('SELECT email,name,status,consent,source,tags,notes FROM contacts WHERE status=?',(status,)))
    def ai_segment(self,limit=100):
        with sqlite3.connect(self.db) as c: rows=c.execute('SELECT email,tags,notes FROM contacts WHERE status="active" LIMIT ?',(limit,)).fetchall()
        return [{"email":e,**self.ai.classify_contact(e,t+' '+n)} for e,t,n in rows]
