
class Mission:

    def __init__(self):
        self._name = None
        self._description = None
        self._origin = None
        self._countries = None
        self._information = None
        self._date = None
        self._location = None
        self._duration = None
        self._status = None
        self._cargo = None
        self._job = None
        self._requirements = None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value

    @property
    def countries(self):
        return self._countries

    @countries.setter
    def countries(self, value):
        self._countries = value

    @property
    def information(self):
        return self._information

    @information.setter
    def information(self, value):
        self._information = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value

    @property
    def requirements(self):
        return self._requirements

    @requirements.setter
    def requirements(self, value):
        self._requirements = value

    def __repr__(self):
        return f'Name: {self._name}\t\t' \
               f'Origin: {self._origin}\t\t' \
               f'Information: {self._information}\t\t\n' \
               f'Date: {self._date}\t\t' \
               f'Location: {self._location}\t\t' \
               f'Duration: {self._duration}\t\t\n' \
               f'Status: {self._status}\t\t' \
               f'Cargo: {self._cargo}\t\t' \
               f'Job: {self._job}\t\t' \
               f'Requirements: {self._requirements}\t\t\n' \
               f'Description: {self._description}\n'

    @classmethod
    def from_input(cls) -> object:
        m = cls()
        m.name = input('Please enter name:')
        m.origin = input('Please enter origin:')
        m.information = input('Please enter information:')
        m.date = input('Please enter date:')
        m.location = input('Please enter location:')
        m.duration = input('Please enter duration:')
        m.status = input('Please enter status:')
        m.cargo = input('Please enter cargo:')
        m.job = input('Please enter job:')
        m.requirements = input('Please enter requirements:')
        m.description = input('Please enter description:')
        return m


if __name__ == '__main__':
    # for test
    mission = Mission()
    mission.name = 'Hello'
    mission.description = 'description'
    print(mission)
    print(mission.name)

    mission = Mission.from_input()
    print(mission)
