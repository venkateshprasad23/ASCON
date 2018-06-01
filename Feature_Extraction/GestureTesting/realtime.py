import numpy as np
#from sklearn import preprocessing
import serial
import numpy
import time



arduinoData = serial.Serial('/dev/ttyACM0',9600)
text_file = open("realtime.txt","w")
#text_file.close()
start_time = System.currentTimeMillis();
wait_time = 10000;
end_time = start_time + wait_time;

while (System.currentTimeMillis() < end_time):
    myData = (arduinoData.readline().strip())
    print myData

    text_file.writelines(myData)
    text_file.write("\n")


realtime = np.loadtxt("realtime.txt",delimiter = ' ',converters = {1: lambda s: float(s.strip(";"))})

a1 = np.mean(realtime,axis=0)
b1 = np.std(realtime,axis=0)

c1 = np.hstack((a1,b1))

    #postnormalisedmatrix = preprocessing.scale(c1)
    #print postnormalisedmatrix

print c1
np.savetxt('testgesture.txt',c1,delimiter=' ')




text_file.close()
