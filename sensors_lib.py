#! python
# coding=utf-8
#
# noinspection PyPep8Naming
#
# This file is library for communication with Hamilton Company MICROLAB®
# Precision Syringe Drive/4 via using serial port
#
# Данная библиотека описывает функции для платы со следующими датчиками:
# Датчик емкости буфера, наличия емкости слива, переполнения емкости слива,
# потока, два датчика пузырьков, оптопара поднятия трубок буфера и слива,
# датчик закрытия,
# двери, датчик наличия заземления,
import time
import threading
import config

port = serial.Serial(port='COM14',
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)


def AskSensors(askTimer):
    """
    Функция опрашивает датчики раз в 10 секунд
    """
    port.write(str.encode("S"))
    ans = str(port.readline())
    config.logger.info(u'Sensors Status:%s' %ans)
    print(port.readline())
    config.logger.info(u'Port for communication with actuator is closed.')
    if not askTimer.is_set():
        threading.Timer(10, AskSensors, [askTimer]).start()
        # Первое число в скобках - таймер опроса датчиков
    return


