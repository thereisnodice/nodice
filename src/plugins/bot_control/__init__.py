from nonebot import on_command, CommandSession, permission,get_loaded_plugins
from nonebot.plugin import reload_plugin,load_plugin
import subprocess
from subprocess import PIPE, STDOUT, CalledProcessError
import os

__plugin_name__ = '[A]bot'
__plugin_usage__ = """
[A]bot 查看版本信息
[A]bot reload 重载插件
[EA]bot update 使用git pull更新
"""

@on_command('bot', permission=permission.SUPERUSER)
async def bot(session: CommandSession):
    arg=session.current_arg.strip()
    if arg=='reload':await reload(session)
    elif arg=='update':await update(session)
    else:await version(session)

async def reload(session: CommandSession):
    plugin_list=[]
    for p in get_loaded_plugins():
        plugin_list.append(p.module.__name__)
    for f in os.listdir('./plugins/'):
        if f!='__pycache__':
            plugin_path = 'plugins.' + os.path.splitext(f)[0]
            plugin_list.append(plugin_path)
    for plugin_path in plugin_list:
        ret = reload_plugin(plugin_path)
        if not ret:
            ret = load_plugin(plugin_path)
        if not ret:
            await session.send("[WARNING] Failed to reload '%s' plugin!" %plugin_path)
    await session.send("Plugins reloaded.")

async def update(session: CommandSession):
    await session.send("Start pulling from git ...")
    try:
        output = subprocess.run(['git', 'pull'], stdout=PIPE, stderr=STDOUT).stdout.decode('utf-8').strip()
        msg = output.replace('https://', '').replace('http://', '') # 防止QQ将链接渲染为卡片
        await session.send(msg.strip())
        await reload(session)
        await version(session)
    except CalledProcessError as e:
        await session.send(f"Fail to update: {e}")

async def version(session: CommandSession):
    f=open(os.path.join(os.path.dirname(__file__),'VERSION'),'r',encoding='utf=8')
    VERSION=f.read()
    f.close()
    await session.send('NoDice by Jigsaw Version '+VERSION)