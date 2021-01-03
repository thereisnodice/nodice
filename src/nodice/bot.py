from os import path

import nonebot

import bot_config

if __name__ == '__main__':
    nonebot.init(bot_config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'plugins'),
        'plugins'
    )
    nonebot.run()
