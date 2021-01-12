import os
import json
import yaml
import random

def get_deck_list():
    deck_list_json=load_decks()
    message='读取到一下牌堆：'
    for i in deck_list_json.keys():
        message+='\n'+i
    return message

def load_decks():
    deck_list_json={}
    deck_list = os.listdir(os.path.join(os.path.dirname(__file__),'decks'))
    for i in deck_list:
        f=open(os.path.join(os.path.dirname(__file__),'decks',i),'r',encoding='utf-8')
        deck_list_json.update(json.loads(f.read()))
        f.close()
    return deck_list_json

def get_value(key,num=1,mode=False):
    value_list=load_decks()[key]
    message=''
    for i in range(num):
        if mode:
            value=value_list.pop(random.randint(0,len(value_list)-1))
        else:
            value=value_list[random.randint(0,len(value_list)-1)]
        while '{' in value:
            value=get_sub_key(value)
        if i:message+='\n'
        message+=value
    return message

def get_sub_key(value):
    l=value[:value.index('}')]
    r=value[value.index('}')+1:]
    key_sub=l[l.rindex('{')+1:]
    l=l[:l.rindex('{')]
    return l+get_value(key_sub)+r

def separate_deckname_and_num(args,mode=False):
    args=args.split()
    deckname=args[0]
    try:num=int(args[1])
    except:num=1
    return '抽到了：\n'+get_value(deckname,num,mode)

# 调试用
if __name__=='__main__':
    print(separate_deckname_and_num(input()))