import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import model_from_json
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
import serial


import pyttsx

def say(s):
	engine = pyttsx.init()
	rate=engine.getProperty('rate')
	engine.setProperty('rate',rate)
	voices=engine.getProperty('voices')
	engine.setProperty('voice','english-us')
	engine.say(s)
	a=engine.runAndWait()

ser = serial.Serial('/dev/ttyACM3',115200)
#to remove crap values
for i in range(20):
    a = ser.readline()

json_file= open('FinalModel.json','r')
json_model = json_file.read()
json_file.close()
model= model_from_json(json_model)
model.load_weights("FinalModel.h5")
print("Loaded IMU model from Disk")

json_fileFLEX= open('FinalModelFLEX.json','r')
json_modelFLEX = json_fileFLEX.read()
json_fileFLEX.close()
modelFLEX= model_from_json(json_modelFLEX)
modelFLEX.load_weights("FinalModelFLEX.h5")
print("Loaded FLEX model from Disk")

Y=["Sorry","Sorry","Sorry","Sorry","Sorry","Thank you","Thank you","Thank you","Thank you","Thank you","What","What","What","What","What"]

encoder= LabelEncoder()
encoder.fit(Y)
encoded_Y=encoder.transform(Y)

while(1):
    a = ser.readline()
    if(a[0:1] != " "):
        print "ok"
        text_file = open("TestDataMultiCls.txt", 'w')
        while a[0:1] != " ":
            a = ser.readline()
            print a
            if(a[0:1] != " "):
                text_file.write(a)
                print "writing"
        text_file.close()
        Z = np.loadtxt("TestDataMultiCls.txt",delimiter = ' ')

        flex = Z[:,0:5]
        imu = Z[:,5:8]

        a = np.mean(flex,axis=0)
        b= np.mean(imu,axis=0)
        c=np.std(imu,axis=0)
        d = np.hstack((b,c))
        #d = np.hstack((a,d))
        d = np.vstack((d,d))
        d = np.vstack((d,d))
	
	

	x=c.astype(int)

	
	if x[0]<200 and x[1]<200 and x[2]<200:
		
		predictionsFLEX=modelFLEX.predict_classes(flex)
	    	print(predictionsFLEX)
		say(predictionsFLEX[0])
	else:
		
		predictions=model.predict_classes(d)
	  	print(predictions)
		encoder_Speech=encoder.inverse_transform(predictions)
		print(encoder_Speech)
		say(encoder_Speech[0])


   

ser.close()
