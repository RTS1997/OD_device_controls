import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=10)
time.sleep(1)

fig, ax = plt.subplots()

data = []

# Animate plot
def animate(i, data, arduino):
    for i in range(100):
        line = arduino.readline().decode('utf-8').rstrip()   # read a byte string
        if line:
            # line= arduino.readline().decode()  # convert the byte string to a unicode string
            num = int(line) # convert the unicode string to an int
            print(str(i)+":"+str(num))
            data.append(num) # add int to data list
    arduino.close()

    ax.clear()
    ax.plot(data)

ani = animate.FuncAnimation(fig, data, arduino)
plt.show()







# build the plot
# plt.plot(data)
# plt.show()
# plt.xlabel('Time')
# plt.ylabel('Potentiometer Reading')
# plt.title('Potentiometer Reading vs. Time')