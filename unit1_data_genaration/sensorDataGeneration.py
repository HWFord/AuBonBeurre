import json
import time
import sched
from classes.Unit import Unit
from classes.SensorData import SensorData 

s = sched.scheduler(time.time, time.sleep)

def main():
    print("Main function")

    #load conf file for unit IDs and sensor IDs
    confFile = open('conf.json')
    confFileData = json.load(confFile)

    #Get unit ID and set
    unit = Unit()
    unit.set_unit_id = confFileData['unit_id']

    #for 0 to 10 create sensorData using class
    for i in range (0, 9):
        sensorData = SensorData(i, confFileData['sensors'][i+1]["type"], unit.get_unit_id())
        json_object = json.dumps(sensorData.__dict__)

        #Create file with specific name
        fileName = str(sensorData.get_sensor_type())+ "_" + str(unit.get_unit_id()) + "_" + str(time.time()) + ".json"
        with open('JsonOutputs/'+fileName, 'w') as f:
            f.write(json_object)
    s.enter(60, 1, main)
          
if __name__ == "__main__":
    main()

s.enter(60, 1, main)
s.run()
