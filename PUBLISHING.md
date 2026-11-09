# Publication checklist

Proposed repository: **hruba202/p4-doorbell**. Upload the contents of this repository directory, including `.github` and `.gitignore`, not the whole ESPHome project.

1. Review the proposed MIT license. VoIP Stack and firmware are separate dependencies, not bundled code.
2. Create a public repository, enable Issues and set description/topics (`home-assistant`, `hacs`, `doorbell`, `esphome`). If renaming it, update manifest/README URLs.
3. Run **Validate** in Actions: HACS, hassfest, regression tests and JS syntax. These jobs were not run by local preparation; resolve failures without ignoring checks. The external `voip_stack` dependency and local brand assets need validation by the current tools.
4. Test a clean installation with VoIP installed first and an update preserving existing settings. Check ring groups, two missed calls and messages. Record actual HA/VoIP versions.
5. Publish a full release `v0.3.3` only after checks pass. HACS installs the source tree; no `zip_release` is configured. The repository ZIP is for uploading source.
6. Share the custom repository link. Public catalog inclusion is a later PR to `hacs/default`, not automatic approval.

References checked 2026-11-09:
- https://contributors.home-assistant.io/marketplace/guides/catalog/
- https://contributors.home-assistant.io/marketplace/reference/validation/

Development: Python 3.14 (locally 3.14.2) and Node.js. Run `python -m unittest discover -s tests -v` and `node --check custom_components/p4_doorbell/panel.js`. Tests use standard-library HA doubles; they neither install HA nor replace real config-flow/lifecycle testing.
