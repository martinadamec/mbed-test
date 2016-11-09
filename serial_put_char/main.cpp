#include "mbed.h"              

DigitalOut led1(LED1);
Serial pc(USBTX, USBRX);

void ledtoggle(DigitalOut* led) {
    *led = 1;
    wait(0.2);
    *led = 0;
    wait(0.2);
}
 
int main() {
    //pc.printf("Echoes back to the screen anything you type\n");
    led1 = 1;
    wait(1);
    led1 = 0;
    
    while(1) {
        pc.putc(pc.getc());
    }
}