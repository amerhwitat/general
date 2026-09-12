from dataclasses import dataclass
from typing import Literal, Optional

NetworkMode = Literal['offline', 'client', 'server', 'host', 'p2p', 'hybrid']

@dataclass(frozen=True)
class AvatarRef:
    kind: Literal['builtin', 'local']
    id: Optional[str] = None
    sha256: Optional[str] = None
    mime: Optional[str] = None

@dataclass(frozen=True)
class UserProfile:
    nickname: str
    avatar: Optional[AvatarRef] = None

@dataclass(frozen=True)
class NetworkConfig:
    mode: NetworkMode
    host: str = '127.0.0.1'
    port: int = 45678
    application_id: str = 'general-app'
    room: str = 'main'
    nickname: str = 'Player'
    avatar: Optional[AvatarRef] = None
    enable_p2p: bool = True
    tls: bool = True

def normalize_nickname(value: str) -> str:
    value = ' '.join(value.strip().split())
    return (value or 'Player')[:32]

def validate_avatar_mime(mime: str) -> bool:
    return mime.lower() in {'image/png', 'image/jpeg', 'image/webp'}
