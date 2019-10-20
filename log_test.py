# log_test.py
# -*- coding: utf-8 -*-
import actuator_lib, pump, system_commands, stand_cooler_lib, thermal_cycler_lib
import serial.tools.list_ports
import subprocess
import time
"""
f = open('./Post_Run_Wash/MiSeqSoftware.00.log', 'r')
a = f.readlines()
f.close()
b = open('./Post_Run_Wash/lg4.log', 'w')
print(len(a))
for i in range(len(a)):
    if a[i].find("19-08-07") != -1:
        b.write(a[i])
b.close()
f = open('./Post_Run_Wash/lg4.log', 'r')
a = f.readlines()
f.close()
b = open('./Post_Run_Wash/lg4.log', 'w')
print(len(a))
for i in range(len(a)):
    if a[i].find("FPGA") == -1 and\
            a[i].find("LED") == -1 and\
            a[i].find("Instrument") == -1 and\
            a[i].find("Motor") == -1 and\
            a[i].find("Camera") == -1 and\
            a[i].find("Sensor") == -1 and\
            a[i].find("Control") == -1:
        b.write(a[i])
b.close()

"""
# stand_cooler_lib.GetCoolerData()
# stand_cooler_lib.SetStandDown()
# stand_cooler_lib.port.close()
# ask_sensors = 'ask_sensors.py'
#print(stand_cooler_lib.GetCoolerData())
#process_sensors = subprocess.Popen(['python', './Subprocess/ask_sensors.py'])
#subprocess.check_output(['python', './lib/stand_cooler_lib.py', 'down'])
#actuator_lib.Test()
pump.Initialization()
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
