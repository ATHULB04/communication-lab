import numpy as np
import matplotlib.pyplot as plt

# Parameter
T = 1
Fs = 100
beta = 1

# Raised Cosine Filter Function
def raised_cosine(t, beta):
    return (1/T)*np.sinc(t/T) * np.cos(np.pi * beta * t/T) / (1 - (2 * beta * t/T) ** 2)



# Binary Sequence
binary_sequence = np.random.randint(0, 2, 100)
j = np.array(binary_sequence) * 2 - 1 # NRZ

# Time vector
t = np.arange(T-2, (len(j)+2) * T, 1 / Fs)

# Pulse-shaped signal
y = sum(j[k] * raised_cosine(t - k * T, beta) for k in range(len(j)))
print(y)
# Plotting
fig, ax = plt.subplots(2, 2)

# Binary Message
ax[0][0].step([i for i in range(len(binary_sequence))],binary_sequence)
ax[0][0].set_title("Binary message")

# Impulse Response of Raised Cosine Filter
t_impulse = np.arange(-5, 5, 0.01)
ax[0][1].plot(raised_cosine(t_impulse, beta))
ax[0][1].set_title("Impulse response (Raised Cosine)")

# Pulse-shaped Signal
ax[1][0].plot(y)
ax[1][0].set_title("Pulse-shaped Signal")

# Eye Diagram

for i in range( 5*Fs, len(y) - 5*Fs, Fs):
    ax[1][1].plot(y[i:i + 2 * Fs], 'blue')
ax[1][1].set_title("Eye diagram")

plt.tight_layout()
plt.show()
