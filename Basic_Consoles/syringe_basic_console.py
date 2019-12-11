#! python
#
# noinspection PyPep8Naming
#
# This file is basic console application for communication with Valco
# Instruments Co. Inc. Universal Electric Actuator Models EUH, EUD, and EUT
# Firmware revisions EQ and subsequent with using all the features of this
# actuator

import serial   # pySerial API version 3.4
import time
import ports

syringe = serial.Serial(port=ports.pump,
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE)
syringe.isOpen()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')
while 1:
    # if msvcrt.kbhit():
    inp = input(">> ")
    if inp == 'exit':
        syringe.close()
        exit()
    else:
        syringe.write(str.encode("/1" + inp + '\r\n'))
        answer = ""
        time.sleep(2)
        while syringe.inWaiting() > 0:
            answer = syringe.readline()
        print(answer)
