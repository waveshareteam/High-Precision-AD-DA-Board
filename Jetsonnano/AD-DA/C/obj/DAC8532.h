/*****************************************************************************
* | File      	:   DAC8532.h
* | Author      :   Waveshare team
* | Function    :   
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2019-03-25
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
#ifndef _DAC8532_H_
#define _DAC8532_H_

#include "DEV_Config.h"


#define channel_A   0x30
#define channel_B   0x34

#define DAC_Value_MAX  65535

#define DAC_VREF  3.3

void Write_DAC8532(UBYTE channel, UWORD Data);
void DAC8532_Out_Voltage(UBYTE Channel, float Voltage);


#endif
