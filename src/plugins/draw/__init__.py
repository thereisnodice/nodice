from nonebot import on_command, CommandSession
import os
import json
import random

deck_list_json={}

@on_command('draw',only_to_me=False)
async def draw(session: CommandSession):
    arg=session.current_arg_text.strip()
    if arg=='list':await session.send(load_deck())
    else:
        await session.send(deck_list_json[arg][random.randint(1,len(deck_list_json[arg]))])

def load_deck():
    deck_list = os.listdir(os.path.join(os.path.dirname(__file__),'decks'))
    message='读取到以下牌堆：'
    for i in deck_list:
        tmp_json={}
        f=open(os.path.join(os.path.dirname(__file__),'decks',i),'r',encoding='utf-8')
        tmp_json=json.loads(f.read())
        f.close()
        message+="\n"+i
        deck_list_json.update(tmp_json)
    return message

