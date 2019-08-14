#! python
# -*- coding: utf-8 -*-
# noinspection PyPep8Naming
#
# This file is library for communication with Valco Instruments Co. Inc.
# Universal Electric Actuator
# Models EUH, EUD, and EUT
# Firmware revisions EQ and subsequent

import time
import serial
import config


port = serial.Serial(port='COM4',
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)


def Transceiver(command):
    """ Sends a command to the selected COM port and return answer from
    actuator """
    port.write(str.encode(command + '\r\n'))
    config.logger.info(u'Xmit Actuator: %s.' % command)
    answer = ''
    while port.in_waiting == 0:
        time.sleep(0.1)
    while port.inWaiting() > 0:
        answer += port.read(1).decode()
    config.logger.info(u'Recv Actuator: %s.' % answer[0:-1])
    return answer


def Transmitter(command):
    """ Sends a command to the selected COM port without waiting for a
    response """
    port.write(str.encode(command + '\r\n'))
    config.logger.info(u'Xmit Actuator: %s.' % command)


def Test():
    config.logger.info(u'Start testing of actuator.')
    ini_test = 0
    if not TogglePos(1):
        ini_test += 1
        config.logger.error(u'1')
    if not TogglePos(13):
        ini_test += 2
        config.logger.error(u'2')
    if MovingTime() > 1800:
        ini_test += 4
        config.logger.error(u'4')
    if not TogglePos(20):
        ini_test += 8
        config.logger.error(u'8')
    TogglePos(positionNumber=24)
    config.logger.info(u'Test is ended. ERROR STATUS: %s.' % ini_test)
    return


def GoToPosition(positionNumber):
    config.logger.info(u'Going to position %s.' % positionNumber)
    Transmitter("GO"+str(positionNumber))


def CurrentPos():
    config.logger.info(u'Interrogating the position of the actuator.')
    return int(Transceiver("CP").replace("CP", "").replace("\r", ""))


def MovingTime():
    config.logger.info(u'Interrogation of the time spent on the previous '
                       u'switch.')
    return int(Transceiver("TM").replace("TM", "").replace("\r", ""))


def TogglePos(positionNumber):
    config.logger.info(u'##### Moving the check switch. #####')
    GoToPosition(positionNumber)
    if positionNumber == CurrentPos():
        config.logger.info(u'##### The switch was successful. #####')
        return True
    else:
        config.logger.info(u'##### Switching was not successful. #####')
        return False
