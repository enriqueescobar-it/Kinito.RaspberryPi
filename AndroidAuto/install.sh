#!/bin/bash

##
# Script for Android Auto (OpenAuto) install on RPi
# Original install instructions https://github.com/f1xpl/openauto/wiki/Build-instructions
#
# Compatible only with Raspbeery PI 3 or newer (Stretch)
##

# Installing dependeces
whiptail --title "OpenAuto RPi" --msgbox "Installing dependences" 8 78
sudo apt-get update
sudo apt-get install -y libboost-all-dev libusb-1.0.0-dev libssl-dev cmake libprotobuf-dev protobuf-c-compiler protobuf-compiler libqt5multimedia5 libqt5multimedia5-plugins libqt5multimediawidgets5 qtmultimedia5-dev libqt5bluetooth5 libqt5bluetooth5-bin qtconnectivity5-dev pulseaudio librtaudio-dev

cd /opt

# Cloning and building Android Auto SDK
whiptail --title "OpenAuto RPi" --msgbox "Cloning and building Android Auto SDK" 8 78
sudo git clone -b master https://github.com/f1xpl/aasdk.git

sudo mkdir aasdk_build
cd aasdk_build
sudo cmake -DCMAKE_BUILD_TYPE=Release ../aasdk
sudo make -j4

# Building ilclient firmware
whiptail --title "OpenAuto RPi" --msgbox "Building ilclient firmware" 8 78
cd /opt/vc/src/hello_pi/libs/ilclient
sudo make -j4

cd /opt

# Cloning and building OpenAuto 
whiptail --title "OpenAuto RPi" --msgbox "Cloning and building OpenAuto" 8 78
sudo git clone -b master https://github.com/f1xpl/openauto.git

sudo mkdir openauto_build
cd openauto_build
sudo cmake -DCMAKE_BUILD_TYPE=Release -DRPI3_BUILD=TRUE -DAASDK_INCLUDE_DIRS="/opt/aasdk/include" -DAASDK_LIBRARIES="/opt/aasdk/lib/libaasdk.so" -DAASDK_PROTO_INCLUDE_DIRS="/opt/aasdk_build" -DAASDK_PROTO_LIBRARIES="/opt/aasdk/lib/libaasdk_proto.so" ../openauto
sudo make -j4

# Enabling OpenAuto autostart
echo "sudo /opt/openauto/bin/autoapp" >> /home/pi/.config/lxsession/LXDE-pi/autostart

# Starting OpenAuto
whiptail --title "OpenAuto RPi" --msgbox "Strating OpenAuto" 8 78
/opt/openauto/bin/autoapp
