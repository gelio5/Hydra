from system_commands import PumpToActuator
from system_commands import PumpToFlowcell
from stand_cooler_lib import SetStandUp
from stand_cooler_lib import SetStandDown
from thermal_cycler_lib import SetThermalCyclerTempLowSpeed
from thermal_cycler_lib import SetThermalCyclerTemp
from time import time
from time import sleep
from redis import Redis


conn = Redis(host='127.0.0.1', port=6379, db=1)

print("Старт")
n = time()
SetStandDown()
sleep(7)
print("Установите на рабочее место штатив с реагентами и чип")
h = ''
while h != "work":
    h = input(">>")
    print(h)
SetStandUp()
sleep(7)
print("Начало отрабатывания циклограммы")

print("Заполнение рабочих каналов и промывка")
conn.set("bubble_need", 1)
print("Заполнение канала номер 1")
PumpToActuator(actPos=1)
print("Заполнение канала номер 2")
PumpToActuator(actPos=2)
print("Заполнение канала номер 3")
PumpToActuator(actPos=3)
print("Заполнение канала номер 5")
PumpToActuator(actPos=5)
print("Заполнение канала номер 7")
PumpToActuator(actPos=7)
print("Заполнение канала номер 8")
PumpToActuator(actPos=8)
print("Заполнение канала номер 9")
PumpToActuator(actPos=9)
print("Заполнение канала номер 12")
PumpToActuator(actPos=12)
print("Заполнение канала номер 17")
PumpToActuator(actPos=17)

print("Выход на температуру 40°C")
SetThermalCyclerTemp(temp=40)
print("Температуры циклера вышла на полку в 40°C")
print("Промывка буфером")
for i in range(10):
    print("Итерация №" + str(i+1))
    PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
    sleep(15)

print("Введение и отжиг геномной библиотеки")
print("Введение геномной библиотеки")
PumpToFlowcell(actPos=17, volume=180, aspirationRate=72, dispenseRate=2000)
sleep(15)
SetThermalCyclerTemp(temp=95)

print("Отжиг геномной библиотеки")
SetThermalCyclerTempLowSpeed(startTemp=95, stopTemp=40, timeToGo=1100)
print("Промывка буфером")
for i in range(10):
    print("Итерация №" + str(i+1))
    PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
    sleep(15)
print("Выход на температуру 50°C")
SetThermalCyclerTemp(temp=50)

print("Первая элонгация")
for i in range(6):
    print("Итерация №" + str(i + 1))
    PumpToFlowcell(actPos=5, volume=90, aspirationRate=72, dispenseRate=2000)
    sleep(30)
print("Ожидание 90 секунд")
sleep(90)
print("Денатурация")
PumpToFlowcell(actPos=8, volume=180, aspirationRate=72, dispenseRate=2000)

print("Первая мостиковая амплификация")
for i in range(24):
    print("Итерация №" + str(i + 1))
    print("Прокачка реагента №8")
    PumpToFlowcell(actPos=8, volume=90, aspirationRate=72, dispenseRate=2000)
    sleep(30)
    print("Прокачка реагента №7")
    PumpToFlowcell(actPos=7, volume=90, aspirationRate=72, dispenseRate=2000)
    sleep(30)
    print("Прокачка реагента №5")
    PumpToFlowcell(actPos=5, volume=90, aspirationRate=72, dispenseRate=2000)
    sleep(80)
print("Выход на температуру 40°C")
SetThermalCyclerTemp(temp=40)
print("Постамплификационная промывка")
for i in range(10):
    print("Итерация №" + str(i+1))
    PumpToFlowcell(actPos=3, volume=90, aspirationRate=72, dispenseRate=2000)
    sleep(15)
print("Выход на температуру 46°C")
SetThermalCyclerTemp(temp=46)

print("Отщепление первой цепи")
for i in range(3):
    print("Итерация №" + str(i + 1))
    PumpToFlowcell(actPos=9, volume=180, aspirationRate=72, dispenseRate=2000)
    sleep(300)
print("Промывка буфером")
PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
sleep(15)
print("Денатурация")
PumpToFlowcell(actPos=8, aspirationRate=72, volume=180, dispenseRate=2000)
sleep(30)
print("Выход на температуру 65°C")
SetThermalCyclerTemp(temp=65)
sleep(60)
print("Введение и отжиг праймеров для секвенирования первой цепи")
print("Введение праймеров для секвенирования первой цепи")
for i in range(2):
    print("Итерация №" + str(i + 1))
    PumpToFlowcell(actPos=12, volume=180, aspirationRate=72, dispenseRate=2000)
    sleep(30)

print("Отжиг праймеров")
SetThermalCyclerTemp(40)
print("Ожидание 60 секунд")
sleep(60)
print("Промывка буфером")
PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
sleep(15)

print("Встраивание первого нуклеотида")
print("Выход на температуру 60°C")
SetThermalCyclerTemp(temp=60)
print("Промывка буфером")
PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
sleep(15)
print("Встраивание первого нуклеотида")
PumpToFlowcell(actPos=1, volume=120, aspirationRate=72, dispenseRate=2000)
PumpToFlowcell(actPos=3, volume=48, aspirationRate=72, dispenseRate=2000)
print("Выход на температуру 65°C")
SetThermalCyclerTemp(temp=65)
print("Ожидание 90 секунд")
sleep(30)
print("Промывка буфером")
PumpToFlowcell(actPos=3, volume=12, aspirationRate=72, dispenseRate=2000)
sleep(30)
print("Выход на температуру 22°C")
SetThermalCyclerTemp(temp=22)
sleep(60)
print("Промывка буфером")
PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
sleep(15)
print("Проявление кластеров")
PumpToFlowcell(actPos=2, volume=120, aspirationRate=72, dispenseRate=2000)
sleep(30)
print("Промывка буфером")
PumpToFlowcell(actPos=3, volume=48, aspirationRate=72, dispenseRate=2000)
sleep(15)


print("Детекция")
h = ''
while h != "work":
    h = input(">>")
    print(h)

for i in range(249):
    print()
