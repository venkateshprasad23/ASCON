import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from keras.wrappers.scikit_learn import KerasClassifier

seed=7
numpy.random.seed(seed)

X= numpy.loadtxt("MultiClsTrainingData.txt",delimiter=' ')
#Z= numpy.loadtxt("TestDataMultiCls.txt",delimiter=' ')
Y=list()
for i in range(10):
    for j in range(50):
        Y.append(i)

encoder= LabelEncoder()
encoder.fit(Y)
encoded_Y=encoder.transform(Y)
dummy_y = np_utils.to_categorical(encoded_Y)

def baseline_model():
    model=Sequential()
    model.add(Dense(10,input_dim=5,init='normal',activation='relu'))
    model.add(Dense(10,init='normal',activation='sigmoid'))

    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model

#estimator= KerasClassifier(build_fn=baseline_model,nb_epoch=300,batch_size=20,verbose=2)
#estimator.fit(X,dummy_y)

model = baseline_model()
model.fit(X,dummy_y,nb_epoch=300,batch_size=20,verbose=2)

#prediction = estimator.predict(Z)
#print (prediction)
#modelPrediction = model.predict_classes(Z)
#print (modelPrediction)


model_json = model.to_json()
with open("FinalModelFLEX.json","w") as json_file:
    json_file.write(model_json)

model.save_weights("FinalModelFLEX.h5")
print("Saved model to Disk")
