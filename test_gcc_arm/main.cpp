#include "mbed.h"

DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);
DigitalOut led4(LED4);

Serial pc(USBTX, USBRX);

void ledtoggle(DigitalOut* led, double time = 0.2) {
    *led = 1;
    wait(time);
    *led = 0;
    wait(time);
}

int main() {
    pc.printf("mbed flashed and communication with PC is OK!");
    led1 = 1;
    led2 = 1;
    led3 = 1;
    led4 = 1;
    wait(1);
    led1 = 0;
    led2 = 0;
    led3 = 0;
    led4 = 0;
    wait(1);
    ledtoggle(&led1, 1);
    ledtoggle(&led2, 1);
    ledtoggle(&led3, 1);
    ledtoggle(&led4, 1);
    wait(1);
    while(1) {
        ledtoggle(&led1);
        ledtoggle(&led2);
        ledtoggle(&led3);
        ledtoggle(&led4);
    }
}
