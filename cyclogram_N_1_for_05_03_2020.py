from stand_cooler_lib import SetStandDown, SetStandUp
from system_commands import PumpToFlowcell
from thermal_cycler_lib import SetThermalCyclerTemp
import time
from system_commands import PumpToActuator


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

PumpToActuator(1)
PumpToActuator(2)
PumpToActuator(4)
PumpToActuator(3)

# Imaging
print("Imaging")
h = ''
while h != "work":
    h = input(">>")
    print(h)

for i in range(19):
    print("Встраивание " + str(i + 2) + "-й буквы")
    a = time.time()
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3, volume=331)
    PumpToFlowcell(actPos=4, volume=167)
    PumpToFlowcell(actPos=3, volume=71)
    time.sleep(10)
    PumpToFlowcell(actPos=3, volume=623)
    PumpToFlowcell(actPos=1, volume=131)
    PumpToFlowcell(actPos=3, volume=64)
    SetThermalCyclerTemp(temp=65)
    time.sleep(20)
    PumpToFlowcell(actPos=3, volume=16)
    time.sleep(20)
    SetThermalCyclerTemp(temp=22)
    PumpToFlowcell(actPos=3, volume=311)
    PumpToFlowcell(actPos=2, volume=167)
    PumpToFlowcell(actPos=3, volume=64)
    time.sleep(15)
    print(a - time.time())
    # Imaging
    print("Imaging")
    h = ''
    while h != "work":
        h = input(">>")
        print(h)
