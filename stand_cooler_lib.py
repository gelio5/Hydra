import serial
import config
from struct import *
import ctypes
from bitstring import BitArray

port = serial.Serial(port='COM14',
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=0.3)

address = 8


def IntToSumOfBytes(num):
    """
    Функция, которая вычесляет сумму байт числа для integer
    """
    a = bin(ctypes.c_uint.from_buffer(ctypes.c_int(num)).value)
    a = a[2:]
    aa = []
    if len(a) < 32:
        a = (32 - len(a)) * '0' + a
    for i in range(4):
        a1 = a[32 - 8 * (i + 1):32 - 8 * i]
        aa.append(BitArray(bin=a1).int)
    return sum(aa)


def FloatToSumOfBytes(num):
    """
    Функция, которая вычесляет сумму байт числа для float
    """
    a = bin(ctypes.c_uint.from_buffer(ctypes.c_float(num)).value)
    a = a[2:]
    aa = []
    if len(a) < 32:
        a = (32 - len(a)) * '0' + a
    for i in range(4):
        a1 = a[32 - 8 * (i + 1):32 - 8 * i]
        aa.append(BitArray(bin=a1).int)
    return sum(aa)


def GetStandState():
    length = 4
    command = 0xBD
    checkSum = address + length + command
    commandToSend = pack("<BBBB", address, length, command, checkSum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Stand: %s.' % commandToSend)
    answerBytes = port.read(20)
    answer = unpack("<BBBiiiBBBBB", answerBytes)
    config.logger.info(u'Recv Stand: %s' % answerBytes)
    if answer[0] + answer[1] + answer[2] + IntToSumOfBytes(answer[3]) + IntToSumOfBytes(answer[4]) + IntToSumOfBytes(answer[5]) + answer[6] + answer[7] + answer[8] + answer[9] != answer[10]:
        config.logger.error(u'Checksum did not match ')
        exit()
    else:
        return


def SetStandZero(attempt):
    if attempt < 50:
        length = 4
        command = 0xBC
        checkSum = address + length + command
        commandToSend = pack("<BBBB", address, length, command, checkSum)
        port.write(commandToSend)
        config.logger.info(u'Xmit Stand: %s.' % commandToSend)
        answerBytes = port.read(4)
        config.logger.info(u'Recv Stand: %s' % answerBytes)
        answer = unpack("<BBBB", answerBytes)
        if answer[0] == 8 and \
                answer[1] == 4 and \
                answer[2] == 0xBC and \
                answer[3] == 200:
            config.logger.info(u'Stand zero position is defined')
            return
        else:
            config.logger.warning(u'Stand zero position isn`t defined. Try '
                                  u'again')
            SetStandZero(attempt + 1)
    else:
        config.logger.error(u'Stand zero position can`t be defined.')
        exit()


def SetStandUp():
    length = 8
    command = 0xBB
    pos = int(1)
    checkSum = address + length + command + pos
    commandToSend = pack("<BBBiB", address, length, command, pos, checkSum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Stand: %s.' % commandToSend)
    answerBytes = port.read(4)
    config.logger.info(u'Recv Stand: %s' % answerBytes)
    answer = unpack("<BBBB", answerBytes)
    if answer[0] == 8 and \
            answer[1] == 4 and \
            answer[2] == 0xBB and \
            answer[3] == 199:
        config.logger.info(u'Sippers fall')
        return
    else:
        config.logger.error(u'Checksum did not match ')
        exit()


def SetStandDown():
    length = 8
    command = 0xBB
    pos = int(2)
    checkSum = address + length + command + pos
    commandToSend = pack("<BBBiB", address, length, command, pos, checkSum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Stand: %s.' % commandToSend)
    answerBytes = port.read(4)
    config.logger.info(u'Recv Stand: %s' % answerBytes)
    answer = unpack("<BBBB", answerBytes)
    if answer[0] + answer[1] + answer[2] == answer[3]:
        config.logger.error(u'Checksum')
        if answer[0] == 8 and \
                answer[1] == 4 and \
                answer[2] == 0xBB and \
                answer[3] == 199:
            config.logger.info(u'Sippers rise')
    else:
        config.logger.error(u'Message is corrupted')
    return
