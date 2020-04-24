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
import sys
import time
import serial
import ports
import config

inpPos = 'h29180'
outPos = 'h29090'
byPassPos = 'h29135'

port = serial.Serial(port=ports.pump,
                     baudrate=9600,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)
port.close()


def Transceiver(command: str):
    """
    Функция посылает команду на Насос и принимает ответ
    """
    try:
        port.open()
    except Exception:
        time.sleep(0.1)
        port.open()
    port.write(str.encode(command + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % command)
    answer = port.readline().decode()
    config.logger.info(u'Recv Pump: %s' % answer)
    port.close()
    return answer


def Initialization():
    """
    Функция инициализации насоса PSD/4 (вызывается в начале работы
     с устройством)
    """
    config.logger.info(u'Start Pump Initialization ')
    Transceiver("/1" + 'h30001R')
    Transceiver("/1" + 'h20000R')
    time.sleep(1)
    SetValvePos(outPos)
    time.sleep(1)
    Transceiver("/1" + 'h10000R')
    Status(0)
    time.sleep(15)
    config.logger.info(u'End of initialization of pump')
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
    SetValveAbsoluteSyrPos(byPassPos, 1000, 3000)
    time.sleep(15)
    if not AskSyrPos().find('1000'):
        error = error << 4
    if error == 0:
        SetValveAbsoluteSyrPos(outPos, rate=1000, syrPos=0)
        config.logger.info(u'Test completed error - 0')
        return error
    else:
        config.logger.info(u'Test completed error - ' + str(error))
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        return error


def AbsoluteSyrPos(rate: int, syrPos: int):
    """"
    Функция передвигает шприц в положение syrPos,
    используя rate в качестве скорости
    """
    if 5800 >= rate >= 5 and 0 <= syrPos <= 3000:
        Transceiver("/1" + 'V' + str(rate) + 'A' + str(syrPos) + 'R')
        Status(0)
        port.close()
    else:
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        exit()
        return


def Aspirate(valvePos: str, rate: int, volume: int):
    """
    Функция устанавливает положение коммутатора,
    передвигает шприц со скоростью Rate
    на Volume колличество шагов вверх
    """
    if 5800 >= rate >= 5 and 0 <= volume <= 3000:
        Transceiver(
            "/1" + valvePos + 'V' + str(rate) + 'P' + str(volume) + 'R')
        Status(0)
    else:
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        exit()
    return


def SyrSetAbsoluteZero(valvePos: str, rate: int):
    """
    Эта функция помещает коммутатор в пололожение valvePos,
    и полностью опорожняет шприц со скоростью rate
    """
    if 5800 >= rate >= 5:
        Transceiver("/1" + 'V' + str(rate) + valvePos + 'A0' + 'R')
        Status(0)
        port.close()
        return
    else:
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        exit(1)


def SetValveAbsoluteSyrPos(valvePos: str, rate: int, syrPos: int):
    """
    Функция устанавливает коммутатор в положение valvePos,
    после устанавливает шприц в положение syrPos со скоростью rate
    """
    if 5800 >= rate >= 5 and 3000 >= syrPos >= 0:
        Transceiver(
            '/1' + valvePos + 'V' + str(rate) + 'A' + str(syrPos) + 'R')
        Status(0)
    else:
        config.logger.info(
            u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
            u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        port.close()
        exit()
    return


def SetValvePos(valvePos: str):
    """
    Функция устанавливает коммутатор в положение valvePos
    """
    Transceiver('/1' + valvePos + 'R')
    Status(0)
    return


def AskSyrPos():
    """
    Функция возвращает текущее положение шприца
    """
    port.open()
    port.write(str.encode("/1" + '?' + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % "/1" + '?')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans[0:-1])
    port.close()
    # ans = Transceiver('/1' + '?')
    return ans


def AskValvePos():
    """
    Функция возвращает текущее положение коммутатора
    """
    port.close()
    port.write(str.encode("/1" + '?25000' + '\r\n'))
    config.logger.info(u'Xmit Pump: %s' % "/1" + '?25000')
    ans = str(port.readline())
    config.logger.info(u'Recv Pump :%s' % ans[0:-1])
    port.close()
    #return Transceiver('/1' + '?25000')
    return ans


def Status(i: int):
    """
    Функция возвращает текущий статус насоса.
    Функция является рекурсивной и
    выполняет роль функции ожидания конца работы.
    Вызывается в каждой функции, связанной с
    перемещением коммутатора или шприца.
    Параметр i - необходим, для исключения бесконечной рекурсии в случае ошибки
    Желательно задавать его равным 0
    """
    n = 0
    if i <= 100:
        i += 1
        ans = Transceiver('/1' + 'Q')
        if ans[2] == '`':
            config.logger.info(u'Pump is ready')
            return
        elif ans[2] == '@':
            time.sleep(0.5)
            Status(i)
            return
        else:
            if n != 5:
                time.sleep(0.5)
                Status(i)
                config.logger.info(u'OSHIBKA ALARM!!!!!!!!!!!!!')
                n += 1
            else:
                config.logger.info(u'ERROR - %s' % ans)
                return
    else:
        config.logger.info(u'Delay time exceeded')


# Функции, описанные ниже нужны для проведения Теста


def Get255() -> bool:
    """
    Функция возвращает 255
    """
    return Transceiver('/1' + '?22').find('255') != -1


def CheckSum() -> bool:
    """
    Функция возвращает Check Sum
    """
    return Transceiver('/1' + '#').find('E882') != -1


def FirmVersion() -> bool:
    """
    Функция возвращает Firm Version
    """
    return Transceiver('/1' + '&').find('E882') != -1


if len(sys.argv) > 1:
    if sys.argv[1] == 'init':
        Initialization()
        Test()
    elif sys.argv[1] == 'test':
        Test()
