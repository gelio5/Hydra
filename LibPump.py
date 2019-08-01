

# Переменная Port типа serial
# Переменная Rate(5-5800) типа string
# Переменная SyrPos(0-3000) типа string
# Переменная Volume(0-3000) типа string
# Переменная ValvePos() типа string
# ValvePos('I' - input, 'O' - output, 'B' - bypass)
import time
import serial

port = serial.Serial(port="COM9",
                     baudrate=38400,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE)


def SetSpeed(Rate):
    """
    Функция устанавливает скорость передвижения шприца (Rate)
    """
    port.write(str.encode("/1" + 'V' + Rate + 'R' + '\r\n'))
    return


def AbsoluteSyrPos(Port, Rate ,SyrPos):
    """"
    Функция устанавливает шприц со скоростью Rate
    в положение SyrPos
    """
    Port.write(str.encode(
        "/1" + 'V' + Rate +  'A' + SyrPos + 'R' + '\r\n'))
    time.sleep(8)
    return


def SyrUp(Port, ValvePos,  Rate, Volume):
    """
    Функция устанавливает положение коммутатора,
    передвигает шприц со скоростью Rate
    на Volume колличество шагов вверх
    """

    Port.write(str.encode(
        "/1" + ValvePos + 'D' + Volume + 'V' + Rate + 'R' + '\r\n'))
    time.sleep(8)
    return


def SyrSetAbsoluteZero(Port,ValvePos, Rate):
    """
    Функция полностью опорожняет шприц
    """
    Port.write(str.encode(
        "/1" + ValvePos + 'P0' + 'V' + Rate + 'R' + '\r\n'))
    time.sleep(8)
    return


def SetValveAbsoluteSyrPos(Port, ValvePos, Rate, SyrPos):
    """
    Функция передвигает коммутатор в положение ValvePos,
    после передвигает шприц со скоростью Rate в положение SyrPos
    """
    Port.write(str.encode(
    "/1" + ValvePos + 'V' + Rate + 'A' + SyrPos + 'R' + '\r\n'))
    time.sleep(8)
    return


def SetValvePos(Port, ValvePos):
    """
    Функция передвигает коммутатор в положение ValvePos
    """
    Port.write(str.encode("/1" + ValvePos + 'R' + '\r\n'))
    time.sleep(0.5)
    return


def PumpInitialization():
    """
    Функция инициализирует устройство для работы
    """
    port.write(str.encode("/1" + 'h30001R' + '\r\n'))
    port.write(str.encode("/1" + 'h10000R' + '\r\n'))
    time.sleep(0.001)
    port.write(str.encode("/1" + 'h20000R' + '\r\n'))
    time.sleep(5)
    return()


def AskSyrPos():
    """
    Функция опрашивает текущее положение шприца
    """
    port.write(str.encode("/1" + '?' + '\r\n'))
    print(port.readline().decode('ascii'))
    return()


def AskValvePos():
    """
    Функция опрашивает текущее положение Коммутатора
    """
    port.write(str.encode("/1" + '?23000' + '\r\n'))
    return port.readline()


def PumpStatus():
    """
    Функция запрашивает статус насоса
    """
    port.write(str.encode("/1" + 'Q' + '\r\n'))
    print(port.readline().decode())
    return()

#def TestDoze(Port, Rate, SyrPos1, SyrPos2, i):
#   while i > 0 :
#       Port.write(str.encode("/1" + 'V' + Rate + 'A' + SyrPos1 + '\r\n'))
#       time.sleep(5)
#       Port.write(str.encode("/1" + 'V' + Rate + 'A' + SyrPos2 + '\r\n'))
#       time.sleep(5)
#       i = i - 1
#   return()




