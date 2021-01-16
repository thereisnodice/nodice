import random
import re

#是否显示运算过程，先丢这儿。
is_show_detail=True

# 定义一个类储存表达式、输入、运算过程、结果
class WodCalculator:

    def __init__(self,e='',r=0.0):
        self.expression=e
        self.source=e
        self.detail=e
        self.result=r

    def __str__(self):
        return f'{self.expression},{self.source},{self.detail},{self.result}'

    # 掷骰
    def throw_dice(self):

        # 匹配正则
        match_result=re.search(r"([0-9]*)a([0-9]*)",self.expression)

        # 获取骰数，获取不到默认为1，超过100或等于0报错
        try:dice_num=int(match_result.group(1))
        except:dice_num=1
        if not dice_num or dice_num>100:return '非法骰数'

        # 获取加骰
        try:dice_diff=int(match_result.group(2))
        except:dice_diff=10
        if dice_diff<5 or dice_diff>10:return '非法加骰'

        # 消息初始化
        self.source=str(dice_num)+'A'+str(dice_diff)
        self.detail=''

        # 模拟现实掷骰并统计
        dice_count=0
        while dice_num:
            if dice_count:self.detail+='+'
            self.detail+='['
            for i in range(dice_num):
                dice_result=random.randint(1,10)
                if i:self.detail+=' '
                self.detail+=str(dice_result)
                if dice_result>=dice_diff:dice_num+=1
                if dice_result>=8:dice_count+=1
            self.detail+=']'
            dice_num=dice_num-i-1
            
        self.result=dice_count

    # 提取出轮数和掷骰原因
    def extract_roundnum_and_reason(self):

        expression=self.expression

        # 匹配正则
        match_result=re.search(r"(([0-9]+)#)?([a0-9]*)(.*)",expression)

        # 获取轮数，获取不到默认为1，超过10或等于0报错
        try:round_num=int(match_result.group(2))
        except:round_num=1
        if not round_num or round_num>10:return '非法轮数'

        # 获取表达式
        expression=match_result.group(3).strip().lower()

        # 初始化WodCalculator类
        calculator=WodCalculator(expression)

        # 获取掷骰原因，获取不到默认为空
        try:roll_reason=match_result.group(4).strip()
        except:roll_reason=''

        # 返回消息
        message=''
        if roll_reason!='':message+='由于'+roll_reason
        message+='掷出了:'
        for i in range(round_num):
            calculator.throw_dice()
            message+='\n'+calculator.source
            if is_show_detail:message+='='+calculator.detail
            message+='='+str(int(calculator.result))
        return message

# 调试用
if __name__=='__main__':
    while(True):
        print(WodCalculator(input()).extract_roundnum_and_reason())