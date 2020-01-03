from system_commands import PumpToActuator
from system_commands import PumpToFlowcell
from stand_cooler_lib import SetStandUp
from stand_cooler_lib import SetStandDown
from thermal_cycler_lib import SetThermalCyclerTemp
import time
import redis

conn = redis.Redis(host='127.0.0.1', port=6379, db=1)

print("Старт")
n = time.time()
SetStandDown()
time.sleep(7)
print("Установите на рабочее место штатив с реагентами и чип")
h = ''
while h != "work":
    h = input(">>")
    print(h)
SetStandUp()
time.sleep(7)
print("Начало отрабатывания циклограммы")

print("Заполнение рабочих каналов и промывка")
conn.set("bubble_need", 1)

print("Заполнение канала номер 3")
PumpToActuator(actPos=3)
print("Заполнение канала номер 4")
PumpToActuator(actPos=4)
print("Заполнение канала номер 8")
PumpToActuator(actPos=8)
print("Заполнение канала номер 19")
PumpToActuator(actPos=19)
print("Заполнение канала номер 20")
PumpToActuator(actPos=20)

SetThermalCyclerTemp(temp=60)
print("Денатурация")
PumpToFlowcell(actPos=8,
               volume=180,
               aspirationRate=72,
               dispenseRate=2000)

print("Промывка буфером")
PumpToFlowcell(actPos=3,
               volume=180,
               aspirationRate=72,
               dispenseRate=2000)
time.sleep(15)

print("Детекция")
h = ''
while h != "work":
    h = input(">>")
    print(h)

SetThermalCyclerTemp(temp=60)

for i in range(5):
    print(str(i+1) + "итерация для 19 ячейки")
    for j in range(10):
        print("Прокачка HEX")
        PumpToFlowcell(actPos=19,
                       volume=90,
                       aspirationRate=72,
                       dispenseRate=2000)
        time.sleep(5)
        print("Промывка буфером")
        PumpToFlowcell(actPos=3,
                       volume=180,
                       aspirationRate=72,
                       dispenseRate=2000)
        print("Прокачка CMS")
        PumpToFlowcell(actPos=4,
                       volume=180,
                       aspirationRate=72,
                       dispenseRate=2000)
        print("Подталкивание буфером")
        PumpToFlowcell(actPos=3,
                       volume=48,
                       aspirationRate=72,
                       dispenseRate=2000)
        time.sleep(10)
        print("Промывка буфером")
        PumpToFlowcell(actPos=3,
                       volume=720,
                       aspirationRate=72,
                       dispenseRate=2000)
    print("Детекция")
    h = ''
    while h != "work":
        h = input(">>")
        print(h)

print("Денатурация")
PumpToFlowcell(actPos=8,
               volume=180,
               aspirationRate=72,
               dispenseRate=2000)

print("Промывка буфером")
PumpToFlowcell(actPos=3,
               volume=180,
               aspirationRate=72,
               dispenseRate=2000)
time.sleep(15)

print("Детекция")
h = ''
while h != "work":
    h = input(">>")
    print(h)

for i in range(5):
    print(str(i+1) + "итерация для 20 ячейки")
    for j in range(10):
        print("Прокачка ROX")
        PumpToFlowcell(actPos=20,
                       volume=90,
                       aspirationRate=72,
                       dispenseRate=2000)
        time.sleep(5)
        print("Промывка буфером")
        PumpToFlowcell(actPos=3,
                       volume=180,
                       aspirationRate=72,
                       dispenseRate=2000)
        print("Прокачка CMS")
        PumpToFlowcell(actPos=4,
                       volume=180,
                       aspirationRate=72,
                       dispenseRate=2000)
        print("Подталкивание буфером")
        PumpToFlowcell(actPos=3,
                       volume=48,
                       aspirationRate=72,
                       dispenseRate=2000)
        time.sleep(10)
        print("Промывка буфером")
        PumpToFlowcell(actPos=3,
                       volume=720,
                       aspirationRate=72,
                       dispenseRate=2000)
    print("Детекция")
    h = ''
    while h != "work":
        h = input(">>")
        print(h)

conn.set("bubble_need", 0)
print(time.time()-n)
