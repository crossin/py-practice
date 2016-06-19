# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import random
import string


STATE_MAP = {}
# 记录所有可能状态的状态表
PREF_LEN = 3
# 前缀长度，越大则生成单词越“逼真”，同时开销也更大
BEGIN_PERF = ('%',) * PREF_LEN
# 初始前缀
END_WORD = '$'
# 结束符，遇到结束符则马氏链终止


def add(pref, suf):
    # 将一个状态加入状态表中，如果已经存在则计数+1
    suffixs = STATE_MAP.setdefault(pref, {})
    suffixs.setdefault(suf, 0)
    suffixs[suf] += 1


def pick_up(pref):
    # 从给定的状态，随机挑选下一个状态
    # 也不是完全随机，而是根据状态出现频率挑选，这样显得真实
    nmatch = 0
    suf = ''
    assert(STATE_MAP.get(pref, None) is not None)
    for k, v in STATE_MAP.get(pref).items():
        # 这是经典的'one pass choice'算法
        nmatch += v
        if random.randint(0, nmatch - 1) < v:
            suf = k
    return suf


def build_word(file_name):
    # 以给定的输入文件，训练出马尔可夫链，文件越大，效果自然越好
    with open(file_name) as f_in:
        for line in f_in:
            words = [x for x in line.split() if x.islower()]
            # 只考虑小写字母单词
            pref = BEGIN_PERF
            words.append(END_WORD)
            for word in words:
                if len(word) < PREF_LEN:
                    continue
                    # 单词长度还不到前缀长度，丢弃
                word = word.lower()
                if not word.isalpha():
                    continue
                for i in range(len(word)):
                    # 依次加入状态表中，并更新前缀
                    add(pref, word[i])
                    pref = pref[1:] + (word[i],)
                add(pref,'$')
                # 别忘了把最后这个也加进去！


def generate():
    pref = BEGIN_PERF
    ans = []
    pos_rand = int(random.gauss(5, 3))
    # 采用高斯分布的随机数，分布更真实些
    if pos_rand < 0:
        pos_rand = 0
    for i in range(pos_rand + 3):
        # 这里其实只限定了单词的最大长度，避免马尔可夫过程不终止
        next_word = pick_up(pref)
        if next_word == END_WORD:
            # 如果已经达到停止状态，则退出
            break
        ans.append(next_word)
        # 随机漫步，并记录状态转移过程，作为输出
        pref = pref[1:] + (next_word,)

    return ans


if __name__ == '__main__':
    build_word('data.txt')
    print(''.join(generate()))
