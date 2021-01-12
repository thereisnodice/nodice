import os
import json
import yaml
import random
import re
from .calculator import Calculator

def get_deck_list():
    deck_list_json=load_decks()
    message='读取到以下牌堆：'
    for i in deck_list_json.keys():
        if i[0]=='_':continue
        message+='\n'+i
    return message

def load_decks():
    deck_list_data={}
    deck_list = os.listdir(os.path.join(os.path.dirname(__file__),'decks'))
    for i in deck_list:
        f=open(os.path.join(os.path.dirname(__file__),'decks',i),'r',encoding='utf-8')
        if i[len(i)-1]=='n':deck_list_data.update(json.loads(f.read()))
        else:deck_list_data.update(yaml.load(f.read()))
        f.close()
    return deck_list_data

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
        while '[' in value:
            value=get_calculator(value)
        if i:message+='\n'
        message+=value
    return message

def get_sub_key(value):
    mode=False
    l=value[:value.index('}')]
    r=value[value.index('}')+1:]
    key_sub=l[l.rindex('{')+1:]
    l=l[:l.rindex('{')]
    if key_sub[0]=='%':
        mode=True
        key_sub=key_sub[1:]

    return l+get_value(key_sub,1,mode)+r

def get_calculator(value):
    l=value[:value.index(']')]
    r=value[value.index(']')+1:]
    key_sub=l[l.rindex('[')+1:]
    l=l[:l.rindex('[')]
    cal=Calculator(key_sub)
    cal.calculate_with_bracket()
    return l+str(int(cal.result))+r

def separate_deckname_and_num(args,mode=False):
    args=args.split()
    deckname=args[0]
    try:num=int(args[1])
    except:num=1
    return '抽到了：\n'+get_value(deckname,num,mode)

# 调试用
if __name__=='__main__':
    print(separate_deckname_and_num(input()))