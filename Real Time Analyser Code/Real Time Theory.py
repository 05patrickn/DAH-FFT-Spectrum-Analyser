import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to generate sinusoidal waves
def generate_sine_wave(frequency, num_samples=1024, sampling_frequency=61522, amplitude=1):
    time_values = np.arange(num_samples) / sampling_frequency
    values = amplitude * np.sin(2 * np.pi * (frequency + 0.5 * np.random.randn()) * time_values)
    return time_values, values

# Function to update the plot for animation
def update(frame, line):
    global random_sampling_frequency

    # Generate the sinusoidal wave with a new random sampling frequency
    random_sampling_frequency = base_sampling_frequency
    time_values, values = generate_sine_wave(frequency, sampling_frequency=random_sampling_frequency)

    # Update the data for the line in the plot
    fft_result = np.fft.rfft(values)
    fft_magnitude = (np.abs(fft_result)**2) / 1000
    fft_freq = np.fft.rfftfreq(len(values), 1 / random_sampling_frequency)

    # Clear the previous plot to avoid overlapping lines
    ax.clear()

    ax.plot(fft_freq, fft_magnitude, marker='o', linestyle='-', label='')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Power [W/KHz]')
    ax.set_title(f'Theoretical Fourier Transform {frequency/1000} KHz')
    ax.grid(True)
    ax.set_xlim(1900, 2200)
    ax.set_ylim(0, 300)
    ax.set_label(f'Frequency: {frequency/1000} KHz, Sampling Frequency: {random_sampling_frequency:.2f} Hz')


    return line,

# Generate a sinusoidal wave with a specific frequency
frequency = 2000  # Example frequency in Hz
base_sampling_frequency = 61522  # Example base sampling frequency in Hz
max_freq = 10000  # Example maximum frequency for x-axis

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Create an initial line for the plot
fft_freq, fft_magnitude = generate_sine_wave(frequency, sampling_frequency=base_sampling_frequency)
line, = ax.plot(fft_freq, fft_magnitude, marker='o', linestyle='-', label='')

# Set x-axis limits
ax.set_xlim(100,300 )

# Create the animation
ani = FuncAnimation(fig, update, fargs=(line,), frames=range(100), interval=20, blit=False)

# Show the animation
plt.show()
