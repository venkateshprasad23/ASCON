import serial
ser = serial.Serial('/dev/ttyACM0',115200)
text_file = open("Gestures.txt", 'w')
a=0;
print "Start"

while True:
	a=ser.readline()
	print a
	text_file.write(a)
    
text_file.close()
ser.close()

