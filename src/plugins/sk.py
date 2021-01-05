from nonebot import on_command, CommandSession
import random

__plugin_name__ = 'SK人物作成'
__plugin_usage__ = (
    '用法：\n'
    '.sk'
)

@on_command('sk', aliases=('时空之轮'),only_to_me=False)
async def sg(session: CommandSession):
    try:round_num=int(session.current_arg_text.strip())
    except:round_num=1
    message=''
    if not round_num or round_num>10:return '非法轮数'
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