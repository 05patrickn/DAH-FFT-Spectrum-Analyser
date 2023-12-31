import numpy as np
import matplotlib.pyplot as plt

# List of file paths
file_paths = [
    "C:/Users/05pat/OneDrive/Escritorio/DAH Project Final/Results/2Khz_data1_trn.txt",
    "C:/Users/05pat/OneDrive/Escritorio/DAH Project Final/Results/8Khz_data1_trn.txt",
    "C:/Users/05pat/OneDrive/Escritorio/DAH Project Final/Results/32Khz_data1_trn.txt",
    "C:/Users/05pat/OneDrive/Escritorio/DAH Project Final/Results/50Khz_data1_trn.txt"
]

# Example frequencies in Hz
frequencies = [2000, 8000, 32000, 50000]  # Example frequencies in Hz
 #Add frequencis

sampling_frequency = 61522  # Sampling frequency in Hz

# Create a grid of subplots
fig, axs = plt.subplots(len(file_paths), 2, figsize=(12, 2.5 * len(file_paths)), squeeze=False)

# Loop through each file path and plot the graphs
for i, file_path in enumerate(file_paths):
    # Read data from file
    data = np.loadtxt(file_path, delimiter='\t')
    time_values = data[:, 0]
    voltage_values = data[:, 1]

    # Plot sinusoidal waveforms
    axs[i, 0].plot(time_values, voltage_values, ".-", label=f'Frequency: {frequencies[i]/1000} KHz', color="black")
    axs[i, 0].set_xlabel('Time [s]')
    axs[i, 0].set_ylabel('Voltage [V]')
    axs[i, 0].set_title(f'Experimental Sawtooth Waveform - {frequencies[i]/1000} KHz')
    axs[i, 0].legend(loc='upper right')  # Set legend to top right
    axs[i, 0].grid(True)
    axs[i, 0].set_xlim(0, 0.0025)  # Set x-axis limits from 0 to 0.0025

    # Plot Fourier transform
    fft_result = np.fft.rfft(voltage_values)
    fft_magnitude = (np.abs(fft_result)**2)/1000
    fft_freq = np.fft.rfftfreq(np.size(voltage_values), 1 / sampling_frequency)
    axs[i, 1].plot(fft_freq[1:], fft_magnitude[1:], label=f'Frequency: {frequencies[i]/1000} KHz', color="black")
    axs[i, 1].set_xlabel('Frequency [Hz]')
    axs[i, 1].set_ylabel('Power [W/KHz]')
    axs[i, 1].set_title(f'Experimental Fourier Transform - {frequencies[i]/1000} KHz')
    axs[i, 1].legend(loc='upper right')  # Set legend to top right
    axs[i, 1].grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
