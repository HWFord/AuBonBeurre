import socket
import json

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "localhost"
ADDR = (SERVER, PORT)

sensor_data = {
    "unit_id": 1,
    "sensor_id": 1,
    "sensor_type": 0X0000BA20,
    "cistern_temperature": 1,
    "ambient_temperature": 1,
    "cistern_milk_weight": 1,
    "finish_product_weight": 1,
    "pH": 1,
    "kplus": 1,
    "nacl": 1,
    "salmonella_lvl": 1,
    "ecoli_lvl": 1,
    "listeria_lvl": 1,
    "check_date": 1,
    "send_date": 1
}

output_data = json.dumps(sensor_data)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send(output_data)
send(DISCONNECT_MSG)
