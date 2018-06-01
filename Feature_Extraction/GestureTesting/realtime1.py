import serial
import numpy as np
from sklearn import preprocessing
import serial
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import model_from_json

ser = serial.Serial('/dev/ttyACM0',115200)
#removing crap Values
for i in range(20):
    a = ser.readline()
#clearing file
text_file = open("Rawdata.txt", 'w')
text_file.close()

while(1):
    a = ser.readline()
    if(a[0:1] != " "):
        print "ok"
        text_file = open("Rawdata.txt", 'a')
        while a[0:1] != " ":
            a = ser.readline()
            print a
            if(a[0:1] != " "):
                text_file.write(a)
                print "writing"
        z=np.loadtxt("Rawdata.txt",delimiter=' ')
        a=np.mean(z,axis=0)
        b=np.std(z,axis=0)
        c=np.hstack((a,b))
        np.savetxt('Rawdata.txt', c ,delimiter=' ')
        #text_file.write("end of trial\n\n")
        text_file.close()
