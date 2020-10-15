import numpy as np
import scipy.signal as signal
import sound as snd
import matplotlib.pyplot as plt

# filter
N = 8 # num of subbands
f1 = signal.remez(8*N, [0,0.0625, 0.0627, 0.5], [1,0], [1, 100])# nyquist frequency  normalized to 0.5
f2 = signal.remez(8*N, [0, 0.0625, 0.0627, 0.125, 0.127, 0.5], [0, 1, 0], [100, 1, 100])
f3 = signal.remez(8*N, [0, 0.125, 0.127, 0.1875, 0.1877, 0.5], [0, 1, 0], [100, 1, 100])
f4 = signal.remez(8*N, [0, 0.1875, 0.1877, 0.25, 0.27, 0.5], [0, 1, 0], [100, 1, 100])
f5 = signal.remez(8*N, [0, 0.25, 0.27, 0.3125, 0.3127, 0.5], [0, 1, 0], [100, 1, 100])
f6 = signal.remez(8*N, [0, 0.3125, 0.3127, 0.375, 0.377, 0.5], [0, 1, 0], [100, 1, 100])
f7 = signal.remez(8*N, [0, 0.375, 0.377, 0.4375, 0.4377, 0.5], [0, 1, 0], [100, 1, 100])
f8 = signal.remez(8*N, [0, 0.4375, 0.4377, 0.5], [0, 1], [100, 1])
# loading sound file as array
[s,rate] = snd.wavread('Track32.wav')

# Taking first chanel of audio
aud = s[:, 0]

# filter implementation
filtered1 = signal.lfilter(f1,1,aud)
filtered2 = signal.lfilter(f2,1,aud)
filtered3 = signal.lfilter(f3,1,aud)
filtered4 = signal.lfilter(f4,1,aud)
filtered5 = signal.lfilter(f5,1,aud)
filtered6 = signal.lfilter(f6,1,aud)
filtered7 = signal.lfilter(f7,1,aud)
filtered8 = signal.lfilter(f8,1,aud)

# playing filtered sound of subband 1
#snd.sound(filtered1, 32000)

# playing filtered sound of subband 4
#snd.sound(filtered4, 32000)

# Now Down-sampling with factor N of subband1
#filteredds1 = filtered1[::N]

# Now Down-sampling with factor N of subband2
#filteredds4 = filtered4[::N]

# playing filtered sound after downsampling
#snd.sound(filteredds1, 4000)

# playing filtered sound after downsampling
#snd.sound(filteredds4, 4000)


# frequency response

w1,H1 = signal.freqz(f1)
w2,H2 = signal.freqz(f2)
w3,H3 = signal.freqz(f3)
w4,H4 = signal.freqz(f4)
w5,H5 = signal.freqz(f5)
w6,H6 = signal.freqz(f6)
w7,H7 = signal.freqz(f7)
w8,H8 = signal.freqz(f8)



# plotting Impulse response and frequency response
#figure,(w1,w2,w3,w4,w5,w6,w7,w8) = plt.subplots(1)
'''plt.plot(H1)
plt.plot(H2)
plt.plot(f3)
plt.plot(f4)
plt.plot(f5)
plt.plot(f6)
plt.plot(f7)
plt.plot(f8)
'''
#w1.set_xlabel('Sample')
#w1.set_ylabel('Value')
#w1.set_title('Impulse Response ')

plt.plot(w1,20*np.log10(np.abs(H1)))
plt.plot(w2,20*np.log10(np.abs(H2)))
plt.plot(w3,20*np.log10(np.abs(H3)))
plt.plot(w4,20*np.log10(np.abs(H4)))
plt.plot(w5,20*np.log10(np.abs(H5)))
plt.plot(w6,20*np.log10(np.abs(H6)))
plt.plot(w7,20*np.log10(np.abs(H7)))
plt.plot(w8,20*np.log10(np.abs(H8)))

'''plt.set_xlabel('Normalized frequency')
plt.set_ylabel('Magnitude in dB')
plt.set_title('Magnitude Frequency response')
'''
plt.show()
