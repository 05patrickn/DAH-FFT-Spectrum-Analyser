import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from DAH import MCP3208

# Define ADC as SPI chip 0 (CE0/GPIO8)
ADC0 = MCP3208(chip=0)

# Define sampling parameters
sampling_rate = 60  # Sample at 1000 Hz
sample_duration = 10.0  # Duration of sampling in seconds (increased for better visualization)
sample_count = int(sampling_rate * sample_duration)
channel = 0  # Specify the ADC channel you want to read

# Initialize arrays to store sampled data and corresponding time stamps
signal_samples = np.empty(sample_count)
time_stamps = np.linspace(0, sample_duration, sample_count, endpoint=False)

# Create a figure and axis for the real-time FFT plot
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, sampling_rate / 2)  # Display up to Nyquist frequency
ax.set_ylim(0, 5)  # Adjust the y-axis limits based on your signal range
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude")
ax.set_title("Real-Time FFT Analysis")

# Create a function to update the FFT plot for each animation frame
def update(frame):
    voltage = ADC0.analogReadVolt(channel)
    signal_samples[frame] = voltage

    #Buffering 500 samples for FFT analysis
    start_frame = max(0, frame - 499)
    fft_result = np.fft.rfft(signal_samples[start_frame : frame + 1])
    fft_magnitude = np.abs(fft_result)

    # Create a frequency axis for the FFT
    fft_freq = np.fft.rfftfreq(sample_count, 1.0 / sampling_rate)

    # Update the real-time FFT plot
    line.set_data(fft_freq, fft_magnitude)
    ax.set_xlim(0, max(fft_freq))

# Create an animation that calls the update function at each frame
ani = FuncAnimation(fig, update, frames=sample_count, repeat=False, blit=False, interval=1000 / sampling_rate)

# Show the real-time FFT plot
plt.show()
