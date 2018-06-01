import serial
arduinoData = serial.Serial('/dev/ttyACM0',9600)

for i in range(1,11):
	for j in range(0,5):
		print("Enter data for")
		print(i-1)
		raw_input()
		text_file = open("MultiClsTrainingData.txt","a")
		arduinoData.write('a')
		for k in range(0,20):
			myData = (arduinoData.readline().strip())
			if k>9:
			 myData = (arduinoData.readline().strip())
		#        print type(myData)
		#        print (myData.decode('utf-8'))
			 print myData

			 text_file.writelines(myData)
			 text_file.write("\n")
			#com = raw_input("Enter some crap to continue working\n")
		text_file.close()
		arduinoData.write('b')
		#serialFile=open('/dev/ttyACM3','w')
#text_file.write("The next try is below :)\n\n")

