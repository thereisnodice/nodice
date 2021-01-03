from nonebot import on_request, RequestSession


# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
        await session.approve()
