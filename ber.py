import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 100000  # Number of bits
EbN0dB_list = np.arange(0, 11)  # Range of Eb/N0 values in dB
BER = []  # Bit Error Rate

# Loop over each Eb/N0 value
for EbN0dB in EbN0dB_list:
    EbN0 = 10**(EbN0dB / 10)  # Convert dB to linear scale
    noise_std_dev = np.sqrt(1 / (2 * EbN0))  # Calculate noise standard deviation
    
    # Generate random BPSK symbols (-1 or +1)
    x = 2 * (np.random.rand(N) >= 0.5) - 1
    
    # Add Gaussian noise
    noise = noise_std_dev * np.random.randn(N)
    received = x + noise
    
    # Detect the received symbols (threshold at 0)
    received_x = np.sign(received)
    
    # Calculate the number of bit errors
    errors = np.sum(x != received_x)
    BER.append(errors / N)

# Plot BER vs Eb/N0
fig , ax = plt.subplots(2,2)
ax[0][1].semilogy(EbN0dB_list, BER, "bo-", label="Simulated BER")


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Define the range of Eb/N0 values in dB
EbN0dB_list_1 = np.arange(0, 11, 1)

# Convert Eb/N0 from dB to linear scale
EbN0_linear_1 = 10**(EbN0dB_list_1 / 10)

# Calculate theoretical BER using the Q-function
BER_theoretical_1 = 0.5 * erfc(np.sqrt(EbN0_linear_1))

# Plot the theoretical BER vs Eb/N0

ax[1][1].semilogy(EbN0dB_list_1, BER_theoretical_1, "r-", label="Theoretical BER")
plt.show()
