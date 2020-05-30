'''登陆系统
1、可以选择创建新的用户
2、可以登陆原有的用户
3、输入密码错误三次后用户则被锁定'''
from typing import List

flag = True  # 循环控制符


def createuser():
    f = open('userlist.txt', 'r')  # 打开已存在用户的文件，假设文件已经存在
    flag = True
    name = f.readlines()
    f.close()
    while flag:
        username = input('username:')
        flag2 = False  # 用户名已存在的标记符
        for line in name:
            if (username == line.split('*')[0]):
                flag2 = True
                print("username already exists, please enter a new one")
        if flag2 != True:
            f = open('userlist.txt', 'a')  # 创建新的用户
            f.write('\n' + username)
            f.write('*')
            password = input('password:')
            f.write(password)
            f.close()
            break
    main()


def login():  # 登入函数，输入密码错误三次则锁定用户
    count = 0  # 密码错误计数,3次则锁定
    f = open('userlist.txt', 'r')
    info: List[str] = f.readlines()
    f.close()
    user = None  # 重复用户标记符
    while flag:
        flag2 = False
        f2 = open('blocklist.txt', 'r')
        block_name = f2.readlines()
        f2.close()
        username = input('username:')
        if user == None:  # user没有使用过，则直接赋予输入的用户名
            user = username
        elif user != username:  # 如果下一次输入的用户名不一样，则记录上一次的用户名，同时计数清零
            user = username
            count = 0;
        for line in block_name:  # 检查用户名是否被锁定，锁定则返回主菜单
            if username == line.strip('\n'):
                print('The user account has been locked, please contact adminstrator')
                main()
        password = input('password:')
        for line in info:
            if (username == line.split('*')[0] and password == line.split('*')[1].strip('\n')):
                print('log in succeed')
                flag2 = True
        if flag2 == False:
            count += 1
            print("log in information incorrect, please reenter")
        if count == 3:  # 错误三次，把用户名添加到锁定列表中
            print('failed too many times, account has been locked')
            f3 = open('blocklist.txt', 'a')
            f3.write('\n' + username)
            f3.close()
            count = 0  # 加入黑名单后重置计数
            main()  # 加入黑名单后退回主菜单


info = '''
------请输入相关数字-----
1.创建新的用户
2.登陆已有用户
3.退出程序
'''


def main():
    print(info)
    while flag:
        i = input()
        if i == '1':
            createuser()
            break
        elif i == '2':
            login()
            break
        elif i == '3':
            exit()
        else:
            print("请输入正确的数字.")


main()  # 程序入口