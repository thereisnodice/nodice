from nonebot import on_request,RequestSession,on_command,CommandSession
from nonebot.permission import GROUP_ADMIN,SUPERUSER
from .sqlite import set_bot_on

# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
        await session.approve()

@on_command('dismiss',permission=GROUP_ADMIN|SUPERUSER)
async def dismiss(session: CommandSession):
    await session.bot.set_group_leave(group_id=session.event.group_id)

@on_command('bot',only_to_me=False,permission=GROUP_ADMIN|SUPERUSER)
async def bot(session: CommandSession):
    if session.current_arg.strip()=='on':
        set_bot_on(session.event.group_id,True)
    else:
        set_bot_on(session.event.group_id,False)