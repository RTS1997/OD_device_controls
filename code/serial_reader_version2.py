import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
import datetime

now = datetime.datetime.now()

#initialize serial port
ser = serial.Serial()
ser.port = '/dev/ttyACM0' #Arduino serial port
ser.baudrate = 9600
ser.timeout = 10 #specify timeout when using readline()
ser.open()
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = [] 
ys = []

def animate(i, xs, ys, now):

    #Aquire and parse data from serial port
    line=ser.readline()      #ascii
    line_as_list = line.split(b',')
    i = int(line_as_list[0])
	
	# Add x and y to lists
    ys.append(i)
    new_time = datetime.datetime.now()
    print((new_time - now).total_seconds())
    xs.append((new_time - now).total_seconds())

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, label="Output")

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, now), interval=1000)
plt.show()
ser.close()