import serial
import time
import matplotlib.pyplot as plt

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)

if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parameters

x = 0

while x<100:
    line=ser.readline().decode('utf-8').rstrip()
    print(line)
    x += 1

ser.close()