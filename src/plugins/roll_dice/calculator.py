import random
import re

#是否显示运算过程，先丢这儿。
is_show_detail=True

# 定义一个类储存表达式、运算过程、结果
# 目前没有实际使用
class calculator:
    expression=''
    detail=''
    result=0

    def __init__(self,e,d,r):
        self.expression=e
        self.detail=d
        self.result=r

# 提取出轮数和掷骰原因
def extract_roundnum_and_reason(expression):

    # 匹配正则
    match_result=re.search(r"(([0-9]+)#)?([dk0-9\.+\-*/\^\(\)]*)(.*)",expression)

    # 获取轮数，获取不到默认为1，超过10或等于0报错
    try:round_num=int(match_result.group(2))
    except:round_num=1
    if not round_num or round_num>10:return '非法轮数'

    # 获取表达式
    expression=match_result.group(3).strip()

    # 获取掷骰原因，获取不到默认为空
    try:roll_reason=match_result.group(4).strip()
    except:roll_reason=''

    # 返回消息
    message=''
    if roll_reason!='':message+='由于'+roll_reason
    message+='掷出了:'
    for i in range(round_num):
        message+='\n'+expression.upper()+'='+calculate_with_bracket(expression)
    return message
    
 # 如果有括号就先计算括号内的表达式
def calculate_with_bracket(expression):

    try:
        l=expression[:expression.index(')')]
        r=expression[expression.index(')')+1:]
        m=l[l.rindex('(')+1:]
        l=l[:l.rindex('(')]
        return calculate_with_bracket(l+str(calculate_without_bracket(m))+r)
    except:
        return str(int(calculate_without_bracket(expression)))

# 计算无括号的表达式
def calculate_without_bracket(expression):

    if '+' in expression:
        l=expression[:expression.index('+')]
        r=expression[expression.index('+')+1:]
        return calculate_without_bracket(l)+calculate_without_bracket(r)
    elif '-' in expression:
        l=expression[:expression.index('-')]
        r=expression[expression.index('-')+1:]
        return calculate_without_bracket(l)-calculate_without_bracket(r)
    elif '*' in expression:
        l=expression[:expression.index('*')]
        r=expression[expression.index('*')+1:]
        return calculate_without_bracket(l)*calculate_without_bracket(r)
    elif '/' in expression:
        l=expression[:expression.index('/')]
        r=expression[expression.index('/')+1:]
        return calculate_without_bracket(l)/calculate_without_bracket(r)
    elif '^' in expression:
        l=expression[:expression.index('^')]
        r=expression[expression.index('^')+1:]
        return calculate_without_bracket(l)**calculate_without_bracket(r)
    elif re.search(r"([0-9]*)d([0-9]*)(k([0-9]*))?",expression) or expression=='':
        return throw_dice(expression)
    else:return float(expression)

# 掷骰
def throw_dice(dice_expression):

    # 匹配正则
    match_result=re.search(r"([0-9]*)d([0-9]*)(k([0-9]*))?",dice_expression)

    # 获取骰数，获取不到默认为1，超过100或等于0报错
    try:dice_num=int(match_result.group(1))
    except:dice_num=1
    if not dice_num or dice_num>100:return '非法骰数'

    # 获取骰面，获取不到默认为100，超过1000或等于0报错
    try:dice_face=int(match_result.group(2))
    except:dice_face=100
    if not dice_face or dice_face>1000:return '非法骰面'

    # 获取有效骰数，获取不到默认为骰数，超过骰数或等于0报错
    try:dice_pick=int(match_result.group(4))
    except:dice_pick=dice_num
    if not dice_pick or dice_pick>dice_num:return '非法有效骰数'

    # 模拟现实掷骰
    dice_result_list=[]
    for i in range(dice_num):
        dice_result=random.randint(1,dice_face)
        dice_result_list.append(dice_result)
    dice_result_list.sort(reverse=True) #降序排列，为有效骰作准备

    # 消息初始化
    message_short='\n'+str(dice_num)+'D'+str(dice_face)
    if(dice_pick<dice_num):message_short+='K'+str(dice_pick)
    message_detail=message_short+' = '+'[ '

    dice_count=0
    for i in range(dice_num):
        if i:message_detail+=' + '
        if i <dice_pick:
            message_detail+=str(dice_result_list[i])
            dice_count+=dice_result_list[i]
        else:
            message_detail+='('+str(dice_result_list[i])+')'
    message_detail+=' ]'

    return dice_count

# 调试用
if __name__=='__main__':
    while(True):
        print(extract_roundnum_and_reason(input()))