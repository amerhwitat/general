from __future__ import annotations

import re
import socket
from dataclasses import dataclass
from urllib.parse import urlparse

import requests

EMAIL_REGEX = re.compile(r"(?<![\w.+-])([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)(?![\w.-])")

@dataclass(frozen=True)
class EmailResult:
    email: str
    page_title: str
    website: str
    source_url: str
    valid_mx: bool | None = None
    status: str = "discovered"

def fetch_page(url: str, timeout: float = 10.0, max_bytes: int = 5_000_000) -> tuple[str, str]:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return "", ""
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True, headers={"User-Agent": "ChimeraEmailExtractor/1.0"}, stream=True)
        response.raise_for_status()
        chunks, size = [], 0
        for chunk in response.iter_content(65536, decode_unicode=True):
            if not chunk:
                continue
            size += len(chunk)
            if size > max_bytes:
                break
            chunks.append(chunk)
        html = "".join(chunks)
        return html, response.url
    except requests.RequestException:
        return "", ""

def extract_emails(html: str) -> set[str]:
    return {m.group(1).strip(".,;:<>[](){}\"").lower() for m in EMAIL_REGEX.finditer(html)}

def extract_page_title(html: str) -> str:
    match = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", match.group(1))).strip() if match else ""

def validate_email(email: str) -> bool:
    parts = email.rsplit("@", 1)
    if len(parts) != 2 or not parts[1]:
        return False
    domain = parts[1].rstrip(".")
    try:
        import dns.resolver
        return bool(dns.resolver.resolve(domain, "MX", lifetime=5))
    except Exception:
        try:
            socket.getaddrinfo(domain, 25)
            return True
        except OSError:
            return False
