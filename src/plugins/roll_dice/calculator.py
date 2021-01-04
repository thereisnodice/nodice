import random
import re

# 替换标准骰子及惩罚奖励骰(3d6, 4d6k3)
def dice_caculator(dice_expression):

    message=dice_expression+' = [ '

    # 匹配标准掷骰
    match_result=re.search(r"([0-9]*)d([0-9]*)(k([0-9]*))?",dice_expression)

    dice_num=int(match_result.group(1))
    dice_face=int(match_result.group(2))
    dice_pick=int(match_result.group(4))
    dice_result_list=[]

    for i in range(dice_num):
        dice_result=random.randint(1,dice_face)
        dice_result_list.append(dice_result)
    
    if dice_pick:
        dice_result_list.sort(reverse=True)
        for i in range(len(dice_result_list)-dice_pick):dice_result_list.pop()

    dice_count=0
    for i in range(len(dice_result_list)):
        if i:message+=' + '
        message+=str(dice_result_list[i])
        dice_count+=dice_result_list[i]
    message+=' ] = '+str(dice_count)
    count=0

    return message.upper()