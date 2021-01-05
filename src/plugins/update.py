import subprocess
from subprocess import PIPE, STDOUT, CalledProcessError
from nonebot import CommandSession, on_command, permission
from __version__ import *

__plugin_name__ = '[E][A]update'
__plugin_usage__ = r"""
从Git上更新NoDice
仅对使用克隆获取仓库有效
【需要管理员权限】
""".strip()

@on_command('update', permission=permission.SUPERUSER)
async def update(session: CommandSession):
    ret = session.get('continue', prompt="这是一个实验性功能，可能导致机器人损坏，是否继续？[y/n]")
    if ret != 'y':
        await session.send("已取消")
        return

    await session.send("Start pulling from git ...")
    try:
        output = subprocess.run(['git', 'pull'], stdout=PIPE, stderr=STDOUT).stdout.decode('utf-8').strip()
        msg = output.replace('https://', '').replace('http://', '') # 防止QQ将链接渲染为卡片
        await session.send(msg.strip())
        await session.send('成功更新至'+version)

    except CalledProcessError as e:
        await session.send(f"Fail to update: {e}")