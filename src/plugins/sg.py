from nonebot import on_command, CommandSession
import random

__plugin_name__ = 'SG人物作成'
__plugin_usage__ = (
    '用法：\n'
    '.sg'
)

@on_command('sg', aliases=('轮回游戏'),only_to_me=False)
async def sg(session: CommandSession):
    try:round_num=int(session.current_arg_text.strip())
    except:round_num=1
    message=''
    if not round_num or round_num>10:return '非法轮数'
    for round in range(round_num):
        attr=[]
        for i in range(6):
            attr.append(str(random.randint(1,3)+random.randint(1,3)))
        message_tmp=(f'壮硕值:{attr[0]},爆发力:{attr[1]}协调性:{attr[2]}精神力:{attr[3]}反应力:{attr[4]}幸运值:{attr[5]}\n'
                '不要忘了还有10点自由属性点哦。'
                )
        if round:message+='\n'
        message+=message_tmp
    await session.send(message)