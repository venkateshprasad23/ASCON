import serial
ser = serial.Serial('/dev/ttyACM0',115200)
#removing crap Values
for i in range(20):
    a = ser.readline()
#clearing file
text_file = open("PunchDataRaw.txt", 'w')
text_file.close()

while(1):
    a = ser.readline()
    if(a[0:1] != " "):
        print "ok"
        text_file = open("PunchDataRaw.txt", 'a')
        while a[0:1] != " ":
            a = ser.readline()
            print a
            if(a[0:1] != " "):
                text_file.write(a)
                print "writing"
        text_file.write("end of trial\n\n")
        text_file.close()
