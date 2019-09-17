#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import RPi.GPIO as GPIO


try:
    ADC = ADS1256.ADS1256()
    if (ADC.ADS1256_init() == -1):
        exit()
    while(1):
    
        # t=time.time()
        ADC_Value = ADC.ADS1256_GetAll()
        # print "  rint " + str((time.time()-t)*1000)+" mS in reading only channel 0\n                          "
        
        print ("0 ADC = %.5f"%(ADC_Value[0]*5.0/0x7fffff))
        print ("1 ADC = %.5f"%(ADC_Value[1]*5.0/0x7fffff))
        print ("2 ADC = %.5f"%(ADC_Value[2]*5.0/0x7fffff))
        print ("3 ADC = %.5f"%(ADC_Value[3]*5.0/0x7fffff))
        print ("4 ADC = %.5f"%(ADC_Value[4]*5.0/0x7fffff))
        print ("5 ADC = %.5f"%(ADC_Value[5]*5.0/0x7fffff))
        print ("6 ADC = %.5f"%(ADC_Value[6]*5.0/0x7fffff))
        print ("7 ADC = %.5f"%(ADC_Value[7]*5.0/0x7fffff)) 
        
        # print "0 ADC = ",(ADC_Value[0])
        # print "1 ADC = ",(ADC_Value[1])
        # print "2 ADC = ",(ADC_Value[2])
        # print "3 ADC = ",(ADC_Value[3])
        # print "4 ADC = ",(ADC_Value[4])
        # print "5 ADC = ",(ADC_Value[5])
        # print "6 ADC = ",(ADC_Value[6])
        # print "7 ADC = ",(ADC_Value[7])

        print ("\33[9A")

        
except :
    GPIO.cleanup()
    print "\r\nProgram end     "
    exit()
