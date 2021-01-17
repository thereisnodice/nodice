from nonebot import on_command, CommandSession
from .data_source import get_jrrp

__plugin_name__ = '今日人品'
__plugin_usage__ = (
    '用法：\n'
    '.jrrp'
)

@on_command('jrrp', aliases=('今日人品'),only_to_me=False)
async def jrrp(session: CommandSession):
    bot_qq_id=str(session.event.self_id)
    qq_id=str(session.event.user_id)
    await session.send(get_jrrp(bot_qq_id,qq_id))
