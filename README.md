# GRITSBot Wifi Communications

A library to communicate wirelessly with the UGVs in the Oregon State HMT lab

## udpMessages

A script that listens for an messages sent over UDP on the wifi. The GRITSbot firmware must be compiled with the broadcast IP set as the IP of the receiving computer (See the [GRITSBot firmware](https://github.com/snyderth/GRITSBots_firmware) and look at GRITSBot_WIFIConfig/WIFIConfig.h)

## GRITSBOTS_MESSAGES

A reference for all GRITSBots codes. There is a C version in the GRITSBots firmware/GRITSBot_Messages

## SendGRITSMessagesUDP

A script to send messages to all GRITSBots currently running on the network. This is able to send the OTA update message.

## Upload_to_pi

A script to upload the newfirmware.bin to the raspberry pi's http server. 

## Arduino folder structure

```
Arduino
|_basic_firmware
|	|_basic_firmware.ino (seperately saved, unnecssary)
|_GRITSBOT_MESSAGES.py
|_sendGRITSmessagesUDP.py
|_udpMessages.py
|_upload_to_pi.sh (references the basic_firmware folder in this directory)
|_libraries (Arduino default library folder)
	|_Adafruit_INA219
	|_Adafruit_NeoPixel
	|_ArduinoJson
	|_GRITSBot_I2CInterface
	|_GRITSBot_Main
	|	|_GRITSBot_Main_ESP8266.cpp
	|	|_GRITSBot_Main_ESP8266.h
	|	|_examples
	|		|_basic_firmware (Contains original example, shows as example in Arduino IDE)
	|		|_random_walk
	|_GRITSBot_Messages
	|_GRITSBot_Motor
	|	|_examples
	|		|_basic_firmware(Contains original example, shows as example in Arduino IDE)
	|		|_random_walk
	|_GRITSBot_WiFiConfig
	|_GRITSBot_WirelessInterface
```
