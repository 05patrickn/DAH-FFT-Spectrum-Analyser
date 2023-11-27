import serial
import numpy as np
import time
import matplotlib.pyplot as plt

# Open the serial port with baud rate 115200bps (change the port if needed)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)
time.sleep(1) # small delay to give the Arduino time to respond
# Clear the serial port buffer to initialize communication
ser.flushInput()
time.sleep(1) # small delay to give the Arduino time to respond

# input parameters
bytesinput = 8 # integer between 4 and 255 that dictates the sampling frequency
signal_frequency = 20000 #Hz
sampling_frequency = 1/(2.05E-06*bytesinput - 1.2E-07)

# Tell the Arduino to sample at a given frequency
ser.write(bytes([int(bytesinput), 2]))
time.sleep(1)

# set up plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot()
line1, = ax.plot(np.linspace(0,sampling_frequency/2,513),np.arange(513),'r-')


while True:
    try:
        # Read 1024 bytes of datafrom ADC and convert to integer array
        data = ser.read(1024) 
        values = np.frombuffer(data, dtype=np.uint8)
        
        # Perform fft
        fft_result = np.fft.rfft(values)
        fft_magnitude = np.abs(fft_result)
        
        # update plot
        fig.canvas.flush_events()
        line1.set_ydata(fft_magnitude)
        fig.canvas.draw()
        time.sleep(2)

    except KeyboardInterrupt:
        break
    
    
    
