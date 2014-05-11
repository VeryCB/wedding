# coding: utf8

import string

from mario.config import DEBUG


ALPHABET_LIST = list(string.ascii_lowercase)
RESERVED_USER_NAMES = ALPHABET_LIST.extend([
    'verycb',

    # 防止假冒官方帐号
    'wanjia',
    '玩家',
    '官方号',
    '官方账号',
    '官方帐号',
    '玩家官方号',
    '玩家官方账号',
    '玩家官方账户',
    '玩家官方帐号',
    '玩家官方帐户',
])

if DEBUG:
    RESERVED_USER_NAMES = []
