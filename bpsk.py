import numpy as np
import matplotlib.pyplot as plt

# Define parameters
# message_frequency = 10
# carrier_frequency = 30
# sampling_frequency = 30 * carrier_frequency


# # Generate time vector
# t = np.arange(0, 2/carrier_frequency, 1 / sampling_frequency)

# # Generate message signal (BPSK modulation)
# message = np.sign(np.cos(2 * np.pi * message_frequency * t) + np.random.normal(scale=0.01, size=len(t)))

# # Generate carrier signal
# carrier = np.cos(2 * np.pi * carrier_frequency * t)

# # Modulate the carrier with the message
# modulated_signal = carrier * message

# # Plot signals
# plt.figure(figsize=(10, 8))

# # Plot message signal
# plt.subplot(3, 1, 1)
# plt.plot(t, message)
# plt.title("Message Signal")

# # Plot carrier signal
# plt.subplot(3, 1, 2)
# plt.plot(t, carrier)
# plt.title("Carrier Signal")

# # Plot BPSK modulated signal
# plt.subplot(3, 1, 3)
# plt.plot(t, modulated_signal)
# plt.title("BPSK Modulated Signal")

# plt.show()

# # Overlay plot for better comparison
# plt.figure(figsize=(10, 6))
# plt.plot(t, message, label="Message Signal")
# plt.plot(t, modulated_signal, "--", label="Modulated Signal")
# plt.plot(t, carrier, "-.", label="Carrier Signal")
# plt.legend()
# plt.show()

# Monte Carlo Simulation for BER calculation
N = 500000  # Number of bits
EbN0dB_list = np.arange(0, 50)  # Range of Eb/N0 values in dB
BER = []  # Bit Error Rate
BER_=[]
# Loop over each Eb/N0 value
for EbN0dB in EbN0dB_list:
    EbN0 = 10**(EbN0dB / 10)  # Convert dB to linear scale
    noise_std_dev = 1 / np.sqrt(2 * EbN0)  # Calculate noise standard deviation
    
    # Generate random BPSK symbols (-1 or +1)
    x = 2 * (np.random.rand(N) >= 0.5) - 1
    y=np.random.rand(N)>=0.5
    y_=2*y-1
    
    # Add Gaussian noise
    noise = noise_std_dev * np.random.randn(N)
    received = x + noise
    new=y+noise
    
    # Detect the received symbols (threshold at 0)
    received_x = 2 * (received >= 0.5) - 1
    received_y = 2 * (new >= 0.5) - 1
    
    # Calculate the number of bit errors
    errors = (x != received_x).sum()
    errors_=(y_!=received_y).sum()
    BER.append(errors / N)
    BER_.append(errors_/N)
print(BER_)
# Plot BER vs Eb/N0
plt.figure(figsize=(10, 6))
plt.semilogy(EbN0dB_list, BER, "go-", label="Simulated BER")
plt.semilogy(EbN0dB_list, BER_, "ro-", label="Theoretical BER")
plt.xscale('linear')
plt.yscale('log')
plt.grid(True, which='both')
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")
plt.title("BER vs Eb/N0 for BPSK")
plt.legend()
plt.show()


