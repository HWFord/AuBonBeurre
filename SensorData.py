import json

class SensorData():
    def __init__(self):
        self.unit_id = None
        self.sensor_id = None
        self.sensor_type = None
        self.cistern_temperature = None
        self.ambient_temperature = None
        self.cistern_milk_weight = None
        self.finish_product_weight = None
        self.pH = None
        self.kplus = None
        self.nacl = None
        self.salmonella_lvl = None
        self.ecoli_lvl = None
        self.listeria_lvl = None
        self.check_date = None
        self.send_date = None

    def build(self, jsonData):
        self.unit_id = jsonData["unit_id"]
        self.sensor_id = jsonData['sensor_id']
        self.sensor_type = jsonData['sensor_type']
        self.cistern_temperature = jsonData['cistern_temperature']
        self.ambient_temperature = jsonData['ambient_temperature']
        self.cistern_milk_weight = jsonData['cistern_milk_weight']
        self.finish_product_weight = jsonData['finish_product_weight']
        self.pH = jsonData['pH']
        self.kplus = jsonData['kplus']
        self.nacl = jsonData['nacl']
        self.salmonella_lvl = jsonData['salmonella_lvl']
        self.ecoli_lvl = jsonData['ecoli_lvl']
        self.listeria_lvl = jsonData['listeria_lvl']
        self.check_date = jsonData['check_date']
        self.send_date = jsonData['send_date']
