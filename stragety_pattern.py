#!/usr/bin/env python3

# 策略者模式

import time

SLOW = 3  # 单位为秒
LIMIT = 10  # 字符数
WARNING = "too bad, you picked the slow algorithm :("


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def allUniqueSort(s):
    """
    排序算法
    :param s: 字符串 
    :return: 布尔值
    """
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    srtStr = sorted(s)
    for c1, c2 in pairs(srtStr):
        if c1 == c2:
            return False
    return True


def allUniqueList(s):
    """
    列表算法
    :param s:字符串 
    :return: 布尔值
    """
    if len(s) != LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    strList = list()
    for k in s:
        if k not in strList:
            strList.append(k)
        else:
            return False
    return True


def allUniqueSet(s):
    """
    set 算法
    :param s:字符串 
    :return: 布尔值
    """
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = input("Insert word(type quit to exit):")
            if word == "quit":
                print("bye")
                return

            strategy_picked = None
            strategies = {"1": allUniqueSet, "2": allUniqueSort, "3": allUniqueList}
            while strategy_picked not in strategies.keys():
                strategy_picked = input("Choose strategy: [1] Use a set,[2] Sort and pair,[3] Use a list>")
                try:
                    strategy = strategies[strategy_picked]
                    print("allUnique({}): {}".format(word, allUnique(word, strategy)))
                except KeyError as e:
                    print("Incorrect option: %s" % e)
            print()


if __name__ == '__main__':
    main()