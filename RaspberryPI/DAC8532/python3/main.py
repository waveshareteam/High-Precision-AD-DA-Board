#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import DAC8532
import RPi.GPIO as GPIO


try:
    print("Program start\r\n")
    
    DAC = DAC8532.DAC8532()
    DAC.DAC8532_Out_Voltage(DAC8532.channel_A, 0)
    DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 0)
    

    while(1):
        for i in range(0,33,1):
            DAC.DAC8532_Out_Voltage(DAC8532.channel_A, 3.3 * i / 33)
            DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 3.3 - 3.3 * i / 33)
            time.sleep(0.2)
            
        for i in range(0,33,1):
            DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 3.3 * i / 33)
            DAC.DAC8532_Out_Voltage(DAC8532.channel_A, 3.3 - 3.3 * i / 33)
            time.sleep(0.2)
    
except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
