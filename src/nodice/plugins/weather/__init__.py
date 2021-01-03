from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
from .data_source import *

__plugin_name__ = '天气'
__plugin_usage__ = (
    '用法：\n'
    '对我说 “天气 长沙” 获取天气简要\n'
    '“天气 长沙 详细” 获取当前天气的详细报告'
)

@on_command('weather', aliases=('天气', '天气预报', '查天气'),only_to_me=False)
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查询哪个城市的天气呢？',at_sender=True)
    is_detailed=session.state.get('is_detailed')
    func = get_weather_desc if is_detailed else get_weather_short
    weather_report = await func(city)
    await session.send(weather_report)

@weather.args_parser
async def _(session: CommandSession):
    args = session.current_arg_text.strip().split(' ', 1)

    if session.is_first_run:
        if args[0]:
            session.state['city'] = args[0]
        return
    if not args[0]:
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = args[0]

# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    # 对消息进行分词和词性标注
    words = posseg.lcut(stripped_msg)

    args={}

    # 遍历 posseg.lcut 返回的列表
    for word in words:
        # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
        if word.flag == 'ns': # ns 表示该词为地名
            args['city'] = word.word
        elif word.word in ('详细', '报告', '详情'):
            args['is_detailed'] = True

    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'weather', args=args)
