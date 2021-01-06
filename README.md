<div align="center">
	<img width="128" src="docs/nodice.png" alt="logo"></br>

# NoDice

*基于[ nonebot ](https://github.com/nonebot/nonebot)以及[ go-cqhttp ](https://github.com/Mrs4s/go-cqhttp)的轻量化QQ跑团掷骰机器人*

~~然而会有一些奇奇怪怪的扩展功能~~

[![License](https://img.shields.io/github/license/thereisnodice/nodice)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![OneBot Version](https://img.shields.io/badge/OneBot-v11-black)

</div>

### Features

- [x] Git热更新 `.bot update` （容易造成文件损坏）
- [x] 重载插件 `.bot reload`
- [x] 标准掷骰 `.r(h) 4#3d6k2 reason`
- [x] 天气查询 `.weather` （目前NLP有bug）
- [ ] 在线IDE `.exec python`
- [ ] Github Webhook 推送
- [x] 原Dice! 的牌堆功能 `.draw 牌堆`
- [ ] 各音乐平台点歌
- [ ] 机器人分群管理
- [x] 人物作成 `.sg/sk` （COC、DND待添加）
- [ ] COC检定与奖惩骰
- [ ] 今日人品
- [ ] 使用说明 `.help`
- [ ] 数据库（与其他插件对接）
- [x] CSU课表查询 `.csu`（此功能不开源）

- 理论上来说 `plugin` 文件夹里的所有插件都可以在 nonebot 框架的机器人上面即插即用。

### TO DO List

- 通过松藕合的dice_caculator函数重构人物作成
- 牌堆类json语言实现
- 链接sqlite3数据库
- csu_class可视化
- 接入数据库的群管功能

### Bugs

- 出现了个奇怪的问题，当我把bot重命名为bot_control之后，通过bot update命令让挂载在服务器的机器人进行更新后，bot插件明明加载了却无法对我的指令响应，此bug待研究，先记着。

### Lisence

go-cqhttp下的文件 ([go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的可执行程序) 保持使用原 [AGPL-3.0 License](https://github.com/Mrs4s/go-cqhttp/blob/master/LICENSE) 许可

项目中其余内容使用 [MIT License](LICENSE)

~~是的，目前除了 Logo 和简介以及 TO DO List 还有 Lisence 外什么也没有。~~