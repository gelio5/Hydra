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

actuator = serial.Serial(port='COM4',
                         baudrate=115200,
                         bytesize=serial.EIGHTBITS,
                         parity=serial.PARITY_NONE,
                         stopbits=serial.STOPBITS_ONE)
actuator.isOpen()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')
while 1:
    # if msvcrt.kbhit():
    inp = input(">> ")
    if inp == 'exit':
        actuator.close()
        exit()
    else:
        if inp.find('AL') != -1 or inp.find('CC') != -1 \
                or inp.find('CW') != -1 or inp.find('GO') != -1\
                or inp.find('HM') != -1 or inp.find('IFM') != -1 \
                or inp.find('LG') != -1 or inp.find('LRN') != -1\
                or inp.find('SB') != -1 or inp.find('TO') != -1 \
                or inp.find('TT') != -1:
            actuator.write(str.encode(inp + '\r\n'))
        elif inp.find('CP') != -1 or inp.find('AM') != -1 \
                or inp.find('CNT') != -1 or inp.find('DT') != -1\
                or inp.find('NP') != -1 or inp.find('SM') != -1 \
                or inp.find('SO') != -1 or inp.find('STAT') != -1\
                or inp.find('TM') != -1 or inp.find('VR') != -1:
            actuator.write(str.encode(inp + '\r\n'))
            out = ''
            answer = ''
            # let wait reading output (let give device time
            # to answer)
            while actuator.in_waiting == 0:
                time.sleep(0.001)
            while actuator.inWaiting() > 0:
                out = actuator.read(1).decode()
                answer += out
            print(answer)
        elif inp.find("/?") != -1:
            actuator.write(str.encode(inp + '\r\n'))
            out = ''
            answer = ''
            # let wait 0.1 second before reading output (let give device time
            # to answer)
            time.sleep(0.1)
            while actuator.inWaiting() > 0:
                out = actuator.read(1).decode()
                answer += out
            print(answer)
        else:
            print("Unknown command")
