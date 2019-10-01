import serial.tools.list_ports
import serial
list_of_ports = serial.tools.list_ports.comports()

for obj in list_of_ports:
    if obj.serial_number == 'AC2A':
        actuator = obj.device
    elif obj.serial_number == '9411':
        pump = obj.device
    elif obj.serial_number == '5395':
        sensors = obj.device
    elif obj.serial_number == 'C7C1':
        cycler = obj.device
    elif obj.serial_number == 'C001':
        cooler = obj.device

