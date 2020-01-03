from system_commands import PumpToActuator
from system_commands import PumpToFlowcell
from stand_cooler_lib import SetStandUp
from stand_cooler_lib import SetStandDown
from thermal_cycler_lib import SetThermalCyclerTemp
from thermal_cycler_lib import SetThermalCyclerTempLowSpeed
import time
import redis

conn = redis.Redis(host='127.0.0.1', port=6379, db=1)

#print("Старт")
#n = time.time()
SetStandUp()
#time.sleep(7)
#print("Установите на рабочее место штатив с реагентами и чип")
#h = ''
#while h != "work":
 #   h = input(">>")
  #  print(h)
#SetStandUp()
#time.sleep(7)
#print("Начало отрабатывания циклограммы")

#print("Заполнение рабочих каналов и промывка")
#conn.set("bubble_need", 1)
#print("Заполнение канала номер 7")
#PumpToActuator(actPos=7)
#SetThermalCyclerTemp(temp=95)
#PumpToFlowcell(3, 180, 72, 2000)
#time.sleep(60)
#SetThermalCyclerTempLowSpeed(95, 30, 60)
#conn.set("bubble_need", 0)
#print("That's oll folks")