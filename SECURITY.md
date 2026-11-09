# Security and dependencies

The control view and panel require an authenticated HA administrator. Services with a user context check administrator permissions; HA automations without a user context are trusted system actions.

This integration controls calls and plays audio. It does not manage locks, authenticate visitors or treat face recognition as permission to unlock a door.

Use HTTPS and grant microphone access only to your own HA frontend. VoIP transport belongs to the separately installed VoIP Stack. Recordings, upload keys and LAN restrictions belong to the recorder/Voice Inbox path. Do not expose uploads or SIP publicly just to make a test work.

No credentials belong in this repository. Logs can include caller/device names: redact private information, HA tokens and upload keys before reporting an issue. Use private GitHub vulnerability reporting if enabled, otherwise contact the maintainer privately for sensitive reports.
