#!/usr/bin/env python3

# 解释器模式

class Publisher:
    """
    发布者类
    属性：订阅者列表
    方法：添加(订阅者)，移除(订阅者)，通告(通告所有订阅者列表中的订阅者)
    """

    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print("Faild to add %s" % observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError as e:
            print("Faild to remove %s" % observer)

    def notify(self):
        [i.notify(self) for i in self.observers]


class DefaultFormatter(Publisher):
    """
    默认格式化类
    属性：名字，数据
    方法：输出
    """

    def __init__(self, name):
        super(DefaultFormatter, self).__init__()
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: {} has data = {}".format(type(self).__name__, self.name, self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        try:
            self._data = int(new_data)
        except ValueError as e:
            print("Error: %s" % e)
        self.notify()


class HexFormatter:
    def notify(self, publisher):
        print("{}: {} has new hex data = {}".format(type(self).__name__, publisher.name, hex(publisher.data)))


class BinarryFormatter:
    def notify(self, publisher):
        print("{}: {} has new bin data = {}".format(type(self).__name__, publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter("test1")
    print(df)

    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinarryFormatter()
    df.add(bf)
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.data = 40
    print(df)

    print()
    df.data = "hello"
    print(bf)

    print()
    df.data = 15.8
    print(df)


if __name__ == '__main__':
    main()
