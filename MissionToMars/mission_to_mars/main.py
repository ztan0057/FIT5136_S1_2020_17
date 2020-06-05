from MissionToMars.mission_to_mars.MissionToMars.user import User
from MissionToMars.mission_to_mars.MissionToMars.mission import Mission
from MissionToMars.Selection import selection
from MissionToMars.spaceShuttle import spaceshuttleinf as shuttle
from MissionToMars import Selection

class Controller:
    def __init__(self, user):
        self.user = user

    def load_missions(self, type='new'):
        # FIXME 从 txt 中加载
        missions = []
        if type == 'new':
            with open('mission_to_mars/data/mission.txt') as f:
                for line in f:
                    parts = line.strip().split('\t')
                    mission = Mission()
                    mission.name = parts[0]
                    mission.description = parts[1]
                    mission.origin = parts[2]
                    mission.countries = parts[3]
                    mission.information = parts[4]
                    mission.date = parts[5]
                    mission.location = parts[6]
                    mission.duration = parts[7]
                    mission.status = parts[8]
                    mission.cargo = parts[9]
                    mission.job = parts[10]
                    mission.requirements = parts[11]
                    missions.append(mission)
        else:
            with open('mission_to_mars/data/mission_origin.txt') as f:
                for line in f:
                    parts = line.strip().split('\t')
                    mission = Mission()
                    mission.name = parts[0]
                    mission.description = parts[5]
                    mission.origin = parts[2]
                    mission.countries = None
                    mission.information = None
                    mission.date = parts[1]
                    mission.location = None
                    mission.duration = parts[3]
                    mission.status = None
                    mission.cargo = parts[15]
                    mission.job = parts[6]
                    mission.requirements = parts[8]
                    missions.append(mission)
        return missions

    def save_missions(self, missions):
        # FIXME 保存到 txt 中
        with open('mission_to_mars/data/mission.txt', 'w') as f:
            for mission in missions:
                f.write(mission.name if mission.name else '')
                f.write('\t')
                f.write(mission.description if mission.description else '')
                f.write('\t')
                f.write(mission.origin if mission.origin else '')
                f.write('\t')
                f.write(mission.countries if mission.countries else '')
                f.write('\t')
                f.write(mission.information if mission.information else '')
                f.write('\t')
                f.write(mission.date if mission.date else '')
                f.write('\t')
                f.write(mission.location if mission.location else '')
                f.write('\t')
                f.write(mission.duration if mission.duration else '')
                f.write('\t')
                f.write(mission.status if mission.status else '')
                f.write('\t')
                f.write(mission.cargo if mission.cargo else '')
                f.write('\t')
                f.write(mission.job if mission.job else '')
                f.write('\t')
                f.write(mission.requirements if mission.requirements else '')
                f.write('\n')

    def can_enter_mission_list(self, user):
        return user.type == 'admin' or user.type == 'Mission coordinator'

    def find_mission_by_name(self, name, missions):
        mission = None
        for m in missions:
            if m.name == name:
                mission = m
        return mission

    def update_mission(self, old, new, missions):
        for i in range(len(missions)):
            if missions[i] == old:
                missions[i] = new

    def start(self):
        # self.save_missions(missions)
        # 登录之后的循环，要接入整个程序需要处理一下
        # 比如说，你框选的模块中不包含用户登录逻辑，所以这边我们暂时通过一个输入判断来确定是否是用户
        # FIXME 状态机
        current = self.user
        # main | mission task
        # main | login
        state = 'main'
        while True:
            missions = self.load_missions()
            if not current.login:
                print('Enter "login candidate" or "login administrator" or "login mission coordinator" to login.')
            else:
                # 判断身份
                if self.can_enter_mission_list(current):
                    print('You can input \n'
                          '\t"y" to get mission list, \n'
                          '\t"u [name]" to update mission by name, \n'
                          '\t"c" to create mission, \n'
                          '\t"cri" to create selection criteria, \n'
                          '\t"exit" to login off.')
                else:
                    print('You can input "exit" to login off.')
            user_input = input('Your input: ').lower()
            # FIXME 必须先登录，使用登录模块的逻辑，这里是为了保证当前模块正确
            if not current.login:
                current.login = True
                if user_input == 'login candidate':
                    current.type = 'candidate'
                elif user_input == 'login administrator':
                    current.type = 'Administrator'
                elif user_input == 'login mission coordinator':
                    current.type = 'Mission coordinator'
                else:
                    current.login = False
                    print('Wrong input, please input again.')
                continue
            if self.can_enter_mission_list(current) and user_input == 'y':
                print('Mission list:')
                for mission in missions:
                    print(mission)
            if self.can_enter_mission_list(current) and user_input == 'cri':
                input('Candidate Age:')
                input('years of exp:')
                input('health check:')
                Selection.main()
                pass
            elif self.can_enter_mission_list(current) and user_input == 'c':
                # 进入创建 mission
                m = Mission.from_input()
                missions.append(m)
                print('Mission created.')
                self.save_missions(missions)
                shuttle.main()
                pass
            elif self.can_enter_mission_list(current) and user_input.startswith('u '):
                # 进入更新 mission
                name = user_input[2:]
                m = self.find_mission_by_name(name, missions)
                if m is not None:
                    new_m = Mission.from_input()
                    self.update_mission(m, new_m, missions)
                    print(f'Mission {name} updated.')
                    self.save_missions(missions)
                else:
                    print(f'Not found mission {name}')
            elif user_input == 'exit':
                current.login = False
                print('login off.')
                break
            else:
                print('Wrong input, please input again.')


def main(user):
    controller = Controller(user)
    controller.start()


if __name__ == '__main__':
    main()
