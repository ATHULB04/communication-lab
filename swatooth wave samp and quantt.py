import numpy as np
import matplotlib.pyplot as plt

# Define sawtooth wave signal parameters
time = np.arange(0, 0.1, 0.0001)
mssg_f = 100  # message frequency
dc = 1  # dc offset to ensure amplitude ranges from 0 to 2V
amp=4
sig = amp * (np.mod(time * mssg_f, 1) - 0.5)  # Sawtooth wave signal

# Plot the basic message signal
plt.plot(time, sig)
plt.title("Sawtooth Wave Signal")
plt.show()

# Sampling
fs = 16 * mssg_f  # Nyquist Criteria and factor of 16 for high resolution
ts = np.arange(0, 0.1, 1/fs)  # Sampling times
sampled_signal = 2 * (np.mod(ts * mssg_f, 1) - 0.5) + dc

# Plot sampled signal
plt.plot(ts, sampled_signal, "r.-")
plt.title("Sampled Sawtooth Wave Signal")
plt.show()

# Quantization and Encoding for different quantization levels
quantization_levels = [2, 4]

for L in quantization_levels:
    sig_min = min(sig)
    sig_max = max(sig)
    q_levels = np.linspace(sig_min, sig_max, L)
    q_sig = np.digitize(sampled_signal, q_levels) - 1

    # Plot quantized signal
    plt.plot(ts, q_levels[q_sig], "b", ts, q_levels[q_sig], "m*")
    plt.title(f"Quantized Signal with {L} Levels")
    plt.show()

    # Encoding
    bit_no = int(np.log2(L))
    encoded_signal = [format(code, f'0{bit_no}b') for code in q_sig]

    # Plot encoded signal
    plt.plot(ts, encoded_signal, "b", ts, encoded_signal, "g*")
    plt.title(f"Encoded Signal with {L} Levels")
    plt.show()

    print(f"Binary Coded Signal with {L} Levels:", encoded_signal)

    # Quantization Noise Calculation
    q_noise = q_levels[q_sig] - sampled_signal

    # Plot quantization noise
    plt.plot(ts, q_noise)
    plt.title(f"Quantization Noise with {L} Levels")
    plt.show()
