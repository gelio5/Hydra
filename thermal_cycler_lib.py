import ports
import config
import serial
from types_to_sum_of_bytes import *
from struct import *
import time
import redis

port = serial.Serial(port=ports.cycler,
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=0.3)
address = 8
port.close()

"""
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
"""

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
        i = FloatToSumOfBytes(i)
        checksum += i
        commandToSend += pack('<f', i)
        n += 1
    if n != 0:
        checksum = checksum % 256
    commandToSend += pack('<B', checksum)
    port.write(commandToSend)
    config.logger.info(u'Xmit Cooler: %s' % commandToSend)
    return commandToSend


def SetThermalCyclerTemp(temp: float):
    #try:
    #   port.open()
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
        SetThermalCyclerTemp(temp)
    else:
        port.close()
        config.logger.info(u'Cooler going to %s' % temp)
    conredis = redis.Redis(host='127.0.0.1', port=6379, db=1)
    ready = 0
    while ready <= temp - 0.5 or ready >= temp + 0.5:
        ready = float(conredis.hget("sensors", 'TC').decode())
        time.sleep(0.5)
    return


def StopThermalCyclerControl():
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.2)
    #    port.open()
    #length = 4
    #command = 0x41
    #checksum = address + length + command
    #commandToSend = pack("<BBBB", address, length, command, checksum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Cooler: %s' % commandToSend)
    commandToSend = Transceiver(0x41, 4)
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
    #config.logger.info(u'Xmit Cycler %s.' % commandToSend)
    Transceiver(0x93, 4)
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


def GetSpeed():
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.01)
    #    port.open()
    #length = 4
    #command = 0x84
    #checksum = address + length + command
    #commandToSend = pack("<BBBB", address, length, command, checksum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Cycler %s.' % commandToSend)
    Transceiver(0x84, 4)
    answerBytes = port.read(12)
    config.logger.info(u'Recv Cycler: %s' % answerBytes)
    answer = unpack("<BBBffB", answerBytes)
    if answer[5] != (answer[0] +
                     answer[1] +
                     answer[2] +
                     FloatToSumOfBytes(answer[3]) +
                     FloatToSumOfBytes(answer[4])) % 256:
        config.logger.error(u'Message is corrupted')
        port.close()
        answer = GetSpeed()
        return answer
    else:
        port.close()
        return answer


def SetSpeed(heat, cold):
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.02)
    #    port.open()
    #length = 4
    #command = 0x85
    #checksum = (address + length + command + FloatToSumOfBytes(
    #    heat) + FloatToSumOfBytes(cold)) % 256
    #commandToSend = pack("<BBBffB", address, length, command, float(heat),
    #                     float(cold), checksum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Cycler %s.' % commandToSend)
    Transceiver(0x85, 4, heat, cold)
    answerBytes = port.read(5)
    config.logger.info(u'Recv Cycler: %s' % answerBytes)
    answer = unpack("<BBBBB", answerBytes)
    if answer[4] != (answer[0] +
                     answer[1] +
                     answer[2]) % 256:
        config.logger.error(u'Message is corrupted')
        port.close()
        print('ex')
        print(answer)
        return
    else:
        port.close()
        print('god')
        return


def SetThermalCyclerTempLowSpeed(startTemp: float, stopTemp: float, timeToGo: float):
    #try:
    #    port.open()
    #except Exception:
    #    time.sleep(0.2)
    #    port.open()
    #length = 16
    #command = 0x9A
    #checksum = (address + length + command + FloatToSumOfBytes(startTemp) +
    #            FloatToSumOfBytes(stopTemp) + FloatToSumOfBytes(
    #            timeToGo)) % 256
    #commandToSend = pack("<BBBfffB", address, length, command, startTemp,
    #                     stopTemp, timeToGo, checksum)
    #port.write(commandToSend)
    #config.logger.info(u'Xmit Cycler %s.' % commandToSend)
    Transceiver(0x9A, 16, startTemp, stopTemp, timeToGo)
    answerBytes = port.read(4)
    config.logger.info(u'Recv Cooler: %s' % answerBytes)
    answer = unpack("<BBBB", answerBytes)
    if answer[3] != 0xA6:
        config.logger.error(u'Answer message is corrupted')
        port.close()
        SetThermalCyclerTempLowSpeed(startTemp, stopTemp, timeToGo)
    else:
        port.close()
    conredis = redis.Redis(host='127.0.0.1', port=6379, db=1)
    ready = 0
    while ready <= stopTemp - 0.5 or ready >= stopTemp + 0.5:
        ready = float(conredis.hget("sensors", 'TC').decode())
        time.sleep(0.5)
    return
