import serial.tools.list_ports
import serial
list_of_ports = serial.tools.list_ports.comports()

for obj in list_of_ports:
    if obj.description.find('Actuator') == 0:
        actuator = obj.description[obj.description.find('COM'):-1]
    elif obj.description.find('Pump') == 0:
        pump = obj.description[obj.description.find('COM'):-1]
    elif obj.description.find('Sensors') == 0:
        sensors = obj.description[obj.description.find('COM'):-1]
    elif obj.description.find('Cycler') == 0:
        cycler = obj.description[obj.description.find('COM'):-1]
    elif obj.description.find('Cooler') == 0:
        cooler = obj.description[obj.description.find('COM'):-1]

