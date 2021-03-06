import json
import time 
import os
import random
import httpx

# 是否使用溯洄的API以达到与Dice!同步的目的
IS_ONLINE=True

def get_jrrp_local(qq_id):
    day=str(time.localtime(time.time())[2])
    try:
        jrrp_data=open(os.path.join(os.path.dirname(__file__),'jrrp_data.json'),'r',encoding='utf-8')
        jrrp_data_json=json.loads(jrrp_data.read())
        jrrp_data.close()
    except:
        jrrp_data_json={}
    if qq_id in jrrp_data_json.keys() :
        if day!=jrrp_data_json[qq_id]['day']:
            jrrp=str(random.randint(1,100))
            jrrp_data_json[qq_id]={'day':day,'jrrp':jrrp}
    else:
        jrrp=str(random.randint(1,100))
        jrrp_data_json[qq_id]={'day':day,'jrrp':jrrp}
    jrrp_data=open(os.path.join(os.path.dirname(__file__),'jrrp_data.json'),'w',encoding='utf-8')
    jrrp_data.write(json.dumps(jrrp_data_json))
    jrrp_data.close()

    return '你今天的人品值是：'+jrrp_data_json[qq_id]['jrrp']

def get_jrrp_online(bot_qq_id,qq_id):
    url='http://api.kokona.tech:5555/jrrp'
    data={'User-Agent':'NoDice','QQ':bot_qq_id,'v':'20190114','QueryQQ':qq_id}
    res=httpx.post(url=url,data=data)
    return '你今天的人品值是：'+res.text

def get_jrrp(bot_qq_id,qq_id):
    if IS_ONLINE:
        return get_jrrp_online(bot_qq_id,qq_id)
    else:
        return get_jrrp_local(qq_id)

if __name__=='__main__':
    print(get_jrrp('1234567890','1234567890'))