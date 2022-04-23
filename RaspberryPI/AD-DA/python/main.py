#!/usr/bin/python3
# -*- coding:utf-8 -*-

import ADS1256
import DAC8532
import RPi.GPIO as GPIO

ADC = ADS1256.ADS1256()
DAC = DAC8532.DAC8532()
ADC.ADS1256_init()

try:
    
    while(1):

        ADC_Value = ADC.ADS1256_GetAll()
        print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
        print ("1 ADC = %lf"%(ADC_Value[1]*5.0/0x7fffff))
        print ("2 ADC = %lf"%(ADC_Value[2]*5.0/0x7fffff))
        print ("3 ADC = %lf"%(ADC_Value[3]*5.0/0x7fffff))
        print ("4 ADC = %lf"%(ADC_Value[4]*5.0/0x7fffff))
        print ("5 ADC = %lf"%(ADC_Value[5]*5.0/0x7fffff))
        print ("6 ADC = %lf"%(ADC_Value[6]*5.0/0x7fffff))
        print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff))

        temp = (ADC_Value[0]>>7)*5.0/0xffff
        print ("DAC :",temp)
        print ("\33[10A")
        DAC.DAC8532_Out_Voltage(DAC8532.channel_A, temp)
        DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 5.0 - temp)

except:

    DAC.DAC8532_Out_Voltage(DAC8532.channel_A,0)
    DAC.DAC8532_Out_Voltage(DAC8532.channel_B,0)
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
