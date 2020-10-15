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

# Now Down-sampling with factor N of subband1
filteredds1 = filtered1[::N]

# Now Down-sampling with factor N of subband2
filteredds2 = filtered2[::N]

# Now Down-sampling with factor N of subband3
filteredds3 = filtered3[::N]

# Now Down-sampling with factor N of subband4
filteredds4 = filtered4[::N]

# Now Down-sampling with factor N of subband5
filteredds5 = filtered5[::N]

# Now Down-sampling with factor N of subband6
filteredds6 = filtered6[::N]

# Now Down-sampling with factor N of subband7
filteredds7 = filtered7[::N]

# Now Down-sampling with factor N of subband8
filteredds8 = filtered8[::N]

# up-sampling

filteredus1 = np.zeros(len(aud))
filteredus2 = np.zeros(len(aud))
filteredus3 = np.zeros(len(aud))
filteredus4 = np.zeros(len(aud))
filteredus5 = np.zeros(len(aud))
filteredus6 = np.zeros(len(aud))
filteredus7 = np.zeros(len(aud))
filteredus8 = np.zeros(len(aud))

filteredus1[::N] = filteredds1
filteredus2[::N] = filteredds2
filteredus3[::N] = filteredds3
filteredus4[::N] = filteredds4
filteredus5[::N] = filteredds5
filteredus6[::N] = filteredds6
filteredus7[::N] = filteredds7
filteredus8[::N] = filteredds8



# synthesis filter
filteredsyn1 = signal.lfilter(f1,1,filteredus1)
filteredsyn2 = signal.lfilter(f2,1,filteredus2)
filteredsyn3 = signal.lfilter(f3,1,filteredus3)
filteredsyn4 = signal.lfilter(f4,1,filteredus4)
filteredsyn5 = signal.lfilter(f5,1,filteredus5)
filteredsyn6 = signal.lfilter(f6,1,filteredus6)
filteredsyn7 = signal.lfilter(f7,1,filteredus7)
filteredsyn8 = signal.lfilter(f8,1,filteredus8)

# playing reconstructed sound
recons = filteredsyn1+filteredsyn2+filteredsyn3+filteredsyn4+filteredsyn5+filteredsyn6+filteredsyn7+filteredsyn8
snd.sound(recons, 32000)


plt.plot(aud)
plt.plot(recons)
plt.show()





