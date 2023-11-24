import serial
import numpy as np
import time
import matplotlib.pyplot as plt

frequency=64000
frequency1=64000

# Open the serial port with baud rate 115200bps (change the port if needed)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)

# A small delay to give the Arduino time to respond
time.sleep(1)

# Clear the serial port buffer to initialize communication
ser.flushInput()

# A small delay may be necessary, again
time.sleep(1)

# Tell the Arduino to start sampling at a given frequency (4 and 2 are arbitrary values)
ser.write(bytes([8, 2]))


# A small delay may be necessary, again
time.sleep(1)

# Read data sample from Arduino ADC (1024 bytes, 8-bit resolution)
data = ser.read(1024)



# Convert data to an array of integers (values between 0 and 255)
values = np.frombuffer(data, dtype=np.uint8)
values=(values/255)*5


time_values=np.arange(values.size)/frequency

freq="1000hz + 2000hz 8"

file_1=(f"{freq}Khz_data1_mic.txt")



# Plot the voltage readings

plt.figure(1)
plt.scatter(time_values[100:], values[100:])
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V])')
plt.title(f'Voltage Readings of {freq}KHz Sinusoidal Waveform \n Sampling frequency {frequency1/1000}KHz')
plt.grid(True)


fft_result = np.fft.rfft(values)
fft_magnitude = np.abs(fft_result)
fft_freq = (np.fft.rfftfreq(np.size(values), 1/frequency))
print(fft_freq[5:][np.argmax(fft_magnitude[5:])])

file_2=(f"{freq}Khz_FFT_data1_mic.txt")



plt.figure(2)
plt.plot(fft_freq[5:], fft_magnitude[5:])
plt.xlabel('Frequecy [Hz]')
plt.ylabel('Voltage [V]')
plt.title(f'Fourier Transforms Voltage \n Readings of {freq}KHz Sinusoidal Waveform \n Sampling frequency {frequency1/1000}KHz')
plt.grid(True)
plt.show()

with open(file_1, "w") as file:
	for i in range (len(values)):
		file.write(f"{time_values[i]}\t{values[i]}\n")

with open(file_2, "w") as file:
	for i in range (len(fft_freq)):
		file.write(f"{fft_freq[i]}\t{fft_magnitude[i]}\n")

