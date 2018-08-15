#!/bin/bash

# remove original binary (possibly unnecessary step)
rm ./basic_firmware/newfirmware.bin

if [ -f "./basic_firmware/basic_firmware.ino.nodemcu.bin" ]
then 	#if firmware bin exists, but not correct name

	echo "Renaming firmware to compatible name"

	#Rename file to newfirmware.bin
	mv ./basic_firmware/basic_firmware.ino.nodemcu.bin ./basic_firmware/newfirmware.bin
	echo "Rename successful, attempting to upload firmware"
else
	#if no .bin file is found with original name of sketch
	echo "Attempting to upload firmware..."
fi

if [ ! -f "./basic_firmware/newfirmware.bin" ] 
then
	#if there is no newfirmware.bin even after the original bin file supposedly reuploads, exit
	echo "Upload failed, file not found: newfirmware.bin"
	exit
fi

echo "Uploading firmware..."
#upload the firmware to the pi in dir /var/www/html using ssh
scp ./basic_firmware/newfirmware.bin pi@192.168.1.129:/var/www/html/
echo "Done"


#optional step, sends an update message (that's what sendGRITS
#messages currently has as it's send message, but this can be 
#changed. See GRITSBOTS_MESSAGES.py)

echo "Sending update message to GRITSBots"

python sendGRITSmessagesUDP.py

