#! python
# coding=utf-8
#
# noinspection PyPep8Naming
#
# This file is library for communication with Hamilton Company MICROLAB®
# Precision Syringe Drive/4 via using serial port
#
# Переменная port типа serial
# Переменная Rate(5-5800) типа int
# Переменная SyrPos(0-3000) типа int
# Переменная Volume(0-3000) типа int
# ValvePos('inpPos' - input, 'outPoss' - output, 'byPassPos' - bypass)

import time
import serial
import config


inpPos = 'h29045'
outPos = 'h29090'
byPassPos = 'h29135'

port = serial.Serial(port='COM9',
                     baudrate=9600,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)


def Initialization():
    """
    Функция инициализации насоса PSD/4 (вызывается в начале работы
     с устройством)
    """
    config.logger.info(u'Start Pump Initialization ')
    port.write(str.encode("/1" + 'h30001R' + '\r\n'))
    config.logger.info(u'Xmit Pump :%s' % '/1' + 'h30001R')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans)
    port.write(str.encode("/1" + 'h20000R' + '\r\n'))
    config.logger.info(u'Xmit Pump :%s' % '/1' + 'h20000R')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans)
    time.sleep(1)
    SetValvePos(outPos)
    time.sleep(1)
    port.write(str.encode("/1" + 'h10000R' + '\r\n'))
    config.logger.info(u'Xmit Pump :%s' % '/1' + 'h10000R')
    time.sleep(15)
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans)
    config.logger.info(u'End of initialization of pump')
    # port.reset_input_buffer()
    return


def Test():
    """
    Это функция тестирует Насос, рекомендуется вызывать после инициализации
    """
    config.logger.info(u'Start Pump test')
    error = 0
    if not Get255():
        error = error << 1
    if not CheckSum():
        error = error << 2
    if not FirmVersion():
        error = error << 3
    SetValveAbsoluteSyrPos(inpPos, 1000, 1000)
    if not AskSyrPos().find('1000'):
        error = error << 4
    if error == 0:
        SetValveAbsoluteSyrPos(inpPos, rate=1000, syrPos=0)
        config.logger.info(u'Test completed error - 0')
        return
    else:
        config.logger.info(u'Test completed error - ' + str(error))
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        exit()
        return


def AbsoluteSyrPos(rate, syrPos):
    """"
    Функция передвигает шприц в положение syrPos,
    используя rate в качестве скорости
    """
    if 5800 >= rate >= 5 and 0 <= syrPos <= 3000:
        port.write(str.encode('/1' + 'V' + str(rate) + 'R' + '\r\n'))
        config.logger.info(u'Xmit Pump: %s' % '/1' + 'V' + str(rate))
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        port.write(str.encode("/1" + 'V' + str(rate) + 'A' + str(syrPos) +
                              'R' + '\r\n'))
        config.logger.info(u'Xmit Pump: %s' % "/1" + 'V' + str(rate) + 'A' +
                           str(syrPos) + 'R')
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        Status(0)
    else:
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        exit()
        return


def Aspirate(valvePos, rate, volume):
    """
    Функция устанавливает положение коммутатора,
    передвигает шприц со скоростью Rate
    на Volume колличество шагов вверх
    """
    if 5800 >= rate >= 5 and 0 <= volume <= 3000:
        port.write(str.encode('/1' + 'V' + str(rate) + 'R' + '\r\n'))
        config.logger.info(u'Xmit Pump: %s' % '/1' + 'V' + str(rate))
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        port.write(str.encode(
            "/1" + valvePos + 'P' + str(volume) + 'V' + str(rate) +
            'R' + '\r\n'))
        config.logger.info(
         u'Xmit Pump: %s' % "/1" + valvePos + 'P' + str(volume) + 'V' +
            str(rate) + 'R')
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        Status(0)
    else:
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        exit()
    return


def SyrSetAbsoluteZero(valvePos, rate):
    """
    Эта функция помещает коммутатор в пололожение valvePos,
    и полностью опорожняет шприц со скоростью rate
    """
    if 5800>= rate >= 5:
        port.write(str.encode('/1' + 'V' + str(rate) + 'R' + '\r\n'))
        config.logger.info(u'Xmit Pump: %s' % '/1' + 'V' + str(rate))
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        port.write(str.encode(
            "/1" + valvePos + 'A0' + 'V' + str(rate) + 'R' + '\r\n'))
        config.logger.info(u'Xmit Pump: %s' % "/1" + valvePos + 'A0V' +
                           str(rate) + 'R')
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        Status(0)
    else:
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        exit()
    return


def SetValveAbsoluteSyrPos(valvePos, rate, syrPos):
    """
    Функция устанавливает коммутатор в положение valvePos,
    после устанавливает шприц в положение syrPos со скоростью rate
    """
    if 5800>= rate >=5 and 3000>= syrPos >=0:
        port.write(str.encode('/1' + 'V' + str(rate) + 'R' + '\r\n'))
        config.logger.info(u'Xmit Pump: %s' % '/1' + 'V' + str(rate))
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        port.write(str.encode("/1" + valvePos + 'V' + str(rate) + 'A' +
                              str(syrPos) + 'R' + '\r\n'))
        config.logger.info(u'Xmit Pump: %s' % "/1" + valvePos + 'V' +
                           str(rate) + 'A' + str(syrPos) + 'R')
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        Status(0)
    else:
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        exit()
    return


def SetValvePos(valvePos):
    """
    Функция устанавливает коммутатор в положение valvePos
    """
    port.write(str.encode("/1" + valvePos + 'R' + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % "/1" + valvePos + 'R')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans[0:-1])
    Status(0)
    return


def AskSyrPos():
    """
    Функция возвращает текущее положение шприца
    """
    port.write(str.encode("/1" + '?' + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % "/1" + '?')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans[0:-1])
    return ans


def AskValvePos():
    """
    Функция возвращает текущее положение коммутатора
    """
    port.write(str.encode("/1" + '?25000' + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % "/1" + '?25000')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans[0:-1])
    return ans


def Status(i):
    """
    Функция возвращает текущий статус насоса
    """
    if i <= 100:
        i += 1
        port.write(str.encode("/1" + 'Q' + '\r\n'))
        config.logger.info(u'Xmit Pump: %s' % "/1" + 'Q')
        ans = str(port.readline())
        config.logger.info(u'Recv Pump :%s' % ans[0:-1])
        if ans[4] == '`':
            config.logger.info(u'Pump is ready')
            return
        elif ans[4] == '@':
            time.sleep(0.5)
            Status(i)
            return
        else:
            config.logger.info(u'ERROR - %s' % ans[4])
            return
    else:
        config.logger.info(u'Delay time exceeded')
# Функции, описанные ниже нужны для проведения Теста


def Get255():
    """
    Функция возвращает 255
    """
    port.write(str.encode('/1' + '?22' + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % "/1" + '?22')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans[0:-1])
    if ans.find('255') == -1:
        ans = False
    else:
        ans = True
    return ans


def CheckSum():
    """
    Функция возвращает Check Sum
    """
    port.write(str.encode('/1' + '#' + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % "/1" + '#')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans[0:-1])
    if ans.find('E882') == -1:
        ans = False
    else:
        ans = True
    return ans


def FirmVersion():
    """
    Функция возвращает Firm Version
    """
    port.write(str.encode('/1' + '&' + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % "/1" + '&')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans[0:-1])
    if ans.find('DV01.32.0A 58269-02') == -1:
        return False
    else:
        return True
