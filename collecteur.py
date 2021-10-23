import json
import socket
import threading
from SensorData import SensorData
import mysql.connector

HEADER = 64
PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# TODO Terminate insertSensorData method
# TODO Créer le script sql
def dbConnect():
    jsonFile = open("config.json", "r")
    config = json.loads(jsonFile.read())
    conn = mysql.connector.connect(
        host=config["HOST"],
        user=config["USER"],
        password=config["PASSWORD"],
        database=config["DATABASE"],
    )
    if conn.is_connected():
        print(f"[DATABASE - {conn.database}] : connection established...")
        jsonFile.close()
        return conn
    else:
        print("Fail to connect at the db")

def insertSensorData(dbConnect, sensorData: SensorData):
    sql = """INSERT INTO SensorData (
        id, 
        unit_id, 
        sensor_id, 
        sensor_type, 
        cistern_temperature, 
        ambient_temperature, 
        cistern_milk_weight, 
        finish_product_weight, 
        pH, 
        kplus, 
        nacl, 
        salmonella_lvl, 
        ecoli_lvl, 
        listeria_lvl,
        send_date,
        check_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    val = (
        None,
        sensorData.unit_id,
        sensorData.sensor_id,
        sensorData.sensor_type,
        sensorData.cistern_temperature,
        sensorData.ambient_temperature,
        sensorData.cistern_milk_weight,
        sensorData.finish_product_weight,
        sensorData.pH,
        sensorData.kplus,
        sensorData.nacl,
        sensorData.salmonella_lvl,
        sensorData.ecoli_lvl,
        sensorData.listeria_lvl,
        sensorData.check_date,
        sensorData.send_date
    )
    cursor = dbConnect.cursor()
    cursor.execute(sql, val)
    dbConnect.commit()
    dbConnect.close()
    
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr} {msg}]")
            conn.send("Msg received".encode(FORMAT))
            sensorData = SensorData()
            sensorData.build(msg)
            insertSensorData(dbConnect(), sensorData)
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

# Run Script
print("[STARTING] server is starting...")

""" testSensorData = SensorData()
testSensorData.unit_id = 1
testSensorData.sensor_id = 1
testSensorData.sensor_type = 1
testSensorData.cistern_temperature = 1
testSensorData.ambient_temperature = 1
testSensorData.cistern_milk_weight = 1
testSensorData.finish_product_weight = 1
testSensorData.pH = 1
testSensorData.kplus = 1
testSensorData.nacl = 1
testSensorData.salmonella_lvl = 1
testSensorData.ecoli_lvl = 1
testSensorData.listeria_lvl = 1
testSensorData.check_date = "2021-10-23"
testSensorData.send_date = "2021-10-23"
insertSensorData(dbConnect(), testSensorData) """
start()


