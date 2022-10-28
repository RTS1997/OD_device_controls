import serial
import time


def call_serial():
    try:
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
    except:
        try:
            ser = serial.Serial(port='COM4', baudrate=9600, timeout=1)
        except:
            print("No serial port found")

    return ser

def check_serial_connection(ser):
    assert ser.is_open==True, 'Serial port is not open'
    print("\nAll right, serial port now open. Configuration:\n")
    print(ser, "\n") #print serial parameters

def create_results_file(file_name='results.csv'):
    columns = 'time'+','+'voltage'+"\n"
    with open(file_name, 'w') as re:
        re.write(columns)

def write_results(time, line, file_name='results.csv'):
    write_input = str(time)+','+str(line)+"\n"
    with open(file_name, 'a') as re:
        re.write(write_input)

def run_measurements(dt):
    ser = call_serial()
    check_serial_connection(ser)
    create_results_file()
    start_time = time.time()
    while time.time() < start_time+dt:
        line = ser.readline().decode('utf-8').rstrip()
        write_results(round(time.time()-start_time, 3), line)
        print(line)

    ser.close()

# def run_calibration():
#     ser = call_serial()
#     ser.close()

dt = 10
run_measurements(dt)






