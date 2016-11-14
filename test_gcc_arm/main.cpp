#include "mbed.h"

DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);
DigitalOut led4(LED4);

Serial pc(USBTX, USBRX);

void ledtoggle(DigitalOut* led, int on = 2, int off = 1) {
    *led = 1;
    wait(on);
    *led = 0;
    wait(off);
}

void AppInit() {

    // 2 && 3
    led1 = 1;
    led2 = 1;
    wait(0.5);
    led1 = 0;
    led2 = 0;

    // 1 && 4
    led3 = 1;
    led4 = 1;
    wait(0.5);
    led3 = 0;
    led4 = 0;
}

int main() {

    AppInit();

    while(1) {
        ledtoggle(&led1);
        ledtoggle(&led2);
        ledtoggle(&led3);
        ledtoggle(&led4);
    }
}
