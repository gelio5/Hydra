from stand_cooler_lib import SetStandDown
from stand_cooler_lib import SetStandUp
import time
import redis
from upper_commands import BridgeAmplification
from upper_commands import FirstExtension
from system_commands import PumpToFlowcell
from system_commands import PumpToActuator
from thermal_cycler_lib import SetThermalCyclerTemp
from upper_commands import AmplificationWash
from upper_commands import FirstLinearisation
from upper_commands import SBSPrime
from highest_commands import FirstRead

conn = redis.Redis(host='127.0.0.1', port=6379, db=1)

print("Старт")
n = time.time()
#SetStandDown()
#time.sleep(7)
#print("Установите на рабочее место штатив с реагентами и чип")
#h = ''
#while h != "work":
#    h = input(">>")
#    print(h)
#SetStandUp()
#time.sleep(7)
print("Начало отрабатывания циклограммы")
conn.set("bubble_need", 1)
FirstLinearisation()
SBSPrime()
FirstRead()
"""
print("Промывка ячейки и заполнение каналов")
PumpToActuator(actPos=3)
#PumpToActuator(actPos=5)
#PumpToActuator(actPos=7)
#PumpToActuator(actPos=8)
PumpToFlowcell(actPos=3, volume=90)
for i in range(1):
    print("Используется " + str(i+1) + ' ячейка')
    print("Введите геномную библиотеку вручную")
    h = ''
    while h != "work":
        h = input(">>")
        print(h)
    SetThermalCyclerTemp(75)
    SetThermalCyclerTemp(40)
    FirstExtension()
    BridgeAmplification()
    AmplificationWash()
    print("Введите Интеркалятор и проведите детекцию")
    h = ''
    while h != "work":
        h = input(">>")
        print(h)
    """
conn.set("bubble_need", 0)
print(time.time() - n)
