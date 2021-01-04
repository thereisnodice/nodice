from nonebot import on_command, CommandSession
from .calculator import *

__plugin_name__ = '掷骰'
__plugin_usage__ = (
    '用法：\n'
    '.r 2d3\n'
    '注意这里是有空格的,目前暂时不支持加减乘除\n'
)

@on_command('roll', aliases=('r','掷骰'),only_to_me=False)
async def roll(session: CommandSession):
    dice_expression = session.current_arg_text.strip()
    await session.send(dice_caculator(dice_expression))

'''
@roll.args_parser
async def _(session: CommandSession):
    args = session.current_arg_text.strip().split(' ', 1)

    if session.is_first_run:
        if args[0]:
            session.state['city'] = args[0]
        return
    if not args[0]:
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = args[0]
'''