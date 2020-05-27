import pandas as pd

def readfile(file_name): #读取candidate名单
    file = pd.read_excel(file_name)
    print(file)
    return file

def selection(candidate,n):
    u_name = candidate.iloc[n+1]["employee name"]
    print(u_name)
    return u_name

def writefile(file_name,u_name):
    file_handle = open(file_name, 'w')
    file_handle.write(u_name +'\n')
    file_handle.close()


def main():
    candidate = readfile('sample missionToMars data.xlsx')
    selection(candidate,2)


main()
# ed = pd.read_excel('sample missionToMars data.xlsx')
# print(ed)
# a = ed.iloc[3]["employee name"]
# print(a)
# print(ed.iloc[2,1])