import time
import serial
print 'Reset start sleep!\r\n'
time.sleep(5)
print 'Reset start!\r\n'
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

out = ''
# let's wait one second before reading output (let's give device time to answer)
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

if out != '':
    print ">>" + out

print 'Reset done!\r\n'
