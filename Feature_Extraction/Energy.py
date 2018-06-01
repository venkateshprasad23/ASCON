import numpy
from scipy.fftpack import fft
import matplotlib.pyplot as plt

def energy(signal):
    fourier = numpy.fft.fft(signal)
    N = len(signal)
    E_fft = numpy.sum(numpy.abs(fourier) ** 2) / N
    return E_fft

Data = numpy.loadtxt("Gestures.txt", delimiter = ',')
print Data

X = Data[:,0]
Y = Data[:,1]
Z = Data[:,2]

print energy(X)
print energy(Y)
print energy(Z)

plt.subplot(311)
plt.plot(X)
plt.subplot(312)
#plt.psd(Signal)
plt.plot(Y)
plt.subplot(313)
plt.plot(Z)
plt.show()

#print Signal
