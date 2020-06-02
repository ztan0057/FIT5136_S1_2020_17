from datetime import datetime
from model.shuttle import Shuttle
import csv


class ShuttleDataLoader:
    def __init__(self):
        self._shuttle_dict = {}  # dict of shuttle data indexed by IDs

    def load_from_csv(self, path):
        # Clear existing data
        self._shuttle_dict = {}

        with open(path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                shuttle = Shuttle()

                shuttle.shuttle_id = int(row['shuttle_id'])
                shuttle.name = row['name']
                shuttle.manufacture_year = datetime.strptime(row['manufacture_year'], '%m/%d/%Y')
                shuttle.fuel_capacity = float(row['fuel_capacity'])
                shuttle.passenger_capacity = int(row['passenger_capacity'])
                shuttle.cargo_capacity = float(row['cargo_capacity'])
                shuttle.travel_speed = float(row['travel_speed'])
                shuttle.origin = row['origin']

                self._shuttle_dict[shuttle.shuttle_id] = shuttle

    def get_shuttle_list(self):
        return self._shuttle_dict.values()

    def get_shuttle_by_id(self, shuttle_id):
        return self._shuttle_dict[shuttle_id]

