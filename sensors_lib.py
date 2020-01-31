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
import stand_cooler_lib
import ports
import thermal_cycler_lib
import types_to_sum_of_bytes as fop
import time
import os

# import redis
# import config
port = serial.Serial(port=ports.sensors,
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)
port.close()

root_dir = os.path.abspath(os.path.dirname(__file__))
ch = root_dir + "/../data/"


def AskSensors():
    try:
        port.open()
    except Exception:
        time.sleep(0.01)
        try:
            port.open()
        except Exception:
            time.sleep(0.01)
            try:
                port.open()
            except Exception:
                time.sleep(0.01)
                try:
                    port.open()
                except Exception:
                    time.sleep(0.01)
                    port.open()
    msg = "STATUS\r\n".encode()
    port.write(msg)
    answer = port.readline().decode()[7:-3]
    if answer.find('UNDEFINED') != -1:
        port.write(msg)
        answer = port.readline().decode()[7:]
    port.close()
    dataFromStand = stand_cooler_lib.GetStandState()
    dataFromCooler = stand_cooler_lib.GetCoolerData()
    dataFromCycler = thermal_cycler_lib.GetThermalCyclerData()
    sP = ' SP=' + str(dataFromStand[4])
    hP = ' HP=' + str(int((dataFromStand[6] & 8) / 8))
    tS = ' TS=' + fop.ToFixed(dataFromCooler[3], 1)
    tC = ' TC=' + fop.ToFixed(dataFromCycler[3], 1)
    cC = ' CC=0'
    bU = ' BU=0'
    cD = ' CD=' + str(int((dataFromStand[6] & 16) / 16))
    lD = ' LD=1'
    tR = ' TR=' + str(int((dataFromCycler[6] & 128) / 128))
    answer += sP + hP + tS + tC + cC + bU + cD + lD + tR
    # r = redis.StrictRedis(host='localhost', port=6379, db=1)
    # r.set('sensors',dict(item.split("=") for item in answer.split(" ")))
    """if not askTimer.is_set():
        threading.Timer(10, AskSensors, [askTimer]).start()"""
    return answer


# TODO: нужна ли функция CheckSensors?!

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


def BubOn():
    try:
        port.open()
    except Exception:
        time.sleep(0.01)
        try:
            port.open()
        except Exception:
            time.sleep(0.01)
            try:
                port.open()
            except Exception:
                time.sleep(0.01)
                try:
                    port.open()
                except Exception:
                    time.sleep(0.01)
                    port.open()
    msg = "BUBON\r\n".encode()
    port.write(msg)
    answer = port.readline().decode()  # [7:-3]
    if answer.find('UNDEFINED') != -1:
        port.write(msg)
        answer = port.readline().decode()  # [7:]
    port.close()
    print(answer)


def BubAsk():
    try:
        port.open()
    except Exception:
        time.sleep(0.01)
        try:
            port.open()
        except Exception:
            time.sleep(0.01)
            try:
                port.open()
            except Exception:
                time.sleep(0.01)
                try:
                    port.open()
                except Exception:
                    time.sleep(0.01)
                    port.open()
    msg = "BUBCOUNT\r\n".encode()
    port.write(msg)
    answer = port.readline().decode()  # [7:-3]
    if answer.find('UNDEFINED') != -1:
        port.write(msg)
        answer = port.readline().decode()  # [7:]
    port.close()
    print(answer)


def BubOff():
    try:
        port.open()
    except Exception:
        time.sleep(0.01)
        try:
            port.open()
        except Exception:
            time.sleep(0.01)
            try:
                port.open()
            except Exception:
                time.sleep(0.01)
                try:
                    port.open()
                except Exception:
                    time.sleep(0.01)
                    port.open()
    msg = "BUBOFF\r\n".encode()
    port.write(msg)
    answer = port.readline().decode()  # [7:-3]
    if answer.find('UNDEFINED') != -1:
        port.write(msg)
        answer = port.readline().decode()  # [7:]
    port.close()
    print(answer)
