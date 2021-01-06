import random
import re

# 标准骰子
def dice_caculator(dice_expression):

    is_show_detail=True

    # 匹配标准掷骰
    match_result=re.search(r"(([0-9]*)#)?(([0-9]*)d([0-9]*))?(k([0-9]*))?(.*)",dice_expression.lower())
    try:round_num=int(match_result.group(2))
    except:round_num=1
    try:dice_num=int(match_result.group(4))
    except:dice_num=1
    try:dice_face=int(match_result.group(5))
    except:dice_face=100
    try:dice_pick=int(match_result.group(7))
    except:dice_pick=dice_num
    roll_reason=match_result.group(8)
    
    if not round_num or round_num>10:return '非法轮数'
    if not dice_num or dice_num>100:return '非法骰数'
    if not dice_face or dice_face>1000:return '非法骰面'
    if not dice_pick or dice_pick>dice_num:return '非法骰数'

    message='由于 '+roll_reason+' 掷出了:\n'
    for round in range(round_num):
        dice_result_list=[]
        for i in range(dice_num):
            dice_result=random.randint(1,dice_face)
            dice_result_list.append(dice_result)

        message_tmp=str(dice_num)+'D'+str(dice_face)
        if(dice_pick<dice_num):message_tmp+='K'+str(dice_pick)
        message_tmp+=' = '
        if is_show_detail:message_tmp+='[ '
        dice_count=0
        for i in range(dice_pick):
            if is_show_detail:
                if i:message_tmp+=' + '
                message_tmp+=str(dice_result_list[i])
            dice_count+=dice_result_list[i]
        if is_show_detail:
            message_tmp+=' ]'
        message_tmp+=' = '+str(dice_count)
        count=0

        if round:message+='\n'
        message+=message_tmp

    return message.upper()