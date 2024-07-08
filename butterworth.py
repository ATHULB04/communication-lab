import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Sample rate and desired cutoff frequency (in Hz)
fs = 1000.0       # Sample rate, Hz
cutoff = 100.0    # Desired cutoff frequency of the filter, Hz

# Create a Butterworth filter
order = 4
nyquist = 0.5 * fs
normal_cutoff = cutoff / nyquist
b, a = butter(order, normal_cutoff, btype='low', analog=False)

# Create a sample signal
t = np.linspace(0, 1.0, int(fs))
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# Apply the Butterworth filter
filtered_signal = filtfilt(b, a, signal)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Original Signal')
plt.plot(t, filtered_signal, label='Filtered Signal', linestyle='--')
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Butterworth Lowpass Filter')
plt.legend()
plt.grid()
plt.show()
