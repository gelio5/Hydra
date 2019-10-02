from lib import config, ports
import serial
from lib.types_to_sum_of_bytes import *
from struct import *

port = serial.Serial(port=ports.cycler,
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=0.3)
address = 8


def SetThermalCyclerTemp(temp: float):
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


def StopThermalCyclerControl():
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


def GetThermalCyclerData():
    length = 4
    command = 0x93
    checksum = address + length + command
    commandToSend = pack("<BBBB", address, length, command, checksum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Cycler %s.' % commandToSend)
    answerBytes = port.read(18)
    config.logger.info(u'Recv Cycler: %s' % answerBytes)
    answer = unpack("<BBBfffBBB", answerBytes)
    if answer[8] != (answer[0] +
                     answer[1] +
                     answer[2] +
                     FloatToSumOfBytes(answer[3]) +
                     FloatToSumOfBytes(answer[4]) +
                     FloatToSumOfBytes(answer[5]) +
                     answer[6] +
                     answer[7]) % 256:
        config.logger.error(u'Message is corrupted')
        exit()
    else:
        return answer
