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

    def build(self, obj):
        obj = json.dumps(obj)
        self.unit_id = obj.unit_id
        self.sensor_id = obj.unit_id
        self.sensor_type = obj.unit_id
        self.cistern_temperature = obj.unit_id
        self.ambient_temperature = obj.unit_id
        self.cistern_milk_weight = obj.unit_id
        self.finish_product_weight = obj.unit_id
        self.pH = obj.unit_id
        self.kplus = obj.unit_id
        self.nacl = obj.unit_id
        self.salmonella_lvl = obj.unit_id
        self.ecoli_lvl = obj.unit_id
        self.listeria_lvl = obj.unit_id
        self.check_date = obj.unit_id
        self.send_date = obj.unit_id
