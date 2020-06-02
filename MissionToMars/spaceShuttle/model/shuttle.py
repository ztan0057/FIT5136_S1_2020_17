class Shuttle:
    def __init__(self):
        self._shuttle_id = None
        self._name = None
        self._manufacture_year = None
        self._fuel_capacity = None
        self._passenger_capacity = None
        self._cargo_capacity = None
        self._travel_speed = None
        self._origin = None

    @property
    def shuttle_id(self):
        return self._shuttle_id

    @shuttle_id.setter
    def shuttle_id(self, value):
        self._shuttle_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def manufacture_year(self):
        return self._manufacture_year

    @manufacture_year.setter
    def manufacture_year(self, value):
        self._manufacture_year = value

    @property
    def fuel_capacity(self):
        return self._fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, value):
        self._fuel_capacity = value

    @property
    def passenger_capacity(self):
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value):
        self._passenger_capacity = value

    @property
    def cargo_capacity(self):
        return self._cargo_capacity

    @cargo_capacity.setter
    def cargo_capacity(self, value):
        self._cargo_capacity = value

    @property
    def travel_speed(self):
        return self._travel_speed

    @travel_speed.setter
    def travel_speed(self, value):
        self._travel_speed = value

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value
