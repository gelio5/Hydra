#! python
#
# noinspection PyPep8Naming
#
# This file is library for rating time of switch in Valco Instruments Co. Inc.
# Universal Electric Actuator
# Models EUH, EUD, and EUT
# Firmware revisions EQ and subsequent

import serial
import numpy
import time
import actuator_lib as act

actuatorPort = serial.Serial(port='COM6',
                             baudrate=115200,
                             bytesize=serial.EIGHTBITS,
                             parity=serial.PARITY_NONE,
                             stopbits=serial.STOPBITS_ONE)

actuatorPort.isOpen()

numbersOfPositions = 24
numberOfCycles = 1

timings = numpy.zeros((1, numbersOfPositions, numbersOfPositions))

for k in range(numberOfCycles):
    for j in range(numbersOfPositions):
        for i in range(numbersOfPositions):
            if i != j:
                act.GoToPosition(actuatorPort, str(i + 1))
                time.sleep(2)
                act.GoToPosition(actuatorPort, str(j + 1))
                time.sleep(2)
                timings[k][j][i] = act.MovingTime(actuatorPort)
                time.sleep(2)
                i += 1
            else:
                i += 1
        j += 1
        #time.sleep(j*100)
    k += 1
    #time.sleep(k*1000)

print(timings)

timings = [
    [0, 260, 395, 525, 655, 790, 930, 1060, 1190, 1320, 1455, 1590, 1680, 1555,
     1420, 1295, 1160, 1025, 895, 765, 630, 495, 360, 225],
    [250, 0, 265, 390, 525, 660, 795, 930, 1065, 1195, 1325, 1455, 1590, 1680,
     1555, 1420, 1285, 1160, 1025, 895, 760, 630, 495, 360],
    [390, 265, 0, 260, 390, 525, 660, 790, 925, 1060, 1190, 1320, 1455, 1585,
     1685, 1560, 1425, 1295, 1160, 1025, 890, 760, 630, 495],
    [525, 390, 260, 0, 260, 395, 530, 655, 790, 925, 1055, 1190, 1320, 1450,
     1585, 1685, 1560, 1425, 1295, 1160, 1025, 895, 760, 625],
    [660, 525, 395, 265, 0, 255, 395, 525, 655, 785, 920, 1050, 1190, 1320,
     1450, 1580, 1685, 1560, 1425, 1295, 1165, 1030, 900, 765],
    [790, 660, 530, 395, 260, 0, 260, 395, 530, 790, 655, 920, 1055, 1185,
     1320, 1450, 1580, 1690, 1560, 1425, 1295, 1165, 1035, 900],
    [930, 795, 660, 525, 395, 265, 0, 260, 390, 525, 660, 785, 920, 1055, 1185,
     1315, 1450, 1580, 1690, 1560, 1425, 1295, 1160, 1030],
    [1060, 930, 795, 660, 530, 395, 260, 0, 255, 390, 520, 655, 790, 920, 1055,
     1185, 1315, 1450, 1580, 1695, 1560, 1430, 1295, 1160],
    [1195, 1060, 930, 795, 665, 525, 395, 260, 0, 260, 390, 520, 660, 785, 920,
     1055, 1185, 1320, 1450, 1580, 1690, 1565, 1430, 1295],
    [1325, 1195, 1060, 925, 790, 660, 525, 395, 255, 0, 255, 390, 525, 655,
     790, 920, 1050, 1180, 1320, 1450, 1580, 1690, 1560, 1430],
    [1455, 1325, 1190, 1055, 925, 790, 655, 525, 390, 255, 0, 260, 390, 525,
     660, 785, 920, 1050, 1185, 1315, 1450, 1580, 1690, 1565],
    [1585, 1455, 1320, 1190, 1055, 920, 785, 655, 520, 385, 255, 0, 260, 390,
     530, 660, 795, 920, 1055, 1185, 1325, 1455, 1590, 1690],
    [1720, 1585, 1450, 1320, 1185, 1055, 915, 780, 650, 520, 385, 255, 0, 260,
     390, 525, 660, 795, 925, 1055, 1190, 1320, 1450, 1585],
    [1565, 1710, 1580, 1450, 1310, 1180, 1050, 915, 780, 650, 515, 385, 255, 0,
     260, 395, 525, 660, 790, 925, 1055, 1185, 1315, 1450],
    [1425, 1560, 1710, 1585, 1450, 1315, 1185, 1050, 920, 785, 650, 520, 385,
     260, 0, 255, 385, 525, 655, 785, 925, 1055, 1185, 1315],
    [1300, 1425, 1560, 1710, 1585, 1450, 1315, 1180, 1050, 915, 785, 655, 520,
     390, 260, 0, 255, 385, 520, 655, 790, 925, 1055, 1190],
    [1165, 1295, 1430, 1565, 1715, 1585, 1450, 1315, 1185, 1050, 920, 795, 660,
     525, 395, 260, 0, 255, 390, 525, 655, 790, 925, 1055],
    [1035, 1165, 1300, 1430, 1565, 1710, 1580, 1450, 1315, 1180, 1045, 915,
     785, 655, 525, 390, 255, 0, 260, 395, 530, 660, 795, 925],
    [900, 1030, 1160, 1300, 1435, 1565, 1710, 1580, 1450, 1315, 1180, 1055,
     915, 785, 650, 520, 390, 255, 0, 255, 390, 525, 655, 790],
    [770, 895, 1035, 1165, 1300, 1430, 1565, 1710, 1575, 1445, 1310, 1180,
     1050, 915, 785, 655, 520, 390, 250, 0, 260, 395, 525, 665],
    [630, 765, 900, 1035, 1165, 1295, 1425, 1565, 1705, 1580, 1450, 1320, 1190,
     1055, 920, 795, 660, 525, 390, 255, 0, 255, 390, 520],
    [500, 635, 765, 900, 1040, 1165, 1300, 1430, 1570, 1710, 1580, 1450, 1320,
     1185, 1050, 925, 790, 660, 525, 390, 260, 0, 260, 390],
    [365, 500, 630, 765, 900, 1030, 1165, 1295, 1430, 1560, 1710, 1590, 1450,
     1320, 1180, 1055, 920, 795, 655, 525, 390, 260, 0, 260],
    [230, 365, 500, 630, 765, 900, 1035, 1160, 1295, 1425, 1565, 1710, 1585,
     1450, 1315, 1180, 1050, 920, 790, 655, 525, 390, 255, 0]
]

diffOne = []
diffTwo = []
diffThree = []
diffFour = []
diffFive = []
diffSix = []
diffSeven = []
diffEight = []
diffNine = []
diffTen = []
diffEleven = []
diffTwelve = []

for i in range(24):
    for j in range(24):
        if i != j:
            x = abs(i-j)
            if x > 12:
                x = abs(x - 24)
            if x == 1:
                diffOne.append(timings[i][j])
            elif x == 2:
                diffTwo.append(timings[i][j])
            elif x == 3:
                diffThree.append(timings[i][j])
            elif x == 4:
                diffFour.append(timings[i][j])
            elif x == 5:
                diffFive.append(timings[i][j])
            elif x == 6:
                diffSix.append(timings[i][j])
            elif x == 7:
                diffSeven.append(timings[i][j])
            elif x == 8:
                diffEight.append(timings[i][j])
            elif x == 9:
                diffNine.append(timings[i][j])
            elif x == 10:
                diffTen.append(timings[i][j])
            elif x == 11:
                diffEleven.append(timings[i][j])
            elif x == 12:
                diffTwelve.append(timings[i][j])
        j += 1
    i += 1

print(diffOne, len(diffOne))
print(diffTwo, len(diffTwo))
print(diffThree, len(diffThree))
print(diffFour, len(diffFour))
print(diffFive, len(diffFive))
print(diffSix, len(diffSix))
print(diffSeven, len(diffSeven))
print(diffEight, len(diffEight))
print(diffNine, len(diffNine))
print(diffTen, len(diffTen))
print(diffEleven, len(diffEleven))
print(diffTwelve, len(diffTwelve))

print(len(diffOne) + len(diffTwo) + len(diffThree) + len(diffFour) +
      len(diffFive) + len(diffSix) + len(diffSeven) + len(diffEight) +
      len(diffTen) + len(diffEleven) + len(diffTwelve))

print()

print(" 1-", min(diffOne), max(diffOne), sum(diffOne)/len(diffOne))
print(" 2-", min(diffTwo), max(diffTwo), sum(diffTwo)/len(diffTwo))
print(" 3-", min(diffThree), max(diffThree), sum(diffThree)/len(diffThree))
print(" 4-", min(diffFour), max(diffFour), sum(diffFour)/len(diffFour))
print(" 5-", min(diffFive), max(diffFive), sum(diffFive)/len(diffFive))
print(" 6-", min(diffSix), max(diffSix), sum(diffSix)/len(diffSix))
print(" 7-", min(diffSeven), max(diffSeven), sum(diffSeven)/len(diffSeven))
print(" 8-", min(diffEight), max(diffEight), sum(diffEight)/len(diffEight))
print(" 9-", min(diffNine), max(diffNine), sum(diffNine)/len(diffNine))
print("10-", min(diffTen), max(diffTen), sum(diffTen)/len(diffTen))
print("11-", min(diffEleven), max(diffEleven), sum(diffEleven)/len(diffEleven))
print("12-", min(diffTwelve), max(diffTwelve), sum(diffTwelve)/len(diffTwelve))

"""
aw = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

d1 = []
d2 = []

for i in range(4):
    for j in range(4):
        x = abs(i - j)
        if x > 2:
            x = abs(x - 4)
        if x == 1:
            d1.append(aw[i][j])
        elif x == 2:
            d2.append(aw[i][j])
        j += 1
    i += 1

print(aw[0])
print(aw[1])
print(aw[2])
print(aw[3])
print()
print(d1, len(d1))
print(d2, len(d2))
print(len(d1)+len(d2))
"""


