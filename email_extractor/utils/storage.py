"""Shared SQLite persistence and CSV export for the Email Extractor."""
from pathlib import Path
import csv
import sqlite3
from typing import Iterable, Mapping

DEFAULT_DB = Path(__file__).resolve().parents[1] / "emails.db"


def init_db(db_file=DEFAULT_DB):
    with sqlite3.connect(db_file) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS emails (
            email TEXT PRIMARY KEY,
            title TEXT,
            website TEXT
        )""")


def save_email(email: str, title: str = "", website: str = "", db_file=DEFAULT_DB):
    with sqlite3.connect(db_file) as conn:
        conn.execute(
            "INSERT OR IGNORE INTO emails(email,title,website) VALUES (?,?,?)",
            (email, title, website),
        )


def save_results(results: Iterable[Mapping], db_file=DEFAULT_DB):
    with sqlite3.connect(db_file) as conn:
        conn.executemany(
            "INSERT OR IGNORE INTO emails(email,title,website) VALUES (?,?,?)",
            [(r.get("email", ""), r.get("title", ""), r.get("website", "")) for r in results],
        )


def export_csv(filename="emails.csv", db_file=DEFAULT_DB):
    init_db(db_file)
    with sqlite3.connect(db_file) as conn, open(filename, "w", newline="", encoding="utf-8") as f:
        rows = conn.execute("SELECT email,title,website FROM emails")
        writer = csv.writer(f)
        writer.writerow(["Email", "Title", "Website"])
        writer.writerows(rows)
