import numpy as np
import matplotlib.pyplot as plt

# Time and Signal Generation
time = np.arange(0, 0.1, 0.0001)
mssg_f = 100
dc = 2
sig = np.sin(2 * np.pi * mssg_f * time) + dc

# Plotting the original signal
plt.plot(time, sig)
plt.title("Signal")
plt.show()

# Sampling the signal
fs = 16 * mssg_f
ts = np.arange(0, 0.05, 1 / fs)
sampled_signal = dc + np.sin(2 * np.pi * mssg_f * ts)

# Plotting the sampled signal
plt.plot(ts, sampled_signal, "r.-")
plt.title("Sampled Signal")
plt.show()

# Quantizing the signal
L = int(input("Enter no.of quantization levels: "))
sig_min = round(min(sig))
sig_max = round(max(sig))
q_levels = np.linspace(sig_min, sig_max, L)
# q_sig = [min(q_levels, key=lambda x: abs(x - s)) for s in sampled_signal]
q_sig = []
for s in sampled_signal:
    min_diff = float('inf')
    quantized_value = None
    for q in q_levels:
        diff = abs(q - s)
        if diff < min_diff:
            min_diff = diff
            quantized_value = q
    q_sig.append(quantized_value)



# Plotting the quantized signal
plt.plot(ts, q_sig, "b", ts, q_sig, "m*")
plt.title("Quantized Signal")
plt.show()

# Quantizer Visualization
q_level = [min(q_levels, key=lambda x: abs(x - s)) for s in np.linspace(0.9, 3, 1000)]
plt.plot(np.linspace(0.725, 3, 1000), q_level)
plt.title("Quantizer")
plt.show()

# Encoding the quantized signal
q_level_map = {q: idx for idx, q in enumerate(q_levels)}
bit_no = int(np.log2(L))
binary_code = {i: format(i, f'0{bit_no}b') for i in range(L)}

print("Quantization Levels Mapping:", q_level_map)
print("\nBinary Code:", binary_code)

encoded_signal = [q_level_map[q] for q in q_sig]

# Plotting the encoded signal
plt.plot(ts, encoded_signal, "b", ts, encoded_signal, "g*")
plt.title("Encoded Signal")
plt.show()

binary_coded_signal = [binary_code[k] for k in encoded_signal]
print("Binary Coded Signal:", binary_coded_signal)

# Quantization Noise
def power(signal):
    return np.mean(np.square(signal))

q_noise = np.array(q_sig) - sampled_signal

# Plotting the quantization noise
plt.plot(ts, q_noise)
plt.title("Quantization Noise")
plt.show()

# SNR Calculation
p_signal = power(sig)
p_noise = power(q_noise)
snr = p_signal / p_noise
snr_db = 20 * np.log10(snr)
print("Signal-to-Noise ratio in dB: ", snr_db)

# SNR vs Number of bits per symbol
snr_db = []
s_min = round(min(sig))
s_max = round(max(sig))
power_signal = power(sig)

for i in range(1, 11):
    R = i
    L = 2 ** R
    step_size = (s_max - s_min) / L
    power_noise = (step_size ** 2) / 3
    snr = power_signal / power_noise
    snr_db.append(20 * np.log10(snr))

# Plotting SNR vs No. of bits per symbol
plt.plot(range(1, 11), snr_db, "r*-")
plt.xlabel("No. of Bits per Symbol")
plt.ylabel("SNR in dB")
plt.title("SNR vs No. of Bits per Symbol")
plt.show()
