from system_commands import PumpToActuator
from system_commands import PumpToFlowcell
from stand_cooler_lib import SetStandUp
from stand_cooler_lib import SetStandDown
from thermal_cycler_lib import SetThermalCyclerTempLowSpeed
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
    time.sleep(15)
