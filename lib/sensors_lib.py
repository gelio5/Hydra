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
from lib import ports, stand_cooler_lib, types_to_sum_of_bytes as fop, thermal_cycler_lib
# import config
port = serial.Serial(port=ports.sensors,
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)


def AskSensors():
    msg = "STATUS\r\n".encode()
    port.write(msg)
    answer = port.readline().decode()[7:-3]
    if answer.find('UNDEFINED') != -1:
        port.write(msg)
        answer = port.readline().decode()[7:]
    dataFromStand = stand_cooler_lib.GetStandState()
    dataFromCooler = stand_cooler_lib.GetCoolerData()
    dataFromCycler = thermal_cycler_lib.GetThermalCyclerData()
    sP = ' SP=' + str(dataFromStand[4])
    hP = ' HP=' + str(int((dataFromStand[6] & 8) / 8))
    tS = ' TS=' + fop.ToFixed(dataFromCooler[4], 2)
    tC = ' TC=' + fop.ToFixed(dataFromCycler[4], 2)
    cC = ' CC=0'
    bU = ' BU=0'
    cD = ' CD=0'
    lD = ' LD=0'
    answer += sP + hP + tS + tC + cC + bU
    sensors_value = open('sensors_value.txt', 'w')
    sensors_value.write(answer)
    sensors_value.close()

    """if not askTimer.is_set():
        threading.Timer(10, AskSensors, [askTimer]).start()"""
    return


def CheckSensors():
    sensors_file = open('sensors_value.txt', 'r')
    sensors_value = sensors_file.read()
    sensors_file.close()
    if sensors_value.find('DB=0 BB=0 GND=1 DC=1 DO=1 TP=1') != -1:
        status = True
    else:
        status = False
    print(status)
    return status
