from nonebot import on_command, CommandSession
import random

__plugin_name__ = 'SG人物作成'
__plugin_usage__ = (
    '用法：\n'
    '.sk'
)

@on_command('sk', aliases=('时空之轮'),only_to_me=False)
async def sg(session: CommandSession):
    attr=[]
    for i in range(7):
        attr.append(str(random.randint(1,5)+random.randint(1,5)))
    message=(f'力量:{attr[0]},敏捷:{attr[1]}体力:{attr[2]}精神:{attr[3]}智慧:{attr[4]}魅力:{attr[5]}幸运:{attr[6]}\n'
          '不要忘了还有10点自由属性点哦。'
        )
    await session.send(message)