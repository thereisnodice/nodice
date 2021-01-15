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

    # 计算有括号的表达式
    def calculate_with_bracket(self):
       
        expression=self.expression
        try:
            l=WodCalculator(expression[:expression.index(')')])
            r=WodCalculator(expression[expression.index(')')+1:])
            m=WodCalculator(l.expression[l.expression.rindex('(')+1:])
            l=WodCalculator(l.expression[:l.expression.rindex('(')])
            m.calculate_without_bracket()
            tmp=WodCalculator(l.expression+str(m.result)+r.expression)
            tmp.calculate_with_bracket()
            self.result=tmp.result
            if 'D' in l.source or 'D' in m.source or 'D' in r.source:
                self.source=l.source+m.source+r.source
                self.detail=l.detail+m.detail+r.detail
        except:
            self.calculate_without_bracket()
        #print(str(self))

    # 计算无括号的表达式
    def calculate_without_bracket(self):

        expression=self.expression

        if '+' in expression:
            l=WodCalculator(expression[:expression.index('+')])
            r=WodCalculator(expression[expression.index('+')+1:])
            l.calculate_without_bracket()
            r.calculate_without_bracket()
            self.result=l.result+r.result
            if 'D' in l.source or 'D' in r.source:
                self.source=l.source+'+'+r.source
                self.detail=l.detail+'+'+r.detail
        elif '-' in expression:
            l=WodCalculator(expression[:expression.index('-')])
            r=WodCalculator(expression[expression.index('-')+1:])
            l.calculate_without_bracket()
            r.calculate_without_bracket()
            self.result=l.result-r.result
            if 'D' in l.source or 'D' in r.source:
                self.source=l.source+'-'+r.source
                self.detail=l.detail+'-'+r.detail
        elif '*' in expression:
            l=WodCalculator(expression[:expression.index('*')])
            r=WodCalculator(expression[expression.index('*')+1:])
            l.calculate_without_bracket()
            r.calculate_without_bracket()
            self.result=l.result*r.result
            if 'D' in l.source or 'D' in r.source:
                self.source=l.source+'*'+r.source
                self.detail=l.detail+'*'+r.detail
        elif '/' in expression:
            l=WodCalculator(expression[:expression.index('/')])
            r=WodCalculator(expression[expression.index('/')+1:])
            l.calculate_without_bracket()
            r.calculate_without_bracket()
            self.result=l.result/r.result
            if 'D' in l.source or 'D' in r.source:
                self.source=l.source+'/'+r.source
                self.detail=l.detail+'/'+r.detail
        elif '^' in expression:
            l=WodCalculator(expression[:expression.index('^')])
            r=WodCalculator(expression[expression.index('^')+1:])
            l.calculate_without_bracket()
            r.calculate_without_bracket()
            self.result=l.result**r.result
            if 'D' in l.source or 'D' in r.source:
                self.source=l.source+'^'+r.source
                self.detail=l.detail+'^'+r.detail
        elif re.search(r"([0-9]*)d([0-9]*)(k([0-9]*))?",expression) or expression=='':
            self.throw_dice()
        else:
            self.result=float(expression)
        # print(str(self))

    # 掷骰
    def throw_dice(self):

        # 匹配正则
        match_result=re.search(r"([0-9]*)d([0-9]*)(k([0-9]*))?",self.expression)

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
        self.source=str(dice_num)+'D'+str(dice_face)
        if(dice_pick<dice_num):self.source+='K'+str(dice_pick)
        self.detail='['

        # 统计骰子以及计算过程
        dice_count=0
        for i in range(dice_num):
            if i:self.detail+='+'
            if i <dice_pick:
                self.detail+=str(dice_result_list[i])
                dice_count+=dice_result_list[i]
            else:
                self.detail+='('+str(dice_result_list[i])+')'
        self.detail+=']'
        self.result=dice_count

    # 提取出轮数和掷骰原因
    def extract_roundnum_and_reason(self):

        expression=self.expression

        # 匹配正则
        match_result=re.search(r"(([0-9]+)#)?([dk0-9\.+\-*/\^\(\)]*)(.*)",expression)

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
            calculator.calculate_with_bracket()
            message+='\n'+calculator.source
            if is_show_detail:message+='='+calculator.detail
            message+='='+str(int(calculator.result))
        return message

# 调试用
if __name__=='__main__':
    while(True):
        print(WodCalculator(input()).extract_roundnum_and_reason())