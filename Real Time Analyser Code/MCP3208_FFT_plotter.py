# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from DAH import MCP3208

# Define ADC as SPI chip 0 (CE0/GPIO8)
ADC0 = MCP3208(chip=0)

# Define sampling parameters
sampling_rate = 1000  # Sample at 1000 Hz
sample_duration = 0.5  # Duration of sampling in seconds
sample_count = int(sampling_rate * sample_duration)
channel = 0  # Specify the ADC channel you want to read

# Initialize an array to store sampled data
signal_samples = np.empty(sample_count)

# Read samples from the ADC
for i in range(sample_count):
    voltage = ADC0.analogReadVolt(channel)
    signal_samples[i] = voltage

# Perform FFT analysis
fft_result = np.fft.rfft(signal_samples)
fft_magnitude = np.abs(fft_result)

# Create a frequency axis for the FFT
fft_freq = np.fft.rfftfreq(sample_count, 1.0 / sampling_rate)

# Plot the FFT magnitude
plt.figure(figsize=(10, 6))
plt.plot(fft_freq, fft_magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Analysis")
plt.grid(True)
plt.show()

# Save FFT magnitude data to a file
np.savetxt("fft_data.txt", fft_magnitude)
