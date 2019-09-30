#! python
# coding=utf-8
#
# noinspection PyPep8Naming
#
# Данная библиотека описывает функции для платы со следующими датчиками:
# Датчик емкости буфера, наличия емкости слива, переполнения емкости слива,
# потока, два датчика пузырьков, оптопара поднятия трубок буфера и слива,
# датчик закрытия,
# двери, датчик наличия заземления,
# import time
# import threading
import serial
from lib import ports, stand_cooler_lib
# import config

port = serial.Serial(port=ports.sensors,
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)


def AskSensors():
    msg = "STATUS\r\n".encode()
    port.write(msg)
    answer = port.readline().decode()
    print(stand_cooler_lib.GetCoolerData())
    sensors_value = open('sensors_value.txt', 'w')
    sensors_value.write(str(answer[0:]))
    sensors_value.close()

    """if not askTimer.is_set():
        threading.Timer(10, AskSensors, [askTimer]).start()"""
    return


def CheckSensors():
    sensors_file = open('sensors_value.txt', 'r')
    sensors_value = sensors_file.read()
    sensors_file.close()
    if sensors_value.find('STATUS DB-0 BB-0 GND-1 DC-1 DO-1 TP-1') != -1:
        status = True
    else:
        status = False
    print(status)
    return status
