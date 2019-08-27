# coding=utf-8
from struct import *
import struct
import num2int as n2i
import serial
import config
import time

adress = 8
flag = 0
""""
Значения флагов представленны ниже:
0 - термостат включен
1 - изменение T термостата
2 - стабилизация T термостата
3 - термостат выключен
4 - Т термостата > допустимой 
5 - Т термостата < допустимой
6 - Т радиатора > допустимой
7 - Т радиатора < допустимой
8 - ошибка отправки сообщения
9 - ошибка подключения к порту
10 - превышено время нагрева
11 - ошибка приема сообщения
12 - ошибочный формат команды (от термостата)
"""

try:
    port_therm = serial.Serial('COM14',
                               115200,
                               parity=serial.PARITY_NONE,
                               stopbits=1)
except serial.SerialException:
    flag = 9


def SetSippersZero():
    length = 4
    command = 0xBC
    crc = adress + length + command
    answer = ''
    command_to_send = pack("<BBBB", adress, length, command, crc)
    try:
        port_therm.write(command_to_send)
        answer_bites = port_therm.read(4)
        print(answer_bites)
        answer = unpack("<BBBB", answer_bites)
    except:
        answer = "Answer not exist"
    return answer


def IniTherm():
    """
    Функция инициализации, считываем значение температуры
     и возвращаем флаг о текущем состоянии термостата

    """
    _, flag = GetTemp()
    return flag


def TestTherm():
    """
    Функция для тестирования термостата. Нагреваем до
    температуры 25 градусов и ждем когда нагреется.
    Выводим состояние термостата и записываем в лог время нагрева(это необязательно сами решите как надо)
    :return: flag

    """
    set_temp = 25
    SetTemp(set_temp)
    temp, _ = GetTemp()
    eps = 0.01
    start_time = time.time()
    config.logger.info(
        "Test to measure the heating time to% s is launched" % temp)
    while abs(
            set_temp - temp) > eps or time.time() - start_time < 20:  # пока разница с 25 градусов не будет меньше 0.01
        # или не пройдет 20 сек
        temp, _ = GetTemp()
    time_test = time.time() - start_time
    vel = GetVelocityHeat()
    if time_test > 20:
        flag = 10
        config.logger.info(
            "Время нагрева составило %f при заданной скорости %f" % (
            time_test, vel[3]))
    else:
        _, flag = GetTemp()
        config.logger.info(
            "Время нагрева составило %f при заданной скорости %f" % (
            time_test, vel[3]))
    return flag


def SetTemp(temp):
    """
    Функция для нагрева до нужной температуры. Посылается команда нагрева,
     ждется ответ и записывается в лог температура
    :param temp:
    :return:flag

    """
    length = 8
    command = 0x91
    crc = (adress + length + command + n2i.num2int(
        temp)) % 256  # составление пакета данных
    values_set_temp = pack("<BBBfB", adress, length, command, temp,
                           crc)  # преобразование в последовательность бит
    try:
        port_therm.write(values_set_temp)
        answer_bity = (port_therm.readline())
        unpack("BBBB", answer_bity)
    except serial.SerialException:
        return 8
    except struct.error:
        return 12
    except:
        return 11
    _, flag = GetTemp()
    config.logger.info("Температура %f установлена" % temp)
    return flag


def GetTemp():
    """
    Функция, которая узнает текущюю температуру и состояние термостата
    :return: temp, flag
    """
    length = 4
    command = 0x90
    crc = adress + length + command
    values_check_temp = pack("<BBBB", adress, length, command, crc)
    try:
        port_therm.write(values_check_temp)
        answer_bity = (port_therm.readline())
        answer = unpack("<BBBffBBB", answer_bity)
    except serial.SerialException:
        return -273, 8
    except struct.error:
        return -273, 12
    except:
        return -273, 11
    temp = answer[3]
    flag = GetFlag(answer[5], answer[6])
    return temp, flag


def StopHeat():
    """
    Функция для остановки работы термостата
    :return: flag
    """
    length = 4
    command = 0x41
    crc = adress + length + command
    values_stop = pack("<BBBB", adress, length, command, crc)
    try:
        port_therm.write(values_stop)
        answer_bity = (port_therm.readline())
        unpack("<BBBB", answer_bity)
    except serial.SerialException:
        return 8
    except struct.error:
        return 12
    except:
        return 11
    _, flag = GetTemp()
    return flag


def SetVelocityHeat(heat, cooling):
    length = 12
    command = 0x85
    crc = (adress + length + command + n2i.num2int(heat) + n2i.num2int(
        cooling)) % 256
    values_set_velocity_heat = pack("<BBBffB", adress, length, command, heat,
                                    cooling, crc)
    port_therm.write(values_set_velocity_heat)
    answer_bity = (port_therm.readline())
    answer = unpack("<BBBB", answer_bity)
    return answer


def GetVelocityHeat():
    length = 4
    command = 0x84
    crc = adress + length + command
    values_check_velocity_heat = pack("<BBBB", adress, length, command, crc)
    port_therm.write(values_check_velocity_heat)
    answer_bity = (port_therm.readline())
    answer = unpack("<BBBffB", answer_bity)
    return answer


def SetDeviationHeat(temp_heat, time_heat, temp_cooling, time_cooling):
    length = 20
    command = 0x83
    crc = (adress + length + command + n2i.num2int(temp_heat) + n2i.num2int(
        time_heat)
           + n2i.num2int(temp_cooling) + n2i.num2int(time_cooling)) % 256
    values_set_deviation_heat = pack("<BBBffffB", adress, length, command, crc)
    port_therm.write(values_set_deviation_heat)
    answer_bity = (port_therm.readline())
    answer = unpack("<BBBB", answer_bity)
    return answer


def GetDeviationHeat():
    length = 4
    command = 0x82
    crc = adress + length + command
    values_check_deviation_heat = pack("<BBBB", adress, length, command, crc)
    port_therm.write(values_check_deviation_heat)
    answer_bity = (port_therm.readline())
    answer = unpack("<BBBffffB", answer_bity)
    return answer


def GetFlag(byte_1, byte_2):
    flag_0 = byte_1 & 128
    flag_1 = byte_1 & 64
    flag_2 = byte_1 & 8
    if flag_0 == 1:
        flag = 0
    else:
        flag = 3
    if flag_1 == 0:
        flag = 1
    else:
        flag = 2
    if flag_2 == 1:
        if byte_2 == 0:
            flag = 0
        elif byte_2 == 1:
            flag = 4
        elif byte_2 == 2:
            flag = 5
        elif byte_2 == 3:
            flag = 6
        elif byte_2 == 4:
            flag = 7
    else:
        flag = 0
    return flag
