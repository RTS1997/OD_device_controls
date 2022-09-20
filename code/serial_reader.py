import matplotlib.pyplot as plt
import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
time.sleep(2)

data = []
for i in range(40):
    line = arduino.readline()   # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int
        print(str(i)+":"+str(num))
        data.append(num) # add int to data list
arduino.close()

with open('readme.txt', 'w') as f:
    for line in data:
        f.write(line)
        f.write('\n')
f.close()

# build the plot
plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Potentiometer Reading')
plt.title('Potentiometer Reading vs. Time')
plt.show()