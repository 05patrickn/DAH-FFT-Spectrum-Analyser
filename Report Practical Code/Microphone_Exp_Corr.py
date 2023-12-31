import numpy as np
import matplotlib.pyplot as plt

# List of file paths
file_paths = [
    "C:/Users/05pat/OneDrive/Escritorio/DAH Project Final/microphone/1000hz + 2000hz 8Khz_data1_mic.txt",
    "C:/Users/05pat/OneDrive/Escritorio/DAH Project Final/microphone/16Khz_data1_mic.txt",
    "C:/Users/05pat/OneDrive/Escritorio/DAH Project Final/microphone/piano A-mid 16Khz_data1_mic.txt"

]

# Example frequencies in Hz
frequencies = ["0.5Khz + 1KHz Sinusoid", "16Khz Sinusoid", "Key: A-mid (Piano)" ]

sampling_frequency = 61522
# Create a grid of subplots
fig, axs = plt.subplots(len(file_paths), 2, figsize=(12, 2 * len(file_paths)), squeeze=False)

# Loop through each file path and plot the graphs
for i, file_path in enumerate(file_paths):
    # Read data from file
    data = np.loadtxt(file_path, delimiter='\t')
    time_values = data[:, 0]
    voltage_values = data[:, 1]

    # Plot sinusoidal waveforms
    axs[i, 0].plot(time_values[1:], voltage_values[1:], ".-", label=f'Frequency: {frequencies[i]}', color="black")
    axs[i, 0].set_xlabel('Time [s]')
    axs[i, 0].set_ylabel('Voltage [V]')
    axs[i, 0].set_title(f'Experimental Microphone Detection Waveform - {frequencies[i]}')
    axs[i, 0].legend(loc='upper right')  # Set legend to top right
    axs[i, 0].grid(True)

    # Plot Fourier transform
    fft_result = np.fft.rfft(voltage_values)
    fft_magnitude = np.abs(fft_result)
    fft_freq = np.fft.rfftfreq(np.size(voltage_values), 1 / sampling_frequency)
    axs[i, 1].plot(fft_freq[1:], fft_magnitude[1:], label=f'Frequency: {frequencies[i]}',  color="black")
    axs[i, 1].set_xlabel('Frequency [Hz]')
    axs[i, 1].set_ylabel('Power [W/KHz]')
    axs[i, 1].set_title(f'Experimental Fourier Transform - {frequencies[i]}')
    axs[i, 1].legend(loc='upper right')  # Set legend to top right
    axs[i, 1].grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
