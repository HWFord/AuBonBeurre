import json
import time
import sched
from classes.Unit import Unit
from classes.SensorData import SensorData 
import datetime

s = sched.scheduler(time.time, time.sleep)
confFileData = []

def main():
    print("Main function")
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

    #load conf file for unit IDs and sensor IDs
    confFile = 'conf.json'

    with open(confFile, 'r') as j:
        confFileData = json.loads(j.read())
        j.close()

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

s.run()
