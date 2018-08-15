#!/bin/bash

rm ./basic_firmware/newfirmware.bin


if [ -f "./basic_firmware/basic_firmware.ino.nodemcu.bin" ]
then
	echo "Renaming firmware to compatible name"
	mv ./basic_firmware/basic_firmware.ino.nodemcu.bin ./basic_firmware/newfirmware.bin
	echo "Rename successful, attempting to upload firmware"
else
	echo "Attempting to upload firmware..."
fi

if [ ! -f "./basic_firmware/newfirmware.bin" ] 
then
	echo "Upload failed, file not found: newfirmware.bin"
	exit
fi

echo "Uploading firmware..."
scp ./basic_firmware/newfirmware.bin pi@192.168.1.129:/var/www/html/
echo "Done"

echo "Sending update message to GRITSBots"

python sendGRITSmessagesUDP.py

