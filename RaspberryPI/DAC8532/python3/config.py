# -*- coding: utf-8 -*-
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


import spidev
import lgpio
import time

# Pin definition
RST_PIN         = 18
CS_PIN          = 22
CS_DAC_PIN      = 23
DRDY_PIN        = 17

# SPI device, bus = 0, device = 0
SPI = spidev.SpiDev(0, 0)

# lgpio handle
h = None

def digital_write(pin, value):
    lgpio.gpio_write(h, pin, value)

def digital_read(pin):
    return lgpio.gpio_read(h, pin)
def delay_ms(delaytime):
    time.sleep(delaytime // 1000.0)

def spi_writebyte(data):
    SPI.writebytes(data)
    
def spi_readbytes(reg):
    return SPI.readbytes(reg)
    

def module_init():
    global h
    h = lgpio.gpiochip_open(0)

    lgpio.gpio_claim_output(h, RST_PIN)
    lgpio.gpio_claim_output(h, CS_DAC_PIN)
    lgpio.gpio_claim_output(h, CS_PIN)
    lgpio.gpio_claim_input(h, DRDY_PIN)
    SPI.max_speed_hz = 20000
    SPI.mode = 0b01
    return 0

def module_exit():
    """Clean up SPI and lgpio resources opened by module_init()."""
    global h
    try:
        if SPI:
            try:
                SPI.close()
            except Exception:
                pass
        if h is not None:
            try:
                lgpio.gpiochip_close(h)
            except Exception:
                pass
            h = None
    except Exception:
        pass

### END OF FILE ###
