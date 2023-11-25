import numpy as np
import matplotlib.pyplot as plt

# Function to generate squared waves
def generate_squared_wave(frequency, num_samples=1024, sampling_frequency=61522, amplitude=1):
    time_values = np.arange(num_samples) / sampling_frequency
    values = amplitude * np.sign(np.sin(2 * np.pi * frequency * time_values))
    return time_values, values

# Generate squared waves with varying frequencies
frequencies = [2000, 8000, 32000, 50000]  # Example frequencies in Hz
  # Example frequencies in Hz  # Example frequencies in Hz
sampling_frequency = 61522  # Example sampling frequency in Hz

# Create a 2x2 grid of subplots for each frequency
fig, axs = plt.subplots(len(frequencies), 2, figsize=(12, 10))

# Plot squared waveforms
for i, freq in enumerate(frequencies):
    time_values, values = generate_squared_wave(freq, sampling_frequency=sampling_frequency)
    axs[i, 0].plot(time_values, values,".-", label=f'Frequency: {frequencies[i]/1000} KHz')
    axs[i, 0].set_xlabel('Time [s]')
    axs[i, 0].set_ylabel('Voltage [V]')
    axs[i, 0].set_title(f'Theoretical Squared Waveform {freq/1000} KHz')
    axs[i, 0].legend(loc='upper right')  # Set legend to top right
    axs[i, 0].grid(True)
    axs[i, 0].set_xlim(0, 0.0025)  # Set x-axis limits from 0 to 0.0025

    # Plot Fourier transform
    fft_result = np.fft.rfft(values)
    fft_magnitude = (np.abs(fft_result)**2)/1000
    fft_freq = np.fft.rfftfreq(np.size(values), 1 / sampling_frequency)
    axs[i, 1].plot(fft_freq, fft_magnitude, label=f'Frequency: {frequencies[i]/1000} KHz')
    axs[i, 1].set_xlabel('Frequency [Hz]')
    axs[i, 1].set_ylabel('Power [W/KHz]')
    axs[i, 1].set_title(f'Theoretical Fourier Transform {freq/1000} KHz')
    axs[i, 1].legend(loc='upper right')  # Set legend to top right
    axs[i, 1].grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
