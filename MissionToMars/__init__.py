from MissionToMars.login import login
from MissionToMars.mission_to_mars import main as mission


def check_selected(user):
    with open('selected.txt', 'r') as f:
        for line in f.readlines():
            if user.name in line:
                print("You have been chosen for a mission")
                with open('inform.txt', 'w') as file:
                    if input("Please choose 1.Accept or 2.Reject:") == '1':
                        file.write(user.name + ' Accepted')
                    else:
                        file.write(user.name + ' Declined')


def main():
    user = mission.User()
    while not user.login:
        state = login.start()
        user.login = state[0]
        user.name = state[1]
        user.type = state[2]
        check_selected(user)
        mission.main(user)


if __name__ == '__main__':
    main()

