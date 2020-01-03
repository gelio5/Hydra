import serial, sys
import ports
import config
from struct import *
from types_to_sum_of_bytes import *
import time

port = serial.Serial(port=ports.cooler,
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=0.3)
address = 8
port.close()


def Transceiver(command, length: int, *others):
    try:
        port.open()
    except Exception:
        time.sleep(0.01)
        port.open()
    n = 0
    checksum = (address + length + command)
    commandToSend = pack('<BBB', address, length, command)
    for i in others:
        if i == int:
            i = i
            checksum += i
            commandToSend += pack('<i', i)
        elif i == float:
            n += 1
            i = FloatToSumOfBytes(i)
            checksum += i
            commandToSend += pack('<f', i)
    if n != 0:
        checksum = checksum % 256
    commandToSend += pack('<B', checksum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Cooler: %s' % commandToSend)
    return commandToSend


def GetStandState():
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.01)
    #    port.open()
    #length = 4
    #command = 0xBD
    #checkSum = address + length + command
    #commandToSend = pack("<BBBB", address, length, command, checkSum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Stand: %s.' % commandToSend)
    Transceiver(0xBD, 4)
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
        port.close()
        answer = GetStandState()
        return answer
    else:
        port.close()
        return answer


def SetStandZero(attempt):
    if attempt < 50:
        #length = 4
        #command = 0xBC
        #checkSum = address + length + command
        #commandToSend = pack("<BBBB", address, length, command, checkSum)
        #port.write(commandToSend)
        #config.logger.info(u'Xmit Stand: %s.' % commandToSend)
        Transceiver(0xBC,4)
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
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.01)
    #    port.open()
    #length = 8
    #command = 0xBB
    pos = int(1)
    #checkSum = address + length + command + pos
    #commandToSend = pack("<BBBiB", address, length, command, pos, checkSum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Stand: %s.' % commandToSend)
    Transceiver(0xBB, 8, pos)
    answerBytes = port.read(4)
    port.close()
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
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.01)
    #    port.open()
    #length = 8
    #command = 0xBB
    pos = int(2)
    #checkSum = address + length + command + pos
    #commandToSend = pack("<BBBiB", address, length, command, pos, checkSum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Stand: %s.' % commandToSend)
    Transceiver(0xBB, 8, pos)
    answerBytes = port.read(4)
    port.close()
    config.logger.info(u'Recv Stand: %s' % answerBytes)
    answer = unpack("<BBBB", answerBytes)
    if answer[0] + answer[1] + answer[2] == answer[3]:
        config.logger.error(u'Checksum')
        if answer[0] == 8 and \
                answer[1] == 4 and \
                answer[2] == 0xBB and \
                answer[3] == 199:
            config.logger.info(u'Sippers rise')
            port.close()
    else:
        port.close()
        SetStandDown()
    return


def GetCoolerData():
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.01)
    #    port.open()
    #length = 4
    #command = 0x93
    #checksum = address + length + command
    #commandToSend = pack("<BBBB", address, length, command, checksum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Cooler %s.' % commandToSend)
    Transceiver(0x93, 4)
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
        port.close()
        answer = GetCoolerData()
        return answer
    else:
        port.close()
        return answer


def SetCoolerTemp(temp: float):
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.01)
    #    port.open()
    temp = float(temp)
    #length = 8
    #command = 0x91
    #checksum = (address + length + command + FloatToSumOfBytes(temp)) % 256
    #commandToSend = pack("<BBBfB", address, length, command, temp, checksum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Cooler %s.' % commandToSend)
    Transceiver(0x91, 8, temp)
    answerBytes = port.read(4)
    config.logger.info(u'Recv Cooler: %s' % answerBytes)
    answer = unpack("<BBBB", answerBytes)
    if answer[3] != 0x9D:
        config.logger.error(u'Answer message is corrupted')
        port.close()
        SetCoolerTemp(temp)
    else:
        config.logger.info(u'Cooler going to %s' % temp)
        port.close()
    return


def StopCoolerControl():
    try:
        port.open()
    except Exception:
        time.sleep(0.01)
        port.open()
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
        port.close()
        StopCoolerControl()
    else:
        config.logger.info(u'Cooler control is stop')
        port.close()
    return


if len(sys.argv) > 1:
    if sys.argv[1] == 'up':
        SetStandDown()
    elif sys.argv[1] == 'down':
        SetStandUp()
