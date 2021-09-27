#import libraries
import json
import random
import string


#Create 10 sensor type names
#Initialize dictionnary for 10 random sensor types.
sensor_types = {}

#For sensor number set length of string
sensorStringLength = 10

#Generate 10 different sensor type codes
for j in range (0, 10):
  #Use random.choices() string module to find the string in Uppercase + numeric data.
  ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = sensorStringLength))
  sensor_types[j] = str(ran)
  print(str(ran))

print(sensor_types)

# write json file with sensor types
#with open("sensors.json", "r+") as file:
#    data = json.load(file)
#    data.update(unit_data)
#    file.seek(0)
#    json.dump(data, file)