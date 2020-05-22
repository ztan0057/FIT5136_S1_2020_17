import sqlite3
import os


def clear():
    os.system('cls')


def checkLogin(userNames, psw):
    re = 'Fail, please check'
    for i in result:
        if userNames == i[1] and psw == i[2]:
            os.system('clear')
            re = 'Success'
    return re


conn = sqlite3.connect('../marsdb.db')
c = conn.cursor()
c.execute('SELECT * FROM user')
result = c.fetchall()
print(result)
print('Welcome to Mission to Mars System!!')
username = input('enter you user name:')
pwd = input('enter your password:')
clear()
print(checkLogin(username, pwd))
conn.close()