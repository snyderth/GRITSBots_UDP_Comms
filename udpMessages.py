import socket
import GRITSBOT_MESSAGES as messenger
import json


# f = open("json.txt", "w+")
UDP_IP="0.0.0.0"
UDP_PORT_OUT = 4998
UDP_PORT_IN = 4999
MESSAGE={"msgType":str(messenger.MSG_UPDATE_FIRMWARE)}
#
#
# print (MESSAGE)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.sendto(MESSAGE.encode(), (UDP_IP,UDP_PORT_OUT))
sock.bind((UDP_IP, UDP_PORT_IN))
while True:
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
