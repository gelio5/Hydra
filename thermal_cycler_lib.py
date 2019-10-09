import ports
import config
import serial
from types_to_sum_of_bytes import *
from struct import *
import time

port = serial.Serial(port=ports.cycler,
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=0.3)
address = 8
port.close()


def SetThermalCyclerTemp(temp: float):
    try:
        port.open()
    except Exception:
        time.sleep(0.01)
        port.open()
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
        port.close()
        SetThermalCyclerTemp(temp)
    else:
        port.close()
        config.logger.info(u'Cooler going to %s' % temp)
    return


def StopThermalCyclerControl():
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
        StopThermalCyclerControl()
    else:
        config.logger.info(u'Cooler control is stop')
        port.close()
    return


def GetThermalCyclerData():
    try:
        port.open()
    except Exception:
        time.sleep(0.01)
        port.open()
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
        port.close()
        answer = GetThermalCyclerData()
        return answer
    else:
        port.close()
        return answer
