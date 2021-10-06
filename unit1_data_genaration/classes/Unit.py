import json

with open('conf.json') as data:
    unitData = json.load(data)

unit_id = unitData["unit_id"]

class Unit:
    'Unit class with id'

    def __init__(self):
        self.unit_id = unit_id

    def get_unit_id(self):
        return self.unit_id

    def set_unit_id(self, x):
        self.unit_id = x
