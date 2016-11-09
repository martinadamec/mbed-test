import time
import serial
import sys


time.sleep(1)

def test(ser, letter):
	ser.write(letter)
	out = ''
	# let's wait one second before reading output (let's give device time to answer)
	time.sleep(1)
	while ser.inWaiting() > 0:
		out += ser.read(1)

	if out == letter:
		print letter + ": SUCCESS"
	else:
		print letter + ": FAIL - '" + out + "'"
	sys.stdout.flush()

def restart(ser):
	ser.send_break()
	out = ''
	# let's wait one second before reading output (let's give device time to answer)
	time.sleep(1)
	while ser.inWaiting() > 0:
		out += ser.read(1)
	print "Reset done!"
	sys.stdout.flush()
 
# configure the serial connections
ser = serial.Serial(
    port='\\.\COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

# Restart
restart(ser)

# Test
test(ser, 'a')
test(ser, 'b')
test(ser, 'Z')
test(ser, '-')
test(ser, ' ')

print 'Test done!\r\n'
