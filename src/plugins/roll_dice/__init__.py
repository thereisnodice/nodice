from nonebot import on_command, CommandSession
from .calculator import BaseCalculator,FateCalculator,WodCalculator,CocCalculator,DndCalculator

__plugin_name__ = '掷骰'
__plugin_usage__ = (
    '用法：\n'
    '.r(h) 4#3d6k2+5 reason\n'
    '注意这里命令与参数之间是有空格的!'
)

@on_command('roll', aliases=('r','掷骰'),only_to_me=False)
async def roll(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    await session.send(BaseCalculator(dice_expression).extract_roundnum_and_reason())

@on_command('roll_hide', aliases=('rh','暗骰'),only_to_me=False)
async def roll_hide(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    if session.event.message_type=='group':
        await session.send('在群聊'+str(session.event.group_id)+'中暗骰，'
                        +BaseCalculator(dice_expression).extract_roundnum_and_reason(),ensure_private=True)
    else:
        await session.send(BaseCalculator(dice_expression).extract_roundnum_and_reason())

@on_command('roll_fate', aliases=('rf','fate'),only_to_me=False)
async def roll_fate(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    await session.send(FateCalculator(dice_expression).extract_roundnum_and_reason())

@on_command('roll_fate_hide', aliases=('rfh','fateh'),only_to_me=False)
async def roll_fate_hide(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    if session.event.message_type=='group':
        await session.send('在群聊'+str(session.event.group_id)+'中暗骰，'
                        +FateCalculator(dice_expression).extract_roundnum_and_reason(),ensure_private=True)
    else:
        await session.send(FateCalculator(dice_expression).extract_roundnum_and_reason())

@on_command('roll_wod', aliases=('w','wod'),only_to_me=False)
async def roll_wod(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    await session.send(WodCalculator(dice_expression).extract_roundnum_and_reason())

@on_command('roll_wod_hide', aliases=('wh','wodh'),only_to_me=False)
async def roll_wod_hide(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    if session.event.message_type=='group':
        await session.send('在群聊'+str(session.event.group_id)+'中暗骰，'
                        +WodCalculator(dice_expression).extract_roundnum_and_reason(),ensure_private=True)
    else:
        await session.send(WodCalculator(dice_expression).extract_roundnum_and_reason())

@on_command('roll_check', aliases=('rc','ra','检定'),only_to_me=False)
async def roll_check(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    await session.send(CocCalculator(dice_expression).roll_check())

@on_command('roll_check_hide', aliases=('rch','rah','暗中检定'),only_to_me=False)
async def roll_check_hide(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    if session.event.message_type=='group':
        await session.send('在群聊'+str(session.event.group_id)+'中暗骰，'
                        +CocCalculator(dice_expression).roll_check(),ensure_private=True)
    else:
        await session.send(CocCalculator(dice_expression).roll_check())

@on_command('develop_check', aliases=('en','成长检定'),only_to_me=False)
async def develop_check(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    await session.send(CocCalculator(dice_expression).develop_check())

@on_command('san_check', aliases=('sc','理智检定'),only_to_me=False)
async def develop_check(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    await session.send(CocCalculator(dice_expression).san_check())