import thermal_cycler_lib as therm
import stand_cooler_lib as cooler
import ports, time
#print(therm.GetThermalCyclerData())
#therm.StopThermalCyclerControl()
#print(therm.GetThermalCyclerData())
#for i in range (20):
#    time.sleep(1)
#    print(therm.GetThermalCyclerData())
#cooler.SetStandUp()
#cooler.SetCoolerTemp(10)
#for i in range (600):
    #time.sleep(1)
    #print(cooler.GetCoolerData())
therm.SetThermalCyclerTemp(90)
print(therm.GetThermalCyclerData())