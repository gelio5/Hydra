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
from lib import ports
# import config

port = ports.sensors


def AskSensors():
    answer = ''
    msg = "STATUS\r\n".encode()
    print(msg)
    port.write(msg)
    answer = port.readline()
    print(answer)
    """if not askTimer.is_set():
        threading.Timer(10, AskSensors, [askTimer]).start()"""
    return
