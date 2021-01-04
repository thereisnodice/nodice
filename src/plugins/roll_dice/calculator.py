import random
import re

# 替换标准骰子及惩罚奖励骰(3d6, 4d6k3)
def dice_caculator(dice_expression):

    

    # 匹配标准掷骰
    match_result=re.search(r"([0-9]*)d([0-9]*)(k([0-9]*))?",dice_expression)
    try:dice_num=int(match_result.group(1))
    except:dice_num=1
    try:dice_face=int(match_result.group(2))
    except:dice_face=100
    try:dice_pick=int(match_result.group(4))
    except:dice_pick=dice_num
    
    
    if not dice_num or dice_num>100:return '非法骰数'
    if not dice_face or dice_face>1000:return '非法骰面'
    if not dice_pick or dice_pick>dice_num:return '非法骰数'

    dice_result_list=[]
    for i in range(dice_num):
        dice_result=random.randint(1,dice_face)
        dice_result_list.append(dice_result)

    message=str(dice_num)+'D'+str(dice_face)
    if(dice_pick<dice_num):message+'K'+str(dice_pick)
    message+=' = [ '
    dice_count=0
    for i in range(dice_pick):
        if i:message+=' + '
        message+=str(dice_result_list[i])
        dice_count+=dice_result_list[i]
    message+=' ] = '+str(dice_count)
    count=0

    return message.upper()