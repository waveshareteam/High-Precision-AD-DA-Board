/*****************************************************************************
* | File      	:   Readme_CN.txt
* | Author      :   Waveshare team
* | Function    :   Help with use
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2019-06-25
* | Info        :   Here is an English version of the documentation for your quick use.
******************************************************************************/
This file is to help you use this routine.

1. Basic information:
This routine was developed based on the 2018-11-13-raspbian-stretch-full system image. Since the current system does not have a hardware SPI,
So use the analog SPI driver,
This routine was developed based on Raspberry Pi 3B, and the routines were verified on Raspberry Pi 3B.
This routine was verified using the High-Precision AD/DA Board module.

2. Pin connection:
Pin connections can be viewed in Config.py and will be repeated here:
OLED   =>    Raspberry Pi/RPI(BCM)
VCC    ->    3.3
GND    ->    GND
DIN    ->    10(MOSI)
CLK    ->    11(SCLK)
DAC8532
CS     ->    23
ADS1256
CS     ->    22
DIR    ->    17
RST    ->    18


3. Basic use:
Since this project is a comprehensive project, you may need to read the following for use:
Python needs to install the corresponding SPI library and GPIO library
python2
    sudo apt-get install python-pip
    sudo pip install Jetson.GPIO
    sudo groupadd -f -r gpio
    sudo usermod -a -G gpio your_user_name
    vsudo udevadm control --reload-rules && sudo udevadm trigger
python3
    sudo apt-get install python-pip3
    sudo pip3 install Jetson.GPIO
    sudo groupadd -f -r gpio
    sudo usermod -a -G gpio your_user_name
    sudo udevadm control --reload-rules && sudo udevadm trigger

Then you need to execute:
C:
    Compile: make
    Run    : sudo ./main
python2
    Run: sudo python main.py
python3
    Run: sudo python3 main.py
