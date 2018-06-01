# ASCON
American Sign Language to Speech Converter
1.The Neural networks folder contains the codes and the models for training and testing the neural network.
2.The Pragyan Final folder contains the final testing codes and the model. This was used for display during Pragyan, the annual techno-management festival of NIT Trichy.
3.The Documentation folder contains the sign language and link to the video of the working prototype.
4.The Feature extraction folder contains the codes for data preprocessing and the attempt at activity recognition to differentiate 
between dynamic and static gestures. As this could not be completed, a button trigger was used to indicate the start and end of the gesture. The button had to be pressed for as long as the gesture was done. All the neural net codes were run on BeagleBone Black. 

Improvements Required:-
1. Activity recognition to differentiate between static and dynamic gestures.
2. Integration of all processing on the single board computer, BeagleBone Black. Right now, the Arduino Mega is being used for     collecting data from the IMU and Flex sensors.
3. More gestures to be classified.
4. Smaller speakers and power source to be used to make it more compact.




