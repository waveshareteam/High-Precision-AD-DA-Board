#!/usr/bin/python
# -*- coding:utf-8 -*-
import config
import time
import ADS1256
import DAC8532
import RPi.GPIO as GPIO


try:
    ADC = ADS1256.ADS1256()
    DAC = DAC8532.DAC8532()
    ADC.ADS1256_init()

    DAC.DAC8532_Out_Voltage(0x30, 3)
    DAC.DAC8532_Out_Voltage(0x34, 3)
    while(1):
        ADC_Value = ADC.ADS1256_GetAll()
        print ("0 ADC = %-.5f"%(ADC_Value[0]*5.0/0x7fffff))
        print ("1 ADC = %-.5f"%(ADC_Value[1]*5.0/0x7fffff))
        print ("2 ADC = %-.5f"%(ADC_Value[2]*5.0/0x7fffff))
        print ("3 ADC = %-.5f"%(ADC_Value[3]*5.0/0x7fffff))
        print ("4 ADC = %-.5f"%(ADC_Value[4]*5.0/0x7fffff))
        print ("5 ADC = %-.5f"%(ADC_Value[5]*5.0/0x7fffff))
        print ("6 ADC = %-.5f"%(ADC_Value[6]*5.0/0x7fffff))
        print ("7 ADC = %-.5f"%(ADC_Value[7]*5.0/0x7fffff))

        temp = (ADC_Value[0]>>7)*5.0/0xffff
        print ("DAC : %-.5f"%temp)
        print ("\33[10A")
        DAC.DAC8532_Out_Voltage(DAC8532.channel_A, temp)
        DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 3.3 - temp)

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("ctrl + c:")
    config.module_exit()
    exit()