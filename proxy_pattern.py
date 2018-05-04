#!/usr/bin/python3

# 代理模式


class SensitiveInfo():
    def __init__(self):
        self.users = ["jack", "tom", "Halun", "liha"]

    def read(self):
        user = ",".join(self.users)
        return "\nThere are {} users:{}\n".format(len(self.users), user)

    def add(self, super_secret):
        secret = input("请输入验证密码:")
        if secret != super_secret:
            print("验证密码不正确")
            return
        user = input("请输入添加用户名:")
        self.users.append(user)
        print("finish add {}".format(user))

    def del_user(self, super_secret):
        secret = input("请输入验证密码:")
        if secret != super_secret:
            print("验证密码不准确")
            return
        user = input("请输入删除用户名:")
        try:
            self.users.remove(user)
        except ValueError as e:
            print("用户列表中没有该用户!")
            return


class Info:
    def __init__(self, secret="0xaddsecret"):
        self.sencitive = SensitiveInfo()
        self.secret = secret

    def read(self):
        print(self.sencitive.read())

    def add(self):
        self.sencitive.add(self.secret)

    def del_user(self):
        self.sencitive.del_user(self.secret)


def main():
    info = Info()
    while True:
        print("1. read all name, 2. add user, 3. del user, 4. exit")
        ch_type = input()
        if ch_type == "1":
            info.read()
        elif ch_type == "2":
            info.add()
        elif ch_type == "3":
            info.del_user()
        elif ch_type == "4":
            exit()
        else:
            print("error type")


if __name__ == "__main__":
    main()
