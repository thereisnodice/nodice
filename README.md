<div align="center">
	<img width="128" src="docs/nodice.png" alt="logo"></br>

# NoDice

*基于[ nonebot ](https://github.com/nonebot/nonebot)以及[ go-cqhttp ](https://github.com/Mrs4s/go-cqhttp)的轻量化QQ跑团掷骰机器人*

~~然而会有一些奇奇怪怪的扩展功能~~

[![License](https://img.shields.io/github/license/thereisnodice/nodice)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![NoneBot Version](https://img.shields.io/badge/nonebot-1+-red.svg)
![OneBot Version](https://img.shields.io/badge/OneBot-v11-black)

</div>

### Features

*理论上来说 `plugin` 文件夹里的所有插件都可以在 nonebot 基础框架的机器人上面即插即用，但是由于大多数 nonebot 机器人（如 HoshinoBot ）已经被二次封装，所以请不要对于这项特性抱有太大希望。*

*由于对松耦合的执着，我把原先作为一个整体的 Dice! 拆散成了多个插件并且复用了多个与 nonebot 框架**完全松耦合**的脚本，所以你很有可能在多个插件目录下都见到同样的文件，例如 `roll_dice`、`draw_deck`、`char_make` 里面都有 `calculator.py` ~~（以后可能还会有更多的插件包含这个东西）~~，请不要对此感到疑惑。*

#### Dice! 功能复刻

- [x] 帮助文档 `.help`
- [x] 规则速查 `.rules`
  
##### 娱乐功能

- [x] 今日人品 `.jrrp`
- [ ] 第三人称动作 `.me`

##### 机器人管理模块

- [ ] 发送消息 `.send`
- [ ] 骰主绑定 `.master`
- [ ] 全局管理 `.admin`
- [ ] 自定义帮助词条 `.helpdoc`
- [ ] 自定义回执文本 `.str`

##### 掷骰模块（核心）

- [x] 标准掷骰 `.r(h) 4#3d6k2+5 reason`
- [ ] 设置默认骰 `.set`
- [x] COC 检定 `.ra(h)`
- [ ] COC 房规 `.setcoc`
- [ ] DND 先攻 `.ri`
- [ ] 先攻列表 `.init`
- [x] FATE 掷骰 `.rf(h) reason`
- [x] WOD 骰池 `.w(h) 5a10 reason`
- [x] COC 理智检定 `.sc`
- [x] COC 成长检定 `.en`
- [ ] COC 奖惩骰 `.rb/p`

##### 牌堆模块

- [x] 拓展牌堆 `.draw` 
- [ ] 分群牌堆 `.deck`
- [x] 疯狂症状 `.ti/li`
- [x] 随机姓名 `.name`

##### 人物模块

- [x] 人物作成 `.coc/dnd`
- [ ] 角色卡 `.pc`
- [ ] 角色卡设置 `.pc`
- [ ] 设置昵称 `.nn(n)`

##### 群管模块

- [ ] 骰子开关 `.bot on/off`
- [x] 退群指令  `.dismiss`
- [ ] 欢迎词 `.welcome`
- [ ] 群管理操作 `.group`
- [ ] 跑团记录 `.log`
- [ ] 旁观者模式 `.ob`

#### 拓展功能

- [x] Git热更新 `.admin update`
- [x] 重载插件 `.admin reload`
- [x] 天气查询 `.weather` （目前NLP有bug）
- [x] 在线IDE `.exec python`
- [ ] Github Webhook 推送
- [ ] 各音乐平台点歌

### Developer

[开发文档](./docs/DEVELOPER.md)

### Lisence

go-cqhttp下的文件 ([go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的可执行程序) 保持使用原 [AGPL-3.0 License](https://github.com/Mrs4s/go-cqhttp/blob/master/LICENSE) 许可

项目中其余内容使用 [MIT License](LICENSE)

### Thanks

- @w4123 溯洄，Dice! 的主要开发者与 Dice3 的开发者，本项目命令格式大部分借鉴自其。
- @mystringEmpty Dice! 的另一名主要开发者。
- @233a344a455 DeltaBot的开发者，本项目的 bot_control 插件修改自其。

### Nothing useful

本项目旨在用 python 移植 CQ原生插件 Dice! ~~（虽然本项目的架构更像是 Dice3）~~。

之所以取名 NoDice ，是因为一开始只是想要把 Dice的感叹号移到前面来，也就是 NotDice ，刚好可以把组织名取作 `this is not dice` 来玩双关。接着因为本项目基于 nonebot 框架，就想取个相近的名字，而 not 和none 就只有 no 这两个字相同了，组织名刚好也能玩双关，只是意思从“这不是骰子”变成了“这里没有骰子”~~（当然我更喜欢翻译为无骰骑士异闻录）~~。