from nonebot import on_command, CommandSession
import json
import time 
import os
import random

__plugin_name__ = '今日人品'
__plugin_usage__ = (
    '用法：\n'
    '.jrrp'
)

@on_command('jrrp', aliases=('今日人品'),only_to_me=False)
async def jrrp(session: CommandSession):
    day=str(time.localtime(time.time())[2])
    qq_id=str(session.event.user_id)
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
    await session.send('你今天的人品值是：'+jrrp_data_json[qq_id]['jrrp'])
