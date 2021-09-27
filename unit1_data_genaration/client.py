import socket
hote = ""
port = ""

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote,port))
print "Connection on {}".format(port)

socket send("unit data")

print "Close"
socket.close()
