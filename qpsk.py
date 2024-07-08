import numpy as np
pi=np.pi
import matplotlib.pyplot as plt


def modulation():
    # Parameters
    fc = 30  # Carrier frequency
    overSamplingRate = 30  # Oversampling rate
    fs = overSamplingRate * fc  # Sampling frequency

    # Generate random bit sequence
    num_bits = 30
    x = np.random.randint(0, 2, num_bits)
    print(x)
    x_str = ''.join([str(i) for i in x])
    print("Message string:", x_str)
    x_str ="010001110110011110000110"

    # Group bits into pairs
    message = [x_str[i:i+2] for i in range(0, len(x_str), 2)]
    print("Message grouped as 2-bit pairs:", message)

    # QPSK modulation for each 2-bit pair
    ts=np.arange(0,2/fc,1/fs)
    print(len(ts))
    modulation_map = {
        '00': np.cos(2 * np.pi * fc*ts+3*np.pi/4,),
        '01': np.cos(2 * np.pi * fc*ts+np.pi/4,),
        '10': np.cos(2 * np.pi * fc*ts+-3*np.pi/4,),
        '11': np.cos(2 * np.pi * fc*ts+-np.pi/4,),
    }

    modulated_signal = np.concatenate([modulation_map[pair] for pair in message])
    print(len(modulated_signal))
    # Time vector for plotting
    t = np.arange(0, len(modulated_signal))
    print(len(t))
    print("Lengths - t:", len(t), "modulated_signal:", len(modulated_signal))

    # Plot the modulated signal
    plt.figure(figsize=(14, 6))
    plt.plot(t, modulated_signal,"g")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Modulated Signal")
    plt.grid(True)
    plt.show()

# BER calculation
N = 500000  # Number of bits for BER calculation
EbN0dB_list = np.arange(0, 50)  # Eb/N0 range in dB
BER = []

for i in range(len(EbN0dB_list)):
    EbN0dB = EbN0dB_list[i] 
    EbN0 = 10**(EbN0dB/10)
    noise = 1/np.sqrt(2 * EbN0)
    x=[1 if x>0.5 else -1 for x in np.random.randint(0,2,N)]
    x_str = [str(int(i)) for i in x] 
    x_str = "".join(x_str)
    message = [x_str[i : i+2] for i in range(0,len(x_str),2)]
    channel = x + np.random.randn(N) * noise 
    received_x = channel >= 0.5
    xReceived_str = [str(int(i)) for i in received_x] 
    xReceived_str = "".join(xReceived_str)
    messageReceived = [xReceived_str[i : i+2] for i in range(0,len(x_str),2)]
    message = np.array(message)
    messageReceived = np.array(messageReceived)
    errors = (message != messageReceived).sum() 
    BER.append(errors/N)
print(BER)


# Plot BER
plt.figure()
plt.semilogy(EbN0dB_list, BER, marker='o')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")
plt.title("BER vs Eb/N0 for QPSK")
plt.grid(True)
plt.show()
