#! python
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
import logging

logging.basicConfig(format=u'%(asctime)s  %(levelname)-8s  %(funcName)-24s '
                           u'%(message)s',
                    level=logging.DEBUG,
                    filename=u'hydra.log')

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
    logging.info(u'Start Pump Initialization ')
    port.write(str.encode("/1" + 'h30001R' + '\r\n'))
    logging.info(u'Xmit Pump :%s' % '/1' + 'h30001R')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans)
    port.write(str.encode("/1" + 'h10000R' + '\r\n'))
    logging.info(u'Xmit Pump :%s' % '/1' + 'h10000R')
    time.sleep(0.001)
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans)
    port.write(str.encode("/1" + 'h20000R' + '\r\n'))
    logging.info(u'Xmit Pump :%s' % '/1' + 'h20000R')
    time.sleep(15)
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans)
    logging.info(u'End of initialization of pump')
    # port.reset_input_buffer()
    return


def Test():
    """
    This function tests the Pump, have to be called after Pump Initialization
    """
    logging.info(u'Start Pump test')
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
        logging.info(u'Test completed error - 0')
        return
    else:
        logging.info(u'Test completed error - ' + str(error))
        return


def AbsoluteSyrPos(Rate, SyrPos):
    """"
    This function places syringe to the SyrPos using Rate as velocity parameter
    """
    if 5800 >= Rate >= 5 and 0 <= SyrPos <= 3000:
        port.write(str.encode("/1" + 'V' + Rate + 'A' + SyrPos + 'R' + '\r\n'))
        time.sleep(8)
        logging.info(u'Xmit Pump: %s' % "/1" + 'V' + Rate + 'A' + SyrPos + 'R')
        ans = str(port.readline())
        logging.info(u'Recv Pump :%s' % ans[0:-1])
    else:
        return 'Wrong parameters'


def Aspirate(valvePos, rate, volume):
    """
    Функция устанавливает положение коммутатора,
    передвигает шприц со скоростью Rate
    на Volume колличество шагов вверх
    """
    port.write(str.encode(
        "/1" + valvePos + 'P' + str(volume) + 'V' + str(rate) + 'R' + '\r\n'))
    time.sleep(15)
    logging.info(
        u'Xmit Pump: %s' % "/1" + valvePos + 'P' + str(volume) + 'V' +
        str(rate) + 'R')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    return


def SyrSetAbsoluteZero(valvePos, rate):
    """
    This function sets commutator to output position and syringe to the
    absolute zero position
    """
    port.write(str.encode(
        "/1" + valvePos + 'A0' + 'V' + str(rate) + 'R' + '\r\n'))
    time.sleep(8)
    logging.info(u'Xmit Pump: %s' % "/1" + valvePos + 'A0V' + str(rate) + 'R')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    return


def SetValveAbsoluteSyrPos(valvePos, rate, syrPos):
    """
    This function moves commutator to the valvePos,
    then moves syringe to the syrPos with Rate as velocity
    """
    port.write(str.encode("/1" + valvePos + 'V' + str(rate) + 'A' +
                          str(syrPos) + 'R' + '\r\n'))
    logging.info(u'Xmit Pump: %s' % "/1" + valvePos + 'V' + str(rate) + 'A' +
                 str(syrPos) + 'R')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    time.sleep(8)
    logging.info(u'Sleep 8s is ended.')
    return


def SetValvePos(valvePos):
    """
    This function moves Valve to the ValvePos
    """
    port.write(str.encode("/1" + valvePos + 'R' + '\r\n'))
    time.sleep(0.5)
    logging.info(u'Xmit Pump: %s' % "/1" + valvePos + 'R')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    return


def AskSyrPos():
    """
    This function returns current syringe position
    """
    port.write(str.encode("/1" + '?' + '\r\n'))
    time.sleep(2)
    logging.info(u'Xmit Pump: %s' % "/1" + '?')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    return ans


def AskValvePos():
    """
    This function returns current valve position
    """
    port.write(str.encode("/1" + '?25000' + '\r\n'))
    time.sleep(2)
    logging.info(u'Xmit Pump: %s' % "/1" + '?25000')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    return ans


def Status():
    """
    This function returns current Pump Status
    """
    port.write(str.encode("/1" + 'Q' + '\r\n'))
    logging.info(u'Xmit Pump: %s' % "/1" + 'Q')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    return ()


# Functions described below are needed for the Pump Test, after initialization


def Get255():
    """
    This function returns 255
    """
    port.write(str.encode('/1' + '?22' + '\r\n'))
    logging.info(u'Xmit Pump: %s' % "/1" + '?22')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    if ans.find('255') == -1:
        ans = False
    else:
        ans = True
    return ans


def CheckSum():
    """
    This function returns Check Sum
    """
    port.write(str.encode('/1' + '#' + '\r\n'))
    logging.info(u'Xmit Pump: %s' % "/1" + '#')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    if ans.find('E882') == -1:
        ans = False
    else:
        ans = True
    return ans


def FirmVersion():
    """
    This function returns Firm Version
    """
    port.write(str.encode('/1' + '&' + '\r\n'))
    logging.info(u'Xmit Pump: %s' % "/1" + '&')
    ans = str(port.readline())
    logging.info(u'Recv Pump :%s' % ans[0:-1])
    if ans.find('DV01.32.0A 58269-02') == -1:
        return False
    else:
        return True
