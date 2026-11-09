# Validation — 2026-11-09

## Evidence

- The owner reported the 0.3.1 test UI looked good and confirmed the corrected integration name in 0.3.2. This is not evidence that every new media configuration was tested.
- All Python implementation files and panel.js in 0.3.3 are byte-identical to the 0.3.2 test ZIP. Metadata, setup translations, action description and icons changed.
- All **42 regression tests passed** on Python 3.14.2: call arbitration, fresh/stale timeout, messages, visitor presses, HTTP errors and media reconfiguration. They use HA doubles rather than a real HA instance. Windows asyncio tests ran outside the sandbox; no HA connection was made.
- JavaScript syntax passed `node --check`. Packaging validates Python/JSON/YAML syntax, translation key parity, the exact Czech name, archive contents and SHA256.

## Not verified

- HACS validation and hassfest on GitHub: workflows prepared, not run by this task.
- A fresh Marketplace installation and full HA config-flow/lifecycle test of 0.3.3.
- Specific third-party IP cameras/players and newer VoIP versions. The current same-device P4 setup remains the reference.
- Complete English runtime panel: not implemented; Czech runtime intentionally preserved.

No deployment, repository creation, release publication or firmware change was performed. The local test suite is not evidence of approval for the public Marketplace catalog. GitHub validation and clean-install testing must pass before publishing the release.
