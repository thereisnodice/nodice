from nonebot import on_command, CommandSession
import random

__plugin_name__ = 'SG人物作成'
__plugin_usage__ = (
    '用法：\n'
    '.sg\n'
)

@on_command('sg', aliases=('轮回游戏'),only_to_me=False)
async def sg(session: CommandSession):
    attr=[]
    for i in range(6):
        attr.append(str(random.randint(1,3)+random.randint(1,3)))
    message=(f'壮硕值:{attr[0]},爆发力:{attr[1]}协调性:{attr[2]}精神力:{attr[3]}反应力:{attr[4]}幸运值:{attr[5]}\n'
             '不要忘了还有10点自由属性点哦。'
            )
    await session.send(message)