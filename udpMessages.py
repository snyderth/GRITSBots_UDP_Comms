import socket
import GRITSBOT_MESSAGES as messenger
import json


UDP_IP="0.0.0.0"

#GRITSBots listen on this port, computer sends
UDP_PORT_OUT = 4998
#GRITSBots send on this port, computer listens
UDP_PORT_IN = 4999


#Setup socket for UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT_IN))
while True:
    #Listen to GRITSBots messages infinitely
    data, addr = sock.recvfrom(256)
    # f.write(data.decode('UTF-8'))
    data = data.decode("UTF-8")
    data = data[:-1] #remove extra weird trailing bit at the end
    obj = json.loads(data)
    if 'msgType' in obj.keys():
        if obj['msgType'] == "91" or obj['msgType'] == "90":
            print(json.dumps(obj, indent=4, sort_keys=True))
    if 'First num' in obj.keys():
        print(json.dumps(obj,indent=4,sort_keys=True))
