# Identity, teams and P2P

Roles: `admin`, `project_manager`, `product_owner`, `developer`, `tester`, `operator`, `service_manager`, `viewer`, plus custom roles. Permissions are workspace/project/service scoped.

Authentication supports local accounts plus OIDC/OAuth2 integration. MFA should be enabled for administrators. Passwords are never stored in plaintext.

Team collaboration uses comments, mentions, subscriptions, presence, notifications, shared dashboards and optional P2P replication. P2P pairing is explicit: both peers exchange identity keys and capabilities, an administrator or user accepts the peer, then synchronization uses signed envelopes and sequence numbers. Offline clients queue changes and reconcile after reconnect.

Voice: clients expose push-to-talk/record controls and configurable TTS. Supported engines can include platform APIs, Whisper-compatible local STT, Piper/Coqui-compatible TTS, Android SpeechRecognizer, iOS Speech framework and browser Speech APIs. Language/locale and voice selection are user settings. Audio is not uploaded unless the user explicitly enables a remote service.
