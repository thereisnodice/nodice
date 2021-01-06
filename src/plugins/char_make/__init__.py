from nonebot import on_command, CommandSession
import random

__plugin_name__ = '人物作成'
__plugin_usage__ = (
    'sg 变量之轮（轮回游戏二版）人物作成'
    'sk 时空之轮人物作成'
)

@on_command('sg', aliases=('轮回游戏'),only_to_me=False)
async def sg(session: CommandSession):
    try:round_num=int(session.current_arg_text.strip())
    except:round_num=1
    message=''
    if not round_num or round_num>10:await session.send('非法轮数')
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

@on_command('sk', aliases=('时空之轮'),only_to_me=False)
async def sk(session: CommandSession):
    try:round_num=int(session.current_arg_text.strip())
    except:round_num=1
    message=''
    if not round_num or round_num>10:await session.send('非法轮数')
    for round in range(round_num):
        attr=[]
        for i in range(7):
            attr.append(str(random.randint(1,5)+random.randint(1,5)))
        message_tmp=(f'力量:{attr[0]},敏捷:{attr[1]}体力:{attr[2]}精神:{attr[3]}智慧:{attr[4]}魅力:{attr[5]}幸运:{attr[6]}\n'
            '不要忘了还有10点自由属性点哦。'
            )
        if round:message+='\n'
        message+=message_tmp
    await session.send(message)