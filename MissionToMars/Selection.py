import pandas as pd

n = 0


def read_from_file(file_name):
    file = open(file_name, 'r')
    name = file.readlines()
    file.close()
    return name


def readexcel(file_name):  # get candidate list, its depend on what type of file we used to store list
    excel = pd.read_excel(file_name)
    print(excel)
    return excel


def selection(candidate):  # use number to choose candidate
    print("please choose candidate")
    n = input()
    n = int(n)
    u_name = candidate.iloc[n]["employee name"]
    print(u_name)
    return u_name


def writefile(file_name, name='', x='w'):
    file_handle = open(file_name, x)
    file_handle.write(name + '\n')
    file_handle.close()


def a_or_r(selected_name):  # accept or reject
    global n
    n = 0
    i = 0
    while i < len(selected_name):  # check whether the candidat has been choosen
        if selected_name(i) == user_name:
            print("You have been choosen for a mission")
            print("Please choose 1.Accept or 2.Reject")
            n = int(input())


def createcandidate(missionname):
    f = missionname + '.txt'
    file = open(f, 'w')
    file.close()
    return f


def main():
    global n
    candidate = readexcel('sample missionToMars data.xlsx')
    # f = createcandidate(missionname) #creat a txt for this mission to store candidate's name
    # writefile(f, c_name,'a')# store the name for each mission
    c_name = selection(candidate)
    writefile('selected.txt', c_name, 'a')  # use to store the name who was selected
    # if user_type == "candidate"
    #     a = read_from_file('selected.txt')
    #     a_or_r(a)
    #     if n == 1:
    #         writefile('inform.txt', user_name,'a')
    #         writefile('inform.txt', "Accept",'a')
    #     elif n ==2:
    #         writefile('inform.txt', user_name,'a')
    #         writefile('inform.txt',"Reject")

    # receive = read_from_file('inform.txt') # If administratro want to know who accept or reject, also can creat a function to print
    # print(receive)
    # writefile('inform')#clear the file

if __name__ == '__main__':
    main()