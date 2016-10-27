import time
import serial

# configure the serial connections
ser = serial.Serial(
    port='\\.\COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)

ser.isOpen()
ser.send_break()

print 'Reset done!\r\n'
