from nonebot import on_request,RequestSession,on_command,CommandSession
from nonebot.permission import GROUP_ADMIN,SUPERUSER

# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
        await session.approve()

@on_command('dismiss',permission=GROUP_ADMIN|SUPERUSER)
async def dismiss(session: CommandSession):
    await session.bot.set_group_leave(group_id=session.event.group_id)

@on_command('bot',only_to_me=False)
async def bot(session: CommandSession):
        pass