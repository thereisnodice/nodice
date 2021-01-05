from nonebot import on_command, CommandSession, permission
from nonebot.plugin import reload_plugin,load_plugin
import subprocess
from subprocess import PIPE, STDOUT, CalledProcessError
import os

PLUGINS_PATH = "."
PLUGINS_PATH = os.path.join(os.path.dirname(__file__), PLUGINS_PATH)

@on_command('reload', permission=permission.SUPERUSER)
async def reload(session: CommandSession):
    for f in os.listdir(PLUGINS_PATH):
        if f != '__pycache__':
            plugin_path = 'plugins.' + os.path.splitext(f)[0]
            ret = reload_plugin(plugin_path)
            if not ret:
                ret = load_plugin(plugin_path)
            if not ret:
                await session.send("[WARNING] Failed to reload '%s' plugin!" %plugin_path)
    await session.send("Plugins reloaded.")