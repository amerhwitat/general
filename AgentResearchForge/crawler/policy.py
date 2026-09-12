from urllib.parse import urlparse
import ipaddress

class CrawlPolicy:
    def __init__(self, allow_onion: bool = False):
        self.allow_onion = allow_onion

    def validate(self, url: str, onion: bool = False) -> bool:
        parsed = urlparse(url)
        if parsed.username or parsed.password:
            return False
        if parsed.scheme not in {'http', 'https'}:
            return False
        host = (parsed.hostname or '').lower().rstrip('.')
        if onion:
            return self.allow_onion and host.endswith('.onion')
        if host.endswith('.onion'):
            return False
        try:
            addr = ipaddress.ip_address(host)
            return not (addr.is_private or addr.is_loopback or addr.is_link_local or addr.is_multicast)
        except ValueError:
            return bool(host)
