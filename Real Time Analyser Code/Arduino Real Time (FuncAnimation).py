import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

sampling_frequency=64000

# Function to update the plot for each frame
def update(frame):
    # Read data sample from Arduino ADC (1024 bytes, 8-bit resolution)
    data = ser.read(1024)

    # Convert data to an array of integers (values between 0 and 255)
    values = np.frombuffer(data, dtype=np.uint8)
    values = (values / 255) * 5

    # Perform FFT analysis
    fft_result = np.fft.rfft(values)
    fft_magnitude = np.abs(fft_result)
    fft_freq = np.fft.rfftfreq(np.size(values), 1 / sampling_frequency)

    # Clear the previous plot
    ax.clear()

    # Plot the FFT magnitude
    ax.plot(fft_freq, fft_magnitude)
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Power [W/KHz]')
    ax.set_title(f'Experimental Fourier Transform {sampling_frequency/1000} KHz')
    ax.grid(True)
    ax.set_xlim()
    ax.set_ylim(0, 250)


# Set up the serial communication
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)
time.sleep(1)
ser.flushInput()
time.sleep(1)
ser.write(bytes([8, 2]))
time.sleep(1)

# Set up the initial figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create an animation that calls the update function at each frame
ani = FuncAnimation(fig, update, frames=range(100), interval=1000, repeat=False) #interval=1000 animation speed

# Save the animation as a GIF
ani.save('2KHz animated square.gif', writer='pillow')

plt.show()

