/*****************************************************************************
* | File      	:   DEV_Config.h
* | Author      :   Waveshare team
* | Function    :   Hardware underlying interface
* | Info        :
*                Used to shield the underlying layers of each master 
*                and enhance portability
*----------------
* |	This version:   V1.0
* | Date        :   2019-03-12
* | Info        :
#
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
#ifndef _DEV_CONFIG_H_
#define _DEV_CONFIG_H_


#include <stdint.h>
#include <stdio.h>
#include "sysfs_gpio.h"
#include "sysfs_software_spi.h"
/**
 * data
**/
#define UBYTE   uint8_t
#define UWORD   uint16_t
#define UDOUBLE uint32_t

/**
 * GPIO config
**/
#define DEV_RST_PIN     GPIO18
#define DEV_CS_PIN      GPIO22
#define DEV_DRDY_PIN    GPIO17

/**
 * GPIO read and write
**/
#define DEV_Digital_Write(_pin, _value)  SYSFS_GPIO_Write(_pin, _value == 0? LOW:HIGH)
#define DEV_Digital_Read(_pin) 			 SYSFS_GPIO_Read(_pin)

/**
 * SPI
**/
#define DEV_SPI_WriteByte(__value) SYSFS_software_spi_transfer(__value)
#define DEV_SPI_ReadByte() SYSFS_software_spi_transfer(0xff)


/*------------------------------------------------------------------------------------------------------*/
UBYTE DEV_ModuleInit(void);
void DEV_ModuleExit(void);
void DEV_Delay_ms(UWORD xms);

#endif
