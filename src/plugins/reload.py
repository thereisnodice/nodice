from nonebot import on_command, CommandSession, permission
import nonebot
import os

__plugin_name__ = '[A]reload'
__plugin_usage__ = r"""
Reload all plugins.
*Required admin permission*
Command(s):
 - /reload
""".strip()

PLUGINS_PATH = "."
PLUGINS_PATH = os.path.join(os.path.dirname(__file__), PLUGINS_PATH)

@on_command('reload', permission=permission.SUPERUSER)
async def reload(session: CommandSession):
    for f in os.listdir(PLUGINS_PATH):
        if f != '__pycache__' and f != 'reload.py' and f[0] != '_':
            plugin_path = 'plugins.' + os.path.splitext(f)[0]
            ret = nonebot.plugin.reload_plugin(plugin_path)
            if not ret:
                ret = nonebot.plugin.load_plugin(plugin_path)
            if not ret:
                await session.send("[WARNING] Failed to reload '%s' plugin!" %plugin_path)
    await session.send("Plugins reloaded.")