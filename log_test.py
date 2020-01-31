# log_test.py
# -*- coding: utf-8 -*-
import actuator_lib, pump, system_commands,  thermal_cycler_lib, stand_cooler_lib

import serial.tools.list_ports
import subprocess
import time
import redis
#thermal_cycler_lib.SetThermalCyclerTemp(30)
#conn = redis.Redis(host='127.0.0.1', port=6379, db=1)
#conn.set("bubble_need", 0)
#print(pump.AskSyrPos())
#import sensors_lib
n = time.time()
#pump.Initialization()
system_commands.PumpToFlowcell(actPos=3, volume=90)
print(time.time() - n)
#stand_cooler_lib.SetCoolerTemp(4)
#thermal_cycler_lib.SetThermalCyclerTemp(30)

#system_commands.PumpToFlowcell(actPos=3, volume=90)
#system_commands.PumpToFlowcell(actPos=3, volume=90)
#system_commands.PumpToFlowcell(actPos=3, volume=90)
#system_commands.PumpToFlowcell(actPos=3, volume=90)
#thermal_cycler_lib.SetThermalCyclerTemp(22)
#thermal_cycler_lib.SetThermalCyclerTempLowSpeed(startTemp=65,stopTemp=40, timeToGo=250)
#time.sleep(180)
#for i in range(1):
#system_commands.AspirateFromBypass(3000, 500, 5000)
#system_commands.DispenseToFlowcell(actPos=3, volume=1600, dispenseRate=100)
#stand_cooler_lib.SetStandUp()
#time.sleep(7)
#for i in range(5):
# system_commands.PumpToFlowcell(3, 3000, 72, 2000)
#    time.sleep(3)
#conn.set("bubble_need", 1)
"""
system_commands.PumpToActuator(1)
system_commands.PumpToActuator(2)
system_commands.PumpToActuator(4)
system_commands.PumpToActuator(8)
system_commands.PumpToActuator(12)
"""

"""
print("Выход на температуру 50°C")
thermal_cycler_lib.SetThermalCyclerTemp(temp=46)
print("Денатурация")
system_commands.PumpToFlowcell(actPos=8, aspirationRate=72, volume=180, dispenseRate=2000)
time.sleep(30)
system_commands.PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
print("Выход на температуру 65°C")
thermal_cycler_lib.SetThermalCyclerTemp(temp=65)
print("Введение и отжиг праймеров для секвенирования первой цепи")
print("Введение праймеров для секвенирования первой цепи")
for i in range(2):
    print("Итерация №" + str(i + 1))
    system_commands.PumpToFlowcell(actPos=12, volume=180, aspirationRate=72, dispenseRate=2000)
    time.sleep(30)
print("Отжиг праймеров")
thermal_cycler_lib.SetThermalCyclerTempLowSpeed(startTemp=65, stopTemp=40, timeToGo=250)
print("Ожидание 60 секунд")
time.sleep(60)
print("Промывка буфером")
system_commands.PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
time.sleep(15)
print("Встраивание первого нуклеотида")
print("Выход на температуру 60°C")
thermal_cycler_lib.SetThermalCyclerTemp(temp=60)
print("Промывка буфером")
system_commands.PumpToFlowcell(actPos=3, volume=180, aspirationRate=72, dispenseRate=2000)
time.sleep(15)
"""
"""
#
#stand_cooler_lib.SetStandDown()
sensors_lib.BubOn()
q = time.time()
time.sleep(5)
system_commands.PumpToFlowcell(actPos=3, aspirationRate=72, volume=3000, dispenseRate=2000)
time.sleep(3)
sensors_lib.BubAsk()
print(time.time()-q)
sensors_lib.BubOff()
"""
#print(thermal_cycler_lib.GetSpeed())
#thermal_cycler_lib.SetSpeed(heat=8, cold=-0.5)
#print(thermal_cycler_lib.GetSpeed())
# stand_cooler_lib.GetCoolerData()
# stand_cooler_lib.SetStandDown()
# stand_cooler_lib.port.close()
# ask_sensors = 'ask_sensors.py'
#print(stand_cooler_lib.GetCoolerData())
#process_sensors = subprocess.Popen(['python', './Subprocess/ask_sensors.py'])
#subprocess.check_output(['python', './lib/stand_cooler_lib.py', 'down'])
#actuator_lib.Test()
#pump.Initialization()

#thermal_cycler_lib.SetThermalCyclerTemp(50)
#time.sleep(120)
#thermal_cycler_lib.StopThermalCyclerControl()
#thermal_cycler_lib.SetThermalCyclerTemp(28)
#time.sleep(20)
#system_commands.PumpToFlowcell(actPos=3, volume=3000, aspirationRate=50, dispenseRate=2000)
#subprocess.Popen(['python', './Subprocess/getCool.py'])
#pump.Test()
#for i in range(20):
 #   system_commands.PumpToFlowcell(3, 2000, 500, 2000)
# system_commands.PumpToFlowcell(18, 2000, 5800, 2000)
# system_commands.PumpToFlowcell(15, 2000, 5800, 2000)
# system_commands.PumpToFlowcell(19, 2000, 5800, 2000)

#thermal_cycler_lib.SetThermalCyclerTemp(25)
#time.sleep(5)
#thermal_cycler_lib.StopThermalCyclerControl()
"""for i in range(5):
    thermal_cycler_lib.SetThermalCyclerTemp(20)
    time.sleep(60)
    thermal_cycler_lib.SetThermalCyclerTemp(50)
    time.sleep(60)"""
#stand_cooler_lib.SetStandUp()
#thermal_cycler_lib.SetThermalCyclerTemp(50)
#thermal_cycler_lib.TestNewFunction(startTemp=30, stopTemp=65, timeToGo=700)
#time.sleep(60)
#thermal_cycler_lib.SetThermalCyclerTempLowSpeed(40)
#time.sleep(60)
#system_commands.PumpToActuator(actPos=3)
#system_commands.PumpToActuator(actPos=3)
#system_commands.PumpToFlowcell(actPos=2, volume=90, aspirationRate=10, dispenseRate=2000)

"""
thermal_cycler_lib.SetThermalCyclerTemp(60)
system_commands.PumpToFlowcell(actPos=3, volume=270, aspirationRate=72, dispenseRate=2000)
system_commands.PumpToFlowcell(actPos=4, volume=180, aspirationRate=72, dispenseRate=2000)
system_commands.PumpToFlowcell(actPos=3, volume=48, aspirationRate=72, dispenseRate=2000)
time.sleep(10)
system_commands.PumpToFlowcell(actPos=3, volume=720, aspirationRate=72, dispenseRate=2000)
"""
#t = 6
#print(type(t) == int)