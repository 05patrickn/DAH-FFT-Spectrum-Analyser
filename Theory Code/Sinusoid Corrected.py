import numpy as np
import matplotlib.pyplot as plt

# Function to generate sinusoidal waves
def generate_sine_wave(frequency, num_samples=1024, sampling_frequency=61522, amplitude=1):
    time_values = np.arange(num_samples) / sampling_frequency
    values = amplitude * np.sin(2 * np.pi * frequency * time_values)
    return time_values, values

# Generate sinusoidal waves with varying frequencies
frequencies = [8000, 50000]  # Example frequencies in Hz
sampling_frequency = 61522  # Example sampling frequency in Hz

# Create a 2x2 grid of subplots for each frequency
fig, axs = plt.subplots(len(frequencies), 2, figsize=(12, 4))

# Plot sinusoidal waveforms
for i, freq in enumerate(frequencies):
    time_values, values = generate_sine_wave(freq, sampling_frequency=sampling_frequency)
    axs[i, 0].plot(time_values, values, ".-", label=f'Frequency: {frequencies[i]/1000} KHz')
    axs[i, 0].set_xlabel('Time [s]')
    axs[i, 0].set_ylabel('Voltage [V]')
    axs[i, 0].set_title(f'Theoretical Sinusoidal Waveform {freq/1000} KHz')
    axs[i, 0].legend(loc='upper right')
    axs[i, 0].grid(True)

    # Plot Fourier transform
    fft_result = np.fft.rfft(values)
    fft_magnitude = np.abs(fft_result)
    fft_freq = np.fft.rfftfreq(np.size(values), 1 / sampling_frequency)
    axs[i, 1].plot(fft_freq, fft_magnitude, label=f'Frequency: {frequencies[i]/1000} KHz')
    axs[i, 1].set_xlabel('Frequency [Hz]')
    axs[i, 1].set_ylabel('Magnitude')
    axs[i, 1].set_title(f'Theoretical Fourier Transform {freq/1000} KHz')
    axs[i, 1].legend(loc='upper right')
    axs[i, 1].grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
