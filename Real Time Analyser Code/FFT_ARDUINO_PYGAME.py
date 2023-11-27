import serial
import numpy as np
import pygame
import sys
import time

# Open the serial port with baud rate 115200bps (change the port if needed)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)

# A small delay to give the Arduino time to respond
time.sleep(1)

# Clear the serial port buffer to initialize communication
ser.flushInput()

# A small delay may be necessary, again
time.sleep(1)

# Tell the Arduino to start sampling at a given frequency (4 and 2 are arbitrary values)
ser.write(bytes([4, 2]))

frequency = 1250  # According to ChatGPT, would need to change the .ino file

# Initialize Pygame
pygame.init()

# Set the display width and height
window_width, window_height = 800, 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Real-time Voltage and FFT Plot')

# Colors
background_color = (0, 0, 0)
line_color = (255, 255, 255)
font_color = (255, 255, 255)
font_size = 24

# Font
font = pygame.font.Font(None, font_size)

data_buffer = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Read data sample from Arduino ADC (1024 bytes, 8-bit resolution)
    data = ser.read(1024)

    # Convert data to an array of integers (values between 0 and 255)
    values = np.frombuffer(data, dtype=np.uint8)

    # Update the data buffer
    data_buffer.append(values)

    # Keep a limited number of data points for plotting
    max_data_points = 100
    if len(data_buffer) > max_data_points:
        data_buffer.pop(0)

    # Create a new surface
    screen.fill(background_color)

    # Plot the voltage readings
    pygame.draw.lines(screen, line_color, False, [(x, y) for x, y in enumerate(values)], 2)

    # Plot the FFT spectrum
    fft_result = np.fft.rfft(values)
    fft_magnitude = np.abs(fft_result)
    fft_freq = np.fft.rfftfreq(np.size(values), 1 / frequency)

    # Normalize FFT magnitude for display
    fft_magnitude /= np.max(fft_magnitude)
    fft_magnitude *= window_height // 2

    # Shift FFT plot to the right
    fft_freq += window_width // 2

    for i in range(1, len(fft_freq)):
        pygame.draw.line(screen, line_color, (int(fft_freq[i - 1]), int(fft_magnitude[i - 1])),
                         (int(fft_freq[i]), int(fft_magnitude[i])), 2)

    # Add text for voltage reading
    text = font.render(f"Voltage: {values[0]}", True, font_color)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    # Control the update rate by adding a delay
    pygame.time.delay(50)
