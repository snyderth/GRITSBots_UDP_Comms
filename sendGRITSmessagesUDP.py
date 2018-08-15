import socket
import struct
import GRITSBOT_MESSAGES as messenger
import json


#Function to send a message
def send_message(sock, out, message):
    #create dict
    msg = {}
    msg['msgType'] = message
    #Convert dict to json
    msg = json.dumps(msg)
    for i in range(0,10):
        #send message, this ip is the "All UDP addresses" ip
        sock.sendto(msg.encode(), ("224.0.0.1",out))



# f = open("json.txt", "w+")
UDP_IP="192.168.1.117"#used only when sending to specific bot
UDP_PORT_OUT = 4998#send on this port
UDP_PORT_IN = 4999#listen on this port


#
#
# print (MESSAGE)
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#Setup port for UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICASE_TTL, 20)

#How you send a message
send_message(sock, UDP_PORT_OUT, messenger.MSG_UPDATE_FIRMWARE)
print("Messages Transmitted")


