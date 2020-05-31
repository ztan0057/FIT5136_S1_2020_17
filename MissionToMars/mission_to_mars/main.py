from models.user import User
from models.mission import Mission


class Controller:
    def load_missions(self, type='new'):
        # FIXME 从 txt 中加载
        missions = []
        if type == 'new':
            with open('./data/mission.txt') as f:
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
            with open('./data/mission_origin.txt') as f:
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
        with open('./data/mission.txt', 'w') as f:
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
        return user.type == 'Administrator' or user.type == 'Mission coordinator'

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
        # FIXME 状态机
        current = User()
        # main | mission task
        # main | login
        state = 'main'
        while True:
            missions = self.load_missions()
            if not current.login:
                print('Enter "login c" or "login a" or "login m" to login.')
            else:
                # 判断身份
                if self.can_enter_mission_list(current):
                    print('You can input \n'
                          '\t"y" to get mission list, \n'
                          '\t"u [name]" to update mission by name, \n'
                          '\t"c" to create mission, \n'
                          '\t"exit" to login off.')
                else:
                    print('You can input "exit" to login off.')
            user_input = input('Your input: ').lower()
            # FIXME 必须先登录，使用登录模块的逻辑，这里是为了保证当前模块正确
            if not current.login:
                current.login = True
                if user_input == 'login candidate':
                    current.type = 'Candidate'
                elif user_input == 'login adminstrator':
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
            elif self.can_enter_mission_list(current) and user_input == 'c':
                # 进入创建 mission
                m = Mission.from_input()
                missions.append(m)
                print('Mission created.')
                self.save_missions(missions)
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
            else:
                print('Wrong input, please input again.')


if __name__ == '__main__':
    controller = Controller()
    controller.start()
