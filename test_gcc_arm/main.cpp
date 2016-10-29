#include "mbed.h"

DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);
DigitalOut led4(LED4);

Serial pc(USBTX, USBRX);

void ledtoggle(DigitalOut* led) {
    *led = 1;
    wait(0.2);
    *led = 0;
    wait(0.2);
}

int main() {
    pc.printf("mbed flashed and communication with PC is OK!");
    led1 = 1;
    led4 = 1;
    wait(1);
    led1 = 0;
    led4 = 0;
    wait(1);
    led2 = 1;
    led3 = 1;
    wait(1);
    led2 = 0;
    led3 = 0;
    wait(1);
    while(1) {
        ledtoggle(&led1);
        ledtoggle(&led2);
        ledtoggle(&led3);
        ledtoggle(&led4);
    }
}
