import serial
from lib import config, ports
from struct import *
from lib.types_to_sum_of_bytes import *

port = ports.cooler
address = 8


def GetStandState():
    length = 4
    command = 0xBD
    checkSum = address + length + command
    commandToSend = pack("<BBBB", address, length, command, checkSum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Stand: %s.' % commandToSend)
    answerBytes = port.read(20)
    answer: tuple = unpack("<BBBiiiBBBBB", answerBytes)
    config.logger.info(u'Recv Stand: %s' % answerBytes)
    if (answer[0] +
        answer[1] +
        answer[2] +
        IntToSumOfBytes(answer[3]) +
        IntToSumOfBytes(answer[4]) +
        IntToSumOfBytes(answer[5]) +
        answer[6] +
        answer[7] +
        answer[8] +
        answer[9]) % \
            256 != answer[10]:
        config.logger.error(u'Message is corrupted')
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
        config.logger.error(u'Message is corrupted')
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


def GetCoolerData():
    length = 4
    command = 0x93
    checksum = address + length + command
    commandToSend = pack("<BBBB", address, length, command, checksum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Cooler %s.' % commandToSend)
    answerBytes = port.read(18)
    config.logger.info(u'Recv Cooler: %s' % answerBytes)
    answer = unpack("<BBBfffBBB", answerBytes)
    if (answer[0] +
        answer[1] +
        answer[2] +
        FloatToSumOfBytes(answer[3]) +
        FloatToSumOfBytes(answer[4]) +
        FloatToSumOfBytes(answer[5]) +
        answer[6] +
        answer[7]) % \
            256 != answer[8]:
        config.logger.error(u'Message is corrupted')
        exit()
    else:
        print(answer)
        return


def SetCoolerTemp(temp: float):
    temp = float(temp)
    length = 8
    command = 0x91
    checksum = (address + length + command + FloatToSumOfBytes(temp)) % 256
    commandToSend = pack("<BBBfB", address, length, command, temp, checksum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Cooler %s.' % commandToSend)
    answerBytes = port.read(4)
    config.logger.info(u'Recv Cooler: %s' % answerBytes)
    answer = unpack("<BBBB", answerBytes)
    if answer[3] != 0x9D:
        config.logger.error(u'Answer message is corrupted')
        exit()
    else:
        config.logger.info(u'Cooler going to %s' % temp)
    return


def StopCoolerControl():
    length = 4
    command = 0x41
    checksum = address + length + command
    commandToSend = pack("<BBBB", address, length, command, checksum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Cooler: %s' % commandToSend)
    answerBytes = port.read(4)
    config.logger.info(u'Recv Cooler: %s' % answerBytes)
    if answerBytes != commandToSend:
        config.logger.error(u'Answer message is corrupted')
        exit()
    else:
        config.logger.info(u'Cooler control is stop')
    return
