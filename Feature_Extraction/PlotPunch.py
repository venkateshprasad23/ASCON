import numpy
from scipy.fftpack import fft
import matplotlib.pyplot as plt

"""Signal = numpy.loadtxt("PunchIsolated.txt")
fourier = fft(Signal)
devn = numpy.std(Signal,axis=0)
mean =  numpy.mean(Signal)
print devn
print mean  """

Data = numpy.loadtxt("Gestures.txt", delimiter = ',')
print Data

X = Data[:,0]
Y = Data[:,1]
Z = Data[:,2]

mean =  numpy.mean(X)
fourier = fft(X)


print X
print Y
print fourier
print mean

plt.subplot(311)
plt.plot(X)
plt.subplot(312)
#plt.psd(Signal)
plt.plot(Y)
plt.subplot(313)
plt.plot(fourier)
plt.show()

#print Signal
