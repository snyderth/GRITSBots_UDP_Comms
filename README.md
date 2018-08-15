# GRITSBot Wifi Communications

A library to communicate wirelessly with the UGVs in the Oregon State HMT lab

## udpMessages

A script that listens for an messages sent over UDP on the wifi. The GRITSbot firmware must be compiled with the broadcast IP set as the IP of the receiving computer (See the [GRITSBot firmware](https://github.com/snyderth/GRITSBots_firmware) and look at GRITSBot_WIFIConfig/WIFIConfig.h)

## GRITSBOTS_MESSAGES

A reference for all GRITSBots codes. There is a C version in the GRITSBots firmware/GRITSBot_Messages

## SendGRITSMessagesUDP

A script to send messages to all GRITSBots currently running on the network. 
