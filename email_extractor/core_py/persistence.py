from __future__ import annotations
import csv, json, sqlite3
from pathlib import Path
from .extractor import EmailResult

SCHEMA = '''CREATE TABLE IF NOT EXISTS emails (
 id INTEGER PRIMARY KEY, email TEXT NOT NULL, page_title TEXT, website TEXT,
 source_url TEXT NOT NULL, valid_mx INTEGER, status TEXT, UNIQUE(email, source_url));'''

def init_db(path: str | Path) -> sqlite3.Connection:
    db = sqlite3.connect(path)
    db.execute(SCHEMA)
    db.commit()
    return db

def save_results(db: sqlite3.Connection, results: list[EmailResult]) -> None:
    db.executemany("INSERT OR IGNORE INTO emails(email,page_title,website,source_url,valid_mx,status) VALUES(?,?,?,?,?,?)",
                   [(r.email,r.page_title,r.website,r.source_url,None if r.valid_mx is None else int(r.valid_mx),r.status) for r in results])
    db.commit()

def export_csv(results: list[EmailResult], path: str | Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["email","page_title","website","source_url","valid_mx","status"])
        w.writeheader()
        for r in results: w.writerow(r.__dict__)

def export_json(results: list[EmailResult], path: str | Path) -> None:
    Path(path).write_text(json.dumps([r.__dict__ for r in results], ensure_ascii=False, indent=2), encoding="utf-8")
