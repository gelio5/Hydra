import serial.tools.list_ports
import serial
list_of_ports = serial.tools.list_ports.comports()
for obj in list_of_ports:
    if obj.description.find('Actuator') == 0:
        actuator = serial.Serial(port=obj.description[obj.description.find('COM'):-1],
                                 baudrate=115200,
                                 bytesize=serial.EIGHTBITS,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE)
    elif obj.description.find('Pump') == 0:
        pump = serial.Serial(port=obj.description[obj.description.find('COM'):-1],
                             baudrate=9600,
                             bytesize=serial.EIGHTBITS,
                             parity=serial.PARITY_NONE,
                             stopbits=serial.STOPBITS_ONE)
    elif obj.description.find('Sensors') == 0:
        sensors = serial.Serial(port=obj.description[obj.description.find('COM'):-1],
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE)
    elif obj.description.find('Cycler') == 0:
        cycler = serial.Serial(port=obj.description[obj.description.find('COM'):-1],
                               baudrate=115200,
                               bytesize=serial.EIGHTBITS,
                               parity=serial.PARITY_NONE,
                               stopbits=serial.STOPBITS_ONE,
                               timeout=0.3)
    elif obj.description.find('Cooler') == 0:
        cooler = serial.Serial(port=obj.description[obj.description.find('COM'):-1],
                               baudrate=115200,
                               bytesize=serial.EIGHTBITS,
                               parity=serial.PARITY_NONE,
                               stopbits=serial.STOPBITS_ONE,
                               timeout=0.3)
