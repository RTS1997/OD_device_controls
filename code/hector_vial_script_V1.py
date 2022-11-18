import argparse
import serial
from statistics import mean
from statistics import stdev
import time


def call_serial():
    try:
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
    except:
        try:
            ser = serial.Serial(port='COM9', baudrate=9600, timeout=1)
        except:
            try:
                ser = serial.Serial(port='COM3', baudrate=9600, timeout=1)
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

def run_calibration(number_of_ODs=1, cdt=10):
    # Create calibration file
    ser = call_serial()
    line_values = []

    with open('calibration_file.csv', 'a') as re:
        re.write('OD_values'+','+'mean_v'+','+'std_v'+"\n")
        selector = input("Initiated calibration, y to start, n to abort:")
        selector = str(selector).lower()
        if selector == 'y':
            for od in range(0, int(number_of_ODs)):
                line_values = []
                od_value = input("Enter OD value")
                input("Enter anything once culture is replaced")
                time.sleep(1)
                start_time = time.time()
                while time.time() < start_time+cdt:
                    line_values.append(ser.readline().decode('utf-8').rstrip())

                re.write(str(od_value)+','+str(mean(line_values))+str(stdev(line_values))+"\n")
                print(mean(line_values))
        else:
            print('Abort')
    return 'Calibration done'


# def run_calibration():
#     ser = call_serial()
#     ser.close()

# General python statement
# This code allows the script to be used as the main program,
# But also to be used as an import
# If it is imported via another script, everything below the if statement
# won't be executed and only the functions above can be used

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="OD_vial_holder"
    )

    parser.add_argument(
        "--time_exp",
        type=int,
        required=True,
        help="Experiment duration in seconds"
    )

    parser.add_argument(
        "--calibration",
        type=int,
        help="1 activates calibration"
    )

    parser.add_argument(
        "--interval",
        type=int,
        help="calibration_time"
    )

    parser.add_argument(
        "--numOD",
        type=int,
        help="Number of OD cultures"
    )

    args = parser.parse_args()

    dt = args.time_exp
    calibration_setting = args.calibration
    calib_dt = args.interval
    numOD = args.numOD

    if calibration_setting == 1:
        run_calibration(number_of_ODs=numOD, cdt = calib_dt)
    elif calibration_setting != 1:
        run_measurements(dt)






