from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2, 1000, endpoint=True) 
sig=signal.square(2 * np.pi* t)	
L=np.linspace(min(sig),max(sig),8)
n=int(np.log2(8))
binary=[format(i,f'0{n}b') for i in range(8)]
# mapping=dict(zip(L,binary))
mapping={L[i]:binary[i] for i in range(8)}
print(mapping)
quantized_signal = [min(L, key=lambda x: abs(x - s)) for s in sig]
encoded_signal=[mapping[i] for i in quantized_signal]
print([int(i,2) for i in encoded_signal])
fig,ax=plt.subplots(2,2)
ax[0][0].plot(t, sig, 'b', label='Original Signal')
ax[0][0].plot(t, quantized_signal, 'r*-', label='Quantized Signal')
ax[0][1].plot(t, encoded_signal, 'b*', label='Original Signal')
ax[1][0].plot(quantized_signal)
plt.legend()
plt.show()
