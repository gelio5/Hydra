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

#port = serial.Serial(port='COM9',
 #                    baudrate=9600,
  #                   bytesize=serial.EIGHTBITS,
   #                  parity=serial.PARITY_NONE,
    #                 stopbits=serial.STOPBITS_ONE)


def AskSensors(askTimer):
    print('ТАНЦУЙ ТАЙМЕР РАБОТАЕТ')
    if not askTimer.is_set():
        threading.Timer(10, AskSensors, [askTimer]).start()
    return
