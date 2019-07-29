/*****************************************************************************
* | File      	:   DEV_Config.c
* | Author      :   Waveshare team
* | Function    :   Hardware underlying interface
* | Info        :
*                Used to shield the underlying layers of each master 
*                and enhance portability
*----------------
* |	This version:   V1.0
* | Date        :   2018-11-22
* | Info        :

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
******************************************************************************/
#include "DEV_Config.h"

/********************************************************************************
function:	Delay function
note:
	Driver_Delay_ms(xms) : Delay x ms
********************************************************************************/


/******************************************************************************
function:	Initialization pin
parameter:
Info:
******************************************************************************/
static void DEV_GPIOConfig(void)
{
    pinMode(DEV_CS_PIN, OUTPUT);
}

/******************************************************************************
function:	Module Initialize, the BCM2835 library and initialize the pins, SPI protocol
parameter:
Info:
******************************************************************************/
int DEV_ModuleInit(void)
{
    //1.wiringPiSetupGpio
    //if(wiringPiSetup() < 0)//use wiringpi Pin number table
    if(wiringPiSetupGpio() < 0) { //use BCM2835 Pin number table
        Debug("set wiringPi lib failed	!!! \r\n");
        return 1;
    } else {
        Debug("set wiringPi lib success  !!! \r\n");
    }


    //2.GPIO config
    DEV_GPIOConfig();
	
    //3.spi init
    //wiringPiSPISetup(0,3200000,1);
	wiringPiSPISetupMode(0,3200000,1);
    return 0;
}

void SPI_WriteByte(uint8_t value)
{
    int read_data;
    read_data = wiringPiSPIDataRW(0,&value,1);
    if(read_data < 0)
        perror("wiringPiSPIDataRW failed\r\n");
}


UBYTE SPI_ReadByte()
{
    UBYTE read_data,value=0xff;
    read_data = wiringPiSPIDataRW(0,&value,1);
    if(read_data < 0)
        perror("wiringPiSPIDataRW failed\r\n");
    return value;
}

void DEV_ModuleExit(void)
{

}

