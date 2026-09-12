"""Bounded concurrent HTTP/HTTPS crawling with progress callbacks."""
import asyncio
import re
import aiohttp
from urllib.parse import urlparse

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

async def fetch_page(session, url, timeout=10):
    if urlparse(url).scheme not in {"http", "https"}: return ""
    try:
        async with session.get(url, timeout=timeout, allow_redirects=True) as resp:
            if resp.status >= 400: return ""
            return await resp.text(errors="ignore")
    except (aiohttp.ClientError, asyncio.TimeoutError):
        return ""

async def crawl(urls, progress=None, concurrency=8):
    contacts = set(); completed = 0; sem = asyncio.Semaphore(concurrency)
    async with aiohttp.ClientSession(headers={"User-Agent":"ChimeraEmailExtractor/1.0"}) as session:
        async def one(url):
            nonlocal completed
            async with sem: html = await fetch_page(session, url)
            contacts.update(e.lower() for e in EMAIL_REGEX.findall(html))
            completed += 1
            if progress: progress(completed, len(contacts))
        await asyncio.gather(*(one(u) for u in urls))
    return contacts
