from nonebot import on_command, CommandSession,get_loaded_plugins

@on_command('usage', aliases=['help','使用帮助', '帮助', '使用方法'],only_to_me=False)
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    plugins = list(filter(lambda p: p.name,get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果用户没有发送参数，则发送功能列表
        await session.send(
            '\n目前支持的功能有：' + '\n'.join(p.name for p in plugins))
        return

    # 如果发了参数则发送相应命令的使用帮助
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)