"""Portable TXT/CSV contact interchange helpers."""
import csv
import re
EMAIL = re.compile(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,63}$", re.I)

def normalize(items):
    return sorted({x.strip().lower() for x in items if x and EMAIL.match(x.strip())})

def import_emails_txt(path):
    with open(path, encoding="utf-8") as f:
        return normalize(f)

def import_emails_csv(path, column="email"):
    with open(path, newline="", encoding="utf-8") as f:
        return normalize(r.get(column, "") for r in csv.DictReader(f))

def export_emails_txt(emails, path):
    with open(path, "w", encoding="utf-8") as f:
        values = normalize(emails); f.write("\n".join(values) + ("\n" if values else ""))

def export_emails_csv(emails, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["email"]); w.writerows([[e] for e in normalize(emails)])
