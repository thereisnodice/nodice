import httpx
from nonebot import on_command, CommandSession

# 是否使用溯洄的API
IS_ONLINE=True

@on_command('rules', aliases=('规则速查'),only_to_me=False)
async def rules(session: CommandSession):
    bot_qq_id=str(session.event.self_id)
    name=session.current_arg_text.strip()
    await session.send(get_rules(bot_qq_id,name))

def get_rules_online(bot_qq_id,name):
    url='http://api.kokona.tech:5555/rules'
    data={'User-Agent':'NoDice','QQ':bot_qq_id,'v':'20190114','Name':name}
    res=httpx.post(url=url,data=data)
    return res.text

def get_rules_local(name):
    pass

def get_rules(bot_qq_id,name):
    if IS_ONLINE:
        return get_rules_online(bot_qq_id,name)
    else:
        return get_rules_local(name)

if __name__=='__main__':
    print(get_rules_online('123456789','大成功'))