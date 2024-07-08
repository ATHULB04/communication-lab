import numpy as np
import matplotlib.pyplot as plt

def calculate_snr(signal, quantized_signal):
    """Calculate Signal-to-Noise Ratio (SNR)"""
    noise = signal - quantized_signal
    signal_power = np.mean(signal**2)
    noise_power = np.mean(noise**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Define parameters
L_values = np.arange(2, 65, 1)  # Number of quantization levels
snr_values = []

# Generate a test signal (e.g., a sinusoidal signal)
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs)
signal = np.sin(2 * np.pi * 5 * t)

for L in L_values:
    # Quantize the signal
    quantized_signal = np.round(signal * (L - 1)) / (L - 1)
    snr = calculate_snr(signal, quantized_signal)
    snr_values.append(snr)

# Plot SNR vs L
plt.figure(figsize=(10, 6))
plt.plot(L_values, snr_values, 'bo-', label="SNR vs L")
plt.grid(True)
plt.xlabel("Number of Quantization Levels (L)")
plt.ylabel("SNR (dB)")
plt.title("SNR vs Number of Quantization Levels (L)")
plt.legend()
plt.show()
