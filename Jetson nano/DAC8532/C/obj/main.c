#include <stdlib.h>     //exit()
#include <signal.h>     //signal()
#include <time.h>
#include "DAC8532.h"
#include "stdio.h"

#include <string.h>

void  Handler(int signo)
{
    //System Exit
    printf("\r\nEND                  \r\n");
    DEV_ModuleExit();

    exit(0);
}

int main(void)
{
    UDOUBLE i;
    DEV_ModuleInit();

    // Exception handling:ctrl + c
    signal(SIGINT, Handler);
    
    printf("Program start\r\n");
    
    DAC8532_Out_Voltage(channel_A, 0);
    while(1){
        for(i=0;i<33;i++){
            DAC8532_Out_Voltage(channel_A, DAC_VREF * i / 33);
            DAC8532_Out_Voltage(channel_B, DAC_VREF - DAC_VREF * i / 33);
            DEV_Delay_ms(100);
        }
        for(i=0;i<33;i++){
            DAC8532_Out_Voltage(channel_B, DAC_VREF * i / 33);
            DAC8532_Out_Voltage(channel_A, DAC_VREF - DAC_VREF * i / 33);
            DEV_Delay_ms(100);
        }
    }
    return 0;
}
