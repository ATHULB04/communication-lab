import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal
fs = 100.0      # Sample rate, Hz
t = np.linspace(0, 1.0, int(fs))
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# Define the low-pass filter (moving average filter)
def moving_average_filter(signal, window_size):
    filtered_signal = np.zeros(len(signal))
    for i in range(len(signal)):
        if i < window_size:
            filtered_signal[i] = np.mean(signal[:i+1])
        else:
            filtered_signal[i] = np.mean(signal[i-window_size+1:i+1])
    return filtered_signal

# Apply the low-pass filter
window_size = 20 # Adjust this for different cutoff frequencies
filtered_signal = moving_average_filter(signal, window_size)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Original Signal')
plt.plot(t, filtered_signal, label='Filtered Signal', linestyle='--')
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Simple Lowpass Filter using Moving Average')
plt.legend()
plt.grid()
plt.show()
