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