import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_symbols = 10
sps = 8
beta = 0.35
output_length = 150 # Desired output length

# Generate random bits
bits = np.random.randint(0, 2, num_symbols)
print(bits)
# Create the pulse
x = np.array([np.concatenate(([bit*2-1], np.zeros(sps-1))) for bit in bits]).flatten()
print(x)

# Plot the pulse
plt.figure(0)
plt.plot(x, '.-')
plt.grid(True)
plt.show()

# Create the raised-cosine filter
Ts = sps
t = np.arange(-50, 51)
h = 1/Ts * np.sinc(t/Ts) * np.cos(np.pi*beta*t/Ts) / (1 - (2*beta*t/Ts)**2)

# Plot the filter
plt.figure(1)
plt.plot(t, h, '.')
plt.grid(True)
plt.show()

# Convolve the signal with the filter
x_shaped = np.convolve(x, h)

# Trim the convolution result to match the desired output length
start_index = (len(x_shaped) - output_length) // 2
end_index = start_index + output_length
x_shaped_trimmed = x_shaped[start_index:end_index]

# Plot the convolved signal
plt.figure(2)
plt.plot(x_shaped_trimmed, '.-')
plt.grid(True)
plt.show()



y=x_shaped_trimmed
# Add noise
SNR_dB = 10
# Add Gaussian noise
power_signal = np.sum(np.abs(x_shaped_trimmed) ** 2) / len(x_shaped_trimmed)
power_noise = power_signal / (10 ** (SNR_dB / 10))
noise = np.random.normal(0, np.sqrt(power_noise), len(x_shaped_trimmed))
x_noisy = x_shaped_trimmed + noise

# Plot the convolved signal with noise
plt.figure(3)
plt.plot(x_noisy, '.-')
plt.grid(True)
plt.show()

t = np.arange(0, len(x_noisy))  # Assuming each sample corresponds to one second

# Sample the signal
sampled_indices = np.arange(0, len(x_noisy), sps)  # Sample every sps-th sample
x_sampled = x_noisy[sampled_indices]

threshold = 0

# Make decisions based on threshold
decisions = np.where(x_sampled > threshold, 1, 0)

# Plot sampled signal with decisions
plt.figure(4)
plt.step(sampled_indices, decisions, 'g', where='mid', label='Decisions')
plt.xlabel('Time')
plt.ylabel('Amplitude/Decision')
plt.title('Sampled Signal with AWGN and Decisions')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(0)
plt.plot(x, '.-')
plt.grid(True)
plt.show()
