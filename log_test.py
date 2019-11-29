# log_test.py
# -*- coding: utf-8 -*-
import actuator_lib, pump, system_commands, stand_cooler_lib, thermal_cycler_lib
import serial.tools.list_ports
import subprocess
import time
import sensors_lib
#system_commands.PumpToFlowcell(actPos=3, volume=90, aspirationRate=75, dispenseRate=2000)
#thermal_cycler_lib.SetThermalCyclerTemp(22)
#thermal_cycler_lib.SetThermalCyclerTempLowSpeed(startTemp=65,stopTemp=40, timeToGo=250)
#time.sleep(180)
#for i in range(1):
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
