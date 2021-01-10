from nonebot import on_command, CommandSession
from .calculator import Calculator

__plugin_name__ = '人物作成'
__plugin_usage__ = (
    'sg 变量之轮（轮回游戏二版）人物作成'
    'sk 时空之轮人物作成'
)

@on_command('sg', aliases=('轮回游戏'),only_to_me=False)
async def sg(session: CommandSession):

    try:round_num=int(session.current_arg_text.strip())
    except:round_num=1
    if not round_num or round_num>10:await session.send('非法轮数')

    message=''
    for round in range(round_num):
        if round:message+='\n'
        attr_name=['壮硕值','爆发力','协调性','精神力','反应力','幸运值']
        attr_cmd=['2d3','2d3','2d3','2d3','2d3','2d3']
        for i in range(len(attr_name)):
            attr_cal=Calculator(attr_cmd[i])
            attr_cal.calculate_with_bracket()
            if i:message+=','
            message+=attr_name[i]+':'+str(int(attr_cal.result))
        
    await session.send(message)

@on_command('sk', aliases=('时空之轮'),only_to_me=False)
async def sk(session: CommandSession):

    try:round_num=int(session.current_arg_text.strip())
    except:round_num=1
    if not round_num or round_num>10:await session.send('非法轮数')

    message=''
    for round in range(round_num):
        if round:message+='\n'
        attr_name=['力量','敏捷','体力','精神','智慧','魅力','幸运']
        attr_cmd=['2d5','2d5','2d5','2d5','2d5','2d5','2d5']
        for i in range(len(attr_name)):
            attr_cal=Calculator(attr_cmd[i])
            attr_cal.calculate_with_bracket()
            if i:message+=','
            message+=attr_name[i]+':'+str(int(attr_cal.result))

    await session.send(message)
    
@on_command('coc', aliases=('克苏鲁的呼唤'),only_to_me=False)
async def coc(session: CommandSession):

    try:round_num=int(session.current_arg_text.strip())
    except:round_num=1
    if not round_num or round_num>10:await session.send('非法轮数')

    message=''
    for round in range(round_num):
        if round:message+='\n'
        attr_name=["力量", "体质", "体型", "敏捷", "外貌", "智力", "意志", "教育", "幸运"]
        attr_cmd=['3d6*5','3d6*5','(2d6+6)*5','3d6*5','3d6*5','(2d6+6)*5','3d6*5','(2d6+6)*5','3d6*5']
        attr_count=0
        for i in range(len(attr_name)):
            attr_cal=Calculator(attr_cmd[i])
            attr_cal.calculate_with_bracket()
            attr_count+=attr_cal.result
            if i:message+=','
            message+=attr_name[i]+':'+str(int(attr_cal.result))
        message +="\n总计:"+str(int(attr_count-attr_cal.result))+'/'+str(int((attr_count))

    await session.send(message)
    
@on_command('dnd', aliases=('龙与地下城'),only_to_me=False)
async def coc(session: CommandSession):

    try:round_num=int(session.current_arg_text.strip())
    except:round_num=1
    if not round_num or round_num>10:await session.send('非法轮数')

    message=''
    for round in range(round_num):
        if round:message+='\n'
        attr_name=["力量", "体质", "敏捷", "智力", "感知", "魅力"]
        attr_cmd=['4d6k3','4d6k3','4d6k3','4d6k3','4d6k3','4d6k3']
        for i in range(len(attr_name)):
            attr_cal=Calculator(attr_cmd[i])
            attr_cal.throw_dice()
            if i:message+=','
            message+=attr_name[i]+':'+str(int(attr_cal.result))

    await session.send(message)