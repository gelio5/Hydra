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
import time
import threading
import serial
import config

port = serial.Serial(port='COM14',
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)


def AskSensors():
    answer = ''
    msg = "STATUS\r\n".encode()
    print(msg)
    port.write(msg)
    print(1)
    time.sleep(30)
    print("sl")
    while port.inWaiting() > 0:
        answer += port.read(1).decode()
        print('p')
    print(answer)
    """if not askTimer.is_set():
        threading.Timer(10, AskSensors, [askTimer]).start()"""
    return
