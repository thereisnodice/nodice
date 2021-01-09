from nonebot import on_command, CommandSession
from .calculator import *

__plugin_name__ = '掷骰'
__plugin_usage__ = (
    '用法：\n'
    '.r(h) 4#3d6k2+5 reason\n'
    '注意这里命令与参数之间是有空格的!'
)

@on_command('roll', aliases=('r','掷骰'),only_to_me=False)
async def roll(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    await session.send(extract_roundnum_and_reason(dice_expression))

@on_command('roll_hide', aliases=('rh','暗骰'),only_to_me=False)
async def roll_hide(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    if session.event.message_type=='group':
        await session.send('在群聊'+str(session.event.group_id)+'中暗骰，'
                        +extract_roundnum_and_reason(dice_expression),ensure_private=True)
    else:
        await session.send(extract_roundnum_and_reason(dice_expression))