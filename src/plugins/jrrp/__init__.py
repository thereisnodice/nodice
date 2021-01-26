from nonebot import on_command, CommandSession
from .data_source import get_jrrp
from .sqlite import get_jrrp_on,set_jrrp_on

__plugin_name__ = '今日人品'
__plugin_usage__ = (
    '用法：\n'
    '.jrrp'
)

@on_command('jrrp', aliases=('今日人品'),only_to_me=False)
async def jrrp(session: CommandSession):
    if session.current_arg.strip()=='on':
        set_jrrp_on(session.event.group_id,True)
    elif session.current_arg.strip()=='off':
        set_jrrp_on(session.event.group_id,False)
    else:
        bot_qq_id=str(session.event.self_id)
        qq_id=str(session.event.user_id)
        if(get_jrrp_on(session.event.group_id)):
            await session.send(get_jrrp(bot_qq_id,qq_id))
