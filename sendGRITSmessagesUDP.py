import socket
import struct
import GRITSBOT_MESSAGES as messenger
import json



def send_message(sock, out, message):
    msg = {}
    msg['msgType'] = message
    msg = json.dumps(msg)
    for i in range(0,10):
        sock.sendto(msg.encode(), ("224.0.0.1",out))



# f = open("json.txt", "w+")
UDP_IP="192.168.1.117"
UDP_PORT_OUT = 4998
UDP_PORT_IN = 4999


#
#
# print (MESSAGE)
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICASE_TTL, 20)

# send_message(sock, UDP_PORT_OUT, messenger.MSG_STOP_ALL_ROBOTS)
send_message(sock, UDP_PORT_OUT, messenger.MSG_UPDATE_FIRMWARE)
print("Messages Transmitted")





# sock.bind((UDP_IP, UDP_PORT_IN))
# while True:
#     data, addr = sock.recvfrom(256)
#     # f.write(data.decode('UTF-8'))
#     data = data.decode("UTF-8")
#     data = data[:-1] #remove extra weird trailing bit at the end
#     obj = json.loads(data)
#     if 'msgType' in obj.keys():
#         if obj['msgType'] == "91" or obj['msgType'] == "90":
#             print(json.dumps(obj, indent=4, sort_keys=True))
#     if 'First num' in obj.keys():
#         print(json.dumps(obj,indent=4,sort_keys=True))
