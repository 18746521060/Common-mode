#!/usr/bin/python3

# MVC pattern

"""
解释：展示并加入名言
    1. model: 获取一条名言，如果获取失败，直接报错
    2. view: 显示名言，方法有显示指定一条名言或者所有名言和随机显示一条名言
    3. controller: 控制用户选择是显示或者添加或者删除等操作
"""
import random

quotes = ["A man is not complete until he is married. Then he is finished.",
          "As I said before, I never repeat myself.",
          "Black holes really such...",
          "Factsare stubborn things."]

pop_quotes = []

add_secret = "0xthisistheaddquote"
del_secret = "0xthisisthedelquote"


def _add_ok(quote):
    quotes.append(quote)
    print("add ok!")


def _del_ok(index):
    pop_quotes.append(quotes.pop(index))
    print("del ok!")


class Model:
    def get_model(self, index):
        try:
            quote = quotes[index]
        except IndexError as e:
            quote = "the {} index is invalid".format(index)
        return quote

    def get_lens(self):
        return len(quotes)

    def get_all(self):
        return quotes

    def add_one(self, add_s, quote):
        _add_ok(quote) if add_s == add_secret else print("添加失败:验证未通过!")

    def del_one(self, del_s, index):
        index = int(index)
        assert isinstance(index, int), "索引必须为正整数!"
        _del_ok(index) if del_s == del_secret else print("删除失败:验证未通过!")


class Views:
    def __init__(self):
        self.model = Model()

    def show_random_one(self):
        index = random.randint(0, self.model.get_lens()-1)
        return self.model.get_model(index)

    def show_select_one(self, index):
        index = int(index)
        return self.model.get_model(index)

    def show_all(self):
        return "\n".join(self.model.get_all())


class Controller:
    def __init__(self):
        self.view = Views()
        self.model = Model()

    def start(self):
        con_type = input("Select the type you need(a:add quote,s:select one quote,d:del quote,r:random,all:show all):")
        if con_type == "a":
            add_s = input("请输入添加权限码:")
            quote = input("请输入添加的名言:")
            self.model.add_one(add_s, quote)
        elif con_type == "s":
            index = input("请输入要查看名言的索引:")
            print(self.view.show_select_one(index))
        elif con_type == "r":
            print(self.view.show_random_one())
        elif con_type == "all":
            print(self.view.show_all())
        elif con_type == "d":
            del_s = input("请输入删除权限码:")
            index = input("请输入名言索引:")
            self.model.del_one(del_s, index)
        elif con_type == "exit":
            exit()
        else:
            print("无效指令!")


def main():
    control = Controller()
    while True:
        control.start()


if __name__ == "__main__":
    main()
