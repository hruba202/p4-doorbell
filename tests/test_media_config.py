"""Exercise media selection/reconfigure against HA doubles, not a live HA."""
import ast
from pathlib import Path
from types import SimpleNamespace as NS
import unittest

SOURCE = Path(__file__).parents[1] / "custom_components/p4_doorbell/config_flow.py"

class Flow:
    def __init_subclass__(cls, **kwargs):
        pass
    def _get_reconfigure_entry(self):
        return self.entry
    def async_show_form(self, **kwargs):
        return kwargs
    def add_suggested_values_to_schema(self, schema, values):
        return schema
    def async_update_reload_and_abort(self, entry, **kwargs):
        return kwargs

scope = dict(config_entries=NS(ConfigFlow=Flow, OptionsFlow=Flow), callback=lambda x: x,
             vol=NS(Schema=lambda x:x, Required=lambda x:x),
             selector=NS(EntitySelector=lambda x:x))
tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
tree.body = [n for n in tree.body if not isinstance(n, (ast.Import, ast.ImportFrom))]
exec(compile(tree, str(SOURCE), "exec"), scope)

class Tests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.flow = scope["DoorbellFlow"]()
        self.controller = NS(lock=NS(locked=lambda:False),
            mailbox=NS(busy=False, watching=False), visitor=NS(handling=False, task=None),
            door_idle=lambda:True)
        self.states = {"camera.ip_camera": NS(state="idle"), "media_player.speaker": NS(state="idle")}
        self.flow.hass = NS(states=NS(get=self.states.get),
                           data={"p4_doorbell":{"controller":self.controller}})
        self.flow.entry = NS(data={"door_device":"p4", "camera":"camera.old", "player":"media_player.old"},
                             options={"record_button":"button.p4_record"})
        self.media = {"camera":"camera.ip_camera", "player":"media_player.speaker"}

    async def test_independent_media_preserves_device_and_recorder(self):
        result = await self.flow.async_step_reconfigure(self.media)
        self.assertEqual(result, {"data_updates":self.media})
        self.assertEqual(self.flow.entry.data["door_device"], "p4")
        self.assertEqual(self.flow.entry.options["record_button"], "button.p4_record")

    async def test_active_call_blocks_change(self):
        self.controller.door_idle = lambda:False
        result = await self.flow.async_step_reconfigure(self.media)
        self.assertEqual(result["errors"], {"base":"busy"})

    async def test_waiting_message_blocks_change(self):
        self.controller.mailbox.watching = True
        result = await self.flow.async_step_reconfigure(self.media)
        self.assertEqual(result["errors"], {"base":"busy"})

    async def test_wrong_domain_or_missing_entity_rejected(self):
        for media in ({**self.media,"camera":"sensor.fake"}, {**self.media,"player":"media_player.missing"}):
            result = await self.flow.async_step_reconfigure(media)
            self.assertEqual(result["errors"], {"base":"door_entities"})

    async def test_unloaded_controller_blocks_change(self):
        self.flow.hass.data.clear()
        result = await self.flow.async_step_reconfigure(self.media)
        self.assertEqual(result["errors"], {"base":"busy"})
