from nonebot import on_command, CommandSession
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