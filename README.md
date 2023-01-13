<p align="center"><img src="images/vial_holder.png" alt="vial_holder" width="600"></p>


# OD_device_controls
This code is used to control an OD measuring device connected to a computer via a "ArduinoMega R3 Board 2560". The OD measuring device is used to measure the bacterial density of a batch culture that feeds a mother machine.

## Installation

To set this up you will need to connect your arduino to a serial port, names might change for windows/mac. For linux the port is typically: `/dev/ttyACM0` (could also be: `/dev/ttyACM1`). You may have to grant permission to this port:
```bash
sudo chmod a+rw /dev/ttyACM0
```
To use this script you will need to install PySerial, using:
```
python -m pip install pyserial
```

## Usage

### Calibration

In the beginning, a calibration of the optical density measuring unit will have to be performed. Ten bacterial cultures of varying OD need to be prepared (Best between OD 0 and 0.2).

To start the calibration enter the following commands:

1. Navigate to the OD_device_controls folder

```
cd ~/<path in between>/OD_device_controls
```

2. Start the calibration function

```
python3 hector_vial-script_V1.py --time_exp 100 --calibration 1 --interval 30 --numOD 10
```

`--time_exp` = Total experiment duration, at the moment it is always

`--required` = even though it is not needed by the calibration function.

`--calibration` = If set to 1, calibration is initiated.

`--interval` = Time each culture is measured during the calibration.

`--numOD` = Number of OD cultures for calibration.

3. The program will ask for the OD of the culture, then measure for the set duration. This will be done for all cultures. In the end the results are saved in the `calibration_file.csv`.

The calibration file has the following structure:

```
OD_values, mean_v, std_v
```
### Start the program

1. Navigate to the OD_device_controls folder

```
cd ~/<path in between>/OD_device_controls
```

2. Start

```
python3 hector_vial-script_V1.py --time_exp 1000
```

`--time_exp` = Experimental time in seconds
