# log_test.py
# -*- coding: utf-8 -*-
from lib import actuator_lib, sensors_lib, pump, system_commands
import serial.tools.list_ports

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
actuator_lib.Test()
pump.Initialization()
sensors_lib.AskSensors()
pump.Test()
system_commands.PumpToFlowcell(13, 2000, 5800, 2000)
system_commands.PumpToFlowcell(18, 2000, 5800, 2000)
system_commands.PumpToFlowcell(15, 2000, 5800, 2000)
system_commands.PumpToFlowcell(19, 2000, 5800, 2000)
