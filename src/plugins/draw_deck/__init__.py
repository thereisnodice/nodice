from nonebot import on_command, CommandSession
from nonebot.command import call_command
from .decks import get_deck_list,separate_deckname_and_num

__plugin_name__ = '拓展牌堆'
__plugin_usage__ = (
    'draw list 牌堆列表'
    'draw deckname 抽取牌堆'
)

@on_command('draw',only_to_me=False)
async def draw(session: CommandSession):
    args=session.current_arg_text.strip()
    if args=='list':await session.send(get_deck_list())
    else:
        await session.send(separate_deckname_and_num(args))

@on_command('ndraw',only_to_me=False)
async def ndraw(session: CommandSession):
    args=session.current_arg_text.strip()
    if args=='list':await session.send(get_deck_list())
    else:
        await session.send(separate_deckname_and_num(args,True))

@on_command('name',only_to_me=False)
async def name(session:CommandSession):
    try:
        await call_command(session.bot,session.event,'draw',current_arg='_name '+str(int(session.current_arg_text.strip())))
    except:
        await call_command(session.bot,session.event,'draw',current_arg='_name_'+session.current_arg_text.strip())

@on_command('ti',only_to_me=False)
async def ti(session:CommandSession):
    await call_command(session.bot,session.event,'draw',current_arg='_即时症状')

@on_command('li',only_to_me=False)
async def li(session:CommandSession):
    await call_command(session.bot,session.event,'draw',current_arg='_总结症状')
