import numpy as np
import pygame
from DAH import MCP3208

"""Pygame was not worth using, problematic."""

# Initialize Pygame
pygame.init()

# Define ADC as SPI chip 0 (CE0/GPIO8)
ADC0 = MCP3208(chip=0)

# Define sampling parameters
sampling_rate = 100  # Sample at 500 Hz
sample_duration = 20.0  # Duration of sampling in seconds (increased for better visualization)
sample_count = int(sampling_rate * sample_duration)
channel = 0  # Specify the ADC channel you want to read

# Initialize arrays to store sampled data and corresponding time stamps
signal_samples = np.empty(sample_count)
time_stamps = np.linspace(0, sample_duration, sample_count, endpoint=False)

# Pygame setup
pygame.display.set_caption("Real-Time FFT Analysis")
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Create a function to update the FFT plot for each frame
def update(frame):
    voltage = ADC0.analogReadVolt(channel)
    signal_samples[frame] = voltage

    # Buffering 500 samples for FFT analysis
    start_frame = max(0, frame - 499)
    fft_result = np.fft.rfft(signal_samples[start_frame : frame + 1])
    fft_magnitude = np.abs(fft_result)

    # Create a frequency axis for the FFT
    fft_freq = np.fft.rfftfreq(sample_count, 1.0 / sampling_rate)

    # Draw the real-time FFT plot
    screen.fill((0, 0, 0))  # Clear the screen
    pygame.draw.line(screen, (255, 255, 255), (0, height // 2), (width, height // 2), 2)  # X-axis
    pygame.draw.line(screen, (255, 255, 255), (width // 2, 0), (width // 2, height), 2)  # Y-axis

    # Plot the FFT magnitude
    for i in range(len(fft_freq)):
        x = int(fft_freq[i] * (width // 2) / (sampling_rate / 2))
        y = int(height - fft_magnitude[i] * height / max(fft_magnitude))
        pygame.draw.circle(screen, (0, 255, 0), (x, y), 2)

    pygame.display.flip()

# Main loop
frame = 0
running = True
while running and frame < sample_count:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update(frame)
    frame += 1
    clock.tick(sampling_rate)  # Adjust the clock tick to control the update rate

pygame.quit()
