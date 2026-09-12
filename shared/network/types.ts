export type NetworkMode = 'offline' | 'client' | 'server' | 'host' | 'p2p' | 'hybrid';

export interface AvatarRef {
  kind: 'builtin' | 'local';
  id?: string;
  sha256?: string;
  mime?: 'image/png' | 'image/jpeg' | 'image/webp';
}

export interface UserProfile {
  nickname: string;
  avatar?: AvatarRef;
}

export interface NetworkConfig {
  mode: NetworkMode;
  host: string;
  port: number;
  applicationId: string;
  room?: string;
  nickname: string;
  avatar?: AvatarRef;
  enableP2P: boolean;
  tls: boolean;
}

export interface Envelope<T = unknown> {
  v: 1;
  type: string;
  id: string;
  room: string;
  sender: string;
  timestamp: number;
  payload: T;
}

export function normalizeNickname(value: string): string {
  return value.trim().replace(/\s+/g, ' ').slice(0, 32) || 'Player';
}

export function validateAvatarMime(mime: string): mime is AvatarRef['mime'] {
  return mime === 'image/png' || mime === 'image/jpeg' || mime === 'image/webp';
}
