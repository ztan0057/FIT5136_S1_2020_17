import sqlite3
import os


def clear():
    os.system('cls')


def start():
    conn = sqlite3.connect('marsdb.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user')
    result = c.fetchall()
    print('Welcome to Mission to Mars System!!')
    print('Login or register? 1---login as |2---register')
    if input() == '1':
        username = input('enter you user name:')
        pwd = input('enter your password:')
        clear()
        re = 'Fail, please check'
        for i in result:
            if username == i[1] and pwd == i[2]:
                logstate = True
                re = 'Success'
                return [True,i[3],i[4]]
        print(re)

    else:
        username = input('enter you user name:')
        pwd = input('enter your password:')
        c.execute("INSERT INTO user (username,password) VALUES(?,?)", (username, pwd))
        conn.commit()
        return False

