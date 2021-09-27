#import libraries
import json
import random
import string
import datetime
import time
import sched
import ast
import os
from time import time, sleep
from generateSensorTypes import sensor_types


#initialize dictionnary for random sensor data for one unit
unit_data = {}

#declare variable unit_id and set it in dictionnary unit_data
unit_id= 1

unit_data["unit_id"] = unit_id

#Get date unix epoch
datetime_object = datetime.datetime.now()
dateUnixEpcoh = datetime_object.timestamp()
print(dateUnixEpcoh)

#Create directory for json files
os.mkdir("JsonOutputs")
for i in range (0,9):
  #create json file for unit
  fileName = str(sensor_types[i] )+ "_" + str(unit_id) + "_" + str(dateUnixEpcoh) + ".json"
  os.mknod("JsonOutputs/"+fileName)


#Loop every 60 seconds
while True:
  sleep(60 - time() % 60)

  #for each sensor in a unit, 10 sensors
  #Set dictionnary keys and assign value of variable to key
  #Use round to round decimal or whole number
  #Use random.unifrom() to get random number
  for i in range (0,9):
    #create json file for unit
    sensorFileName = str(sensor_types[i] )+ "_" + str(unit_id) + "_" + str(dateUnixEpcoh) + ".json"
    f = "JsonOutputs/"+sensorFileName

    unit_data["sensor_id"] = i

    #use one of the sensor types generated previously
    unit_data["sensor_type"] = sensor_types[i]
    unit_data["cistern_temperature"] = round(random.uniform(0, 100), 1)
    unit_data["ambient_temperature"] = round(random.uniform(0, 100), 1)
    unit_data["cistern_milk_weight"] = round(random.uniform(0, 9999), 0)
    unit_data["finish_product_weight"] = round(random.uniform(0, 9999), 0)
    unit_data["pH"] = round(random.uniform(-10, 10), 1)
    unit_data["kplus"] = round(random.uniform(0, 50), 0)
    unit_data["nacl"] = round(random.uniform(0, 10), 1)
    unit_data["salmonella_lvl"] = round(random.uniform(0, 50), 0)
    unit_data["ecoli_lvl"] = round(random.uniform(0, 50), 0)
    unit_data["listeria_lvl"] = round(random.uniform(0, 50), 0)
    print(unit_data)

    # Create Json object with dictionnary
    json_object = json.dumps(unit_data , indent = 4)

    with open(f, "r") as file:
      data = json.load(file)

    data.append(json_object)

    #open file previously created and add json
    with open(f, 'w') as outfile:
      json.dump(json_object, outfile)
      outfile.close()

  with open(sensorFileName) as json_file:
      data = json.load(json_file)
      if len(data) > 59 :
        del data[0]
