import config
import RPi.GPIO as GPIO


ScanMode = 0


# gain channel
ADS1256_GAIN_E = {'ADS1256_GAIN_1' : 0, # GAIN   1
                  'ADS1256_GAIN_2' : 1,	# GAIN   2
                  'ADS1256_GAIN_4' : 2,	# GAIN   4
                  'ADS1256_GAIN_8' : 3,	# GAIN   8
                  'ADS1256_GAIN_16' : 4,# GAIN  16
                  'ADS1256_GAIN_32' : 5,# GAIN  32
                  'ADS1256_GAIN_64' : 6,# GAIN  64
                 }

# data rate
ADS1256_DRATE_E = {'ADS1256_30000SPS' : 0xF0, # reset the default values
                   'ADS1256_15000SPS' : 0xE0,
                   'ADS1256_7500SPS' : 0xD0,
                   'ADS1256_3750SPS' : 0xC0,
                   'ADS1256_2000SPS' : 0xB0,
                   'ADS1256_1000SPS' : 0xA1,
                   'ADS1256_500SPS' : 0x92,
                   'ADS1256_100SPS' : 0x82,
                   'ADS1256_60SPS' : 0x72,
                   'ADS1256_50SPS' : 0x63,
                   'ADS1256_30SPS' : 0x53,
                   'ADS1256_25SPS' : 0x43,
                   'ADS1256_15SPS' : 0x33,
                   'ADS1256_10SPS' : 0x20,
                   'ADS1256_5SPS' : 0x13,
                   'ADS1256_2d5SPS' : 0x03
                  }

# registration definition
REG_E = {'REG_STATUS' : 0,  # x1H
         'REG_MUX' : 1,     # 01H
         'REG_ADCON' : 2,   # 20H
         'REG_DRATE' : 3,   # F0H
         'REG_IO' : 4,      # E0H
         'REG_OFC0' : 5,    # xxH
         'REG_OFC1' : 6,    # xxH
         'REG_OFC2' : 7,    # xxH
         'REG_FSC0' : 8,    # xxH
         'REG_FSC1' : 9,    # xxH
         'REG_FSC2' : 10,   # xxH
        }

# command definition
CMD = {'CMD_WAKEUP' : 0x00,     # Completes SYNC and Exits Standby Mode 0000  0000 (00h)
       'CMD_RDATA' : 0x01,      # Read Data 0000  0001 (01h)
       'CMD_RDATAC' : 0x03,     # Read Data Continuously 0000   0011 (03h)
       'CMD_SDATAC' : 0x0F,     # Stop Read Data Continuously 0000   1111 (0Fh)
       'CMD_RREG' : 0x10,       # Read from REG rrr 0001 rrrr (1xh)
       'CMD_WREG' : 0x50,       # Write to REG rrr 0101 rrrr (5xh)
       'CMD_SELFCAL' : 0xF0,    # Offset and Gain Self-Calibration 1111    0000 (F0h)
       'CMD_SELFOCAL' : 0xF1,   # Offset Self-Calibration 1111    0001 (F1h)
       'CMD_SELFGCAL' : 0xF2,   # Gain Self-Calibration 1111    0010 (F2h)
       'CMD_SYSOCAL' : 0xF3,    # System Offset Calibration 1111   0011 (F3h)
       'CMD_SYSGCAL' : 0xF4,    # System Gain Calibration 1111    0100 (F4h)
       'CMD_SYNC' : 0xFC,       # Synchronize the A/D Conversion 1111   1100 (FCh)
       'CMD_STANDBY' : 0xFD,    # Begin Standby Mode 1111   1101 (FDh)
       'CMD_RESET' : 0xFE,      # Reset to Power-Up Values 1111   1110 (FEh)
      }

class ADS1256:
    def __init__(self):
        self.rst_pin = config.RST_PIN
        self.cs_pin = config.CS_PIN
        self.drdy_pin = config.DRDY_PIN

    # Hardware reset
    def ADS1256_reset(self):
        config.digital_write(self.rst_pin, GPIO.HIGH)
        config.delay_ms(200)
        config.digital_write(self.rst_pin, GPIO.LOW)
        config.delay_ms(200)
        config.digital_write(self.rst_pin, GPIO.HIGH)
    
    def ADS1256_WriteCmd(self, reg):
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([reg])
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
    
    def ADS1256_WriteReg(self, reg, data):
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([CMD['CMD_WREG'] | reg, 0x00, data])
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
        
    def ADS1256_Read_data(self, reg):
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([CMD['CMD_RREG'] | reg, 0x00])
        data = config.spi_readbytes(1)
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1

        return data
        
    def ADS1256_WaitDRDY(self):
        for i in range(0,400000,1):
            if(config.digital_read(self.drdy_pin) == 0):
                
                break
        if(i >= 400000):
            print ("Time Out ...\r\n")
        
        
    def ADS1256_ReadChipID(self):
        self.ADS1256_WaitDRDY()
        id = self.ADS1256_Read_data(REG_E['REG_STATUS'])
        id = id[0] >> 4
        # print 'ID',id
        return id
        
    #The configuration parameters of ADC, gain and data rate
    def ADS1256_ConfigADC(self, gain, drate):
        self.ADS1256_WaitDRDY()
        buf = [0,0,0,0,0,0,0,0]
        buf[0] = (0<<3) | (1<<2) | (1<<1)
        buf[1] = 0x08
        buf[2] = (0<<5) | (0<<3) | (gain<<0)
        buf[3] = drate
        
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([CMD['CMD_WREG'] | 0, 0x03])
        config.spi_writebyte(buf)
        
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
        config.delay_ms(1) 



    def ADS1256_SetChannal(self, Channal):
        if Channal > 7:
            return 0
        self.ADS1256_WriteReg(REG_E['REG_MUX'], (Channal<<4) | (1<<3))

    def ADS1256_SetDiffChannal(self, Channal):
        if Channal == 0:
            self.ADS1256_WriteReg(REG_E['REG_MUX'], (0 << 4) | 1) 	#DiffChannal  AIN0-AIN1
        elif Channal == 1:
            self.ADS1256_WriteReg(REG_E['REG_MUX'], (2 << 4) | 3) 	#DiffChannal   AIN2-AIN3
        elif Channal == 2:
            self.ADS1256_WriteReg(REG_E['REG_MUX'], (4 << 4) | 5) 	#DiffChannal    AIN4-AIN5
        elif Channal == 3:
            self.ADS1256_WriteReg(REG_E['REG_MUX'], (6 << 4) | 7) 	#DiffChannal   AIN6-AIN7

    def ADS1256_SetMode(self, Mode):
        ScanMode = Mode

    def ADS1256_init(self):
        if (config.module_init() != 0):
            return -1
        self.ADS1256_reset()
        id = self.ADS1256_ReadChipID()
        if id == 3 :
            print("ID Read success  ")
        else:
            print("ID Read failed   ")
            return -1
        self.ADS1256_ConfigADC(ADS1256_GAIN_E['ADS1256_GAIN_1'], ADS1256_DRATE_E['ADS1256_30000SPS'])
        return 0
        
    def ADS1256_Read_ADC_Data(self):
        self.ADS1256_WaitDRDY()
        config.digital_write(self.cs_pin, GPIO.LOW)#cs  0
        config.spi_writebyte([CMD['CMD_RDATA']])
        # config.delay_ms(10)

        buf = config.spi_readbytes(3)
        config.digital_write(self.cs_pin, GPIO.HIGH)#cs 1
        read = (buf[0]<<16) & 0xff0000
        read |= (buf[1]<<8) & 0xff00
        read |= (buf[2]) & 0xff
        if (read & 0x800000):
            read &= 0xF000000
        return read
 
    def ADS1256_GetChannalValue(self, Channel):
        if(ScanMode == 0):# 0  Single-ended input  8 channel1 Differential input  4 channe 
            if(Channel>=8):
                return 0
            self.ADS1256_SetChannal(Channel)
            self.ADS1256_WriteCmd(CMD['CMD_SYNC'])
            # config.delay_ms(10)
            self.ADS1256_WriteCmd(CMD['CMD_WAKEUP'])
            # config.delay_ms(200)
            Value = self.ADS1256_Read_ADC_Data()
        else:
            if(Channel>=4):
                return 0
            self.ADS1256_SetDiffChannal(Channel)
            self.ADS1256_WriteCmd(CMD['CMD_SYNC'])
            # config.delay_ms(10) 
            self.ADS1256_WriteCmd(CMD['CMD_WAKEUP'])
            # config.delay_ms(10) 
            Value = self.ADS1256_Read_ADC_Data()
        return Value
        
    def ADS1256_GetAll(self):
        ADC_Value = [0,0,0,0,0,0,0,0]
        for i in range(0,8,1):
            ADC_Value[i] = self.ADS1256_GetChannalValue(i)
        return ADC_Value
### END OF FILE ###

