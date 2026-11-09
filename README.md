<img width="1892" height="664" alt="p401" src="https://github.com/user-attachments/assets/b3687db0-074a-4da7-9f69-ac99a090e7d7" />

# P4 Doorbell

A dedicated front-door panel for Home Assistant. **VoIP Stack handles calls; the project P4 recorder and Voice Inbox handle voice messages.**

Developed by hruba202 with assistance from **OpenAI ChatGPT / Codex**. [VoIP Stack](https://github.com/n-IA-hane/esphome-intercom) by n-IA-hane is installed separately; its implementation is not bundled here.
- Voice Inbox-Integration for the doorbell, recording and playback of messages—install this along with the integration.
- https://github.com/hruba202/voice-inbox

## Features

- Door camera alongside a VoIP phone card.
- Ring 1–3 HA browser phones, with the first answer winning through VoIP Stack.
- Prerecorded reply: claim the corresponding ringing call, end it, then play local media at the door.
- Optional voice-message sequence after a fresh observed unanswered-call timeout.
- Visitor button: ring, confirm recording after the prompt, then stop and save.
- Independent HA camera/player selection and reconfiguration without recreating the entry.

## Requirements and limits

Minimum declared HA version: **2026.10.3**. The project VoIP baseline is commit `6581cfea712d0e13bf88c5aff3fa97b9e27123ab`. Newer VoIP releases require qualification: this integration depends on its public services, phone-state attributes, entity suffixes and card resource URL.

The caller must be an existing ESPHome device working in VoIP Stack. P4 is the tested profile. Receivers are **HA browser phones**, not arbitrary SIP/ESP receivers. One doorbell per HA instance, with 1–3 receivers. The panel requires an HA administrator. Browser calls require HTTPS, media permissions and an active loaded frontend; a closed or sleeping browser is not a reliable receiver.

Camera and player can be separate HA entities. The player must be audible at the door and play the chosen HA media. Recording prompts require observable playback start and completion. Selecting a camera does not turn snapshots into a stream or enable SIP video transmission.

Setup forms are English/Czech. The runtime panel, entity names and messages remain **Czech**. This is a community integration, not an official Home Assistant integration.

## Install and configure

Intended repository: `https://github.com/hruba202/p4-doorbell`. Publication and public-catalog acceptance are separate steps; see PUBLISHING.md.

1. Install/configure VoIP Stack separately and verify a call between the door ESP and each receiving browser phone.
2. Add this repository to HACS / Marketplace as **Integration**, download, then restart HA.
3. In Settings → Devices & services → Add integration, search **Dveřní zvonek P4**.
4. Select the caller ESP, exact VoIP caller name, its VoIP State sensor, camera, player and 1–3 browser phones.
5. Select a prerecorded reply from local HA media and its button label.
6. Open **Dveřní zvonek** in the sidebar (`/p4-doorbell`); choose the phone belonging to that physical display.
7. Press **Zapojit vybrané panely** to enroll receivers in the generated ring group. Existing groups are retained. Disable receiver auto-answer. Test with **Zazvonit z P4**.

Manual alternative: copy `custom_components/p4_doorbell` into HA's configuration directory, then restart. This is not an app/add-on. Do not run two copies of the same domain.

## Voice messages

Calls/replies can be used without setting up recording. For messages, first verify the P4 recorder uploads successfully to Voice Inbox. Then open **Configure** and select the prompt and recorder entities: record, cancel, busy, status and last-call reason. These entities must still belong to the selected door ESP.


Automatic fallback is opt-in and requires fresh ringing followed by `timeout`. An answered call or stale timeout does not qualify. Button mode waits up to 60 seconds after the prompt for a press, then a press during recording requests save. Presses during calls/prompts/uploads do not start competing operations. Already started uploads cannot be recalled by Cancel.

Native VoIP Stack voicemail is a separate path and is not enabled here. Do not enable both fallbacks for the same call without testing their interaction. Voice Inbox and P4 recorder firmware are separate dependencies, not included in this package.

## Update and rollback

Version **0.3.3** keeps the executable behavior of 0.3.2 and adds distribution metadata, setup translations and brand assets. The domain `p4_doorbell`, API, entry version and entity identities remain unchanged. Back up HA and the old integration, install the files, fully restart HA and refresh the browser. **Do not remove/recreate the entry.**

Use **Reconfigure** to change camera/player only. Finish calls and cancel pending message sequences first. Caller, receivers and recorder settings stay unchanged. Rollback: restore the previous integration files and restart; if changing media, select the original entities first. Firmware and Voice Inbox recordings are not modified.

## Troubleshooting and boundaries

- First make the regular VoIP card work. Missing `_call_state`, `_ring_group` or `_auto_answer` means unsupported/missing receiver entities; do not fabricate entities to bypass checks.
- Test media playback and the camera directly in HA before using them here.
- No built-in presence routing, lock control, face recognition or universal SIP endpoint support.
- Removing this integration does not uninstall VoIP or delete Voice Inbox recordings. Added receiver membership in `P4-dvere-…` is not automatically removed; remove only that group if no longer needed.
- Newer VoIP versions, independent IP-camera playback and a fresh Marketplace install are not yet fully qualified.

See [VALIDATION.md](VALIDATION.md), [PUBLISHING.md](PUBLISHING.md), [SECURITY.md](SECURITY.md) and [CHANGELOG.md](CHANGELOG.md). Never include credentials or private recordings in issue reports.

<img width="1891" height="947" alt="p402" src="https://github.com/user-attachments/assets/3acdb52a-0f91-4677-a8b9-ed0c3c0fb5f8" />


