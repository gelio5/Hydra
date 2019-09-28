#! python
#
# noinspection PyPep8Naming

from lib import actuator_lib as actuator, config, pump, \
    stand_cooler_lib as therm_stat, sensors_lib as sensors, \
    thermal_cycler_lib as cycler
import time

config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Start of the '
                   u'program      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


actuator.port.isOpen()
config.logger.info(u'Port for communication with actuator is opened.')
pump.port.isOpen()
config.logger.info(u'Port for communication with pump is opened.')
therm_stat.port.isOpen()
config.logger.info(
    u"Port for communication with stand and cooler is opened.")
cycler.port.isOpen()
config.logger.info(u'Port for communication with cycler is opened.')
sensors.port.isOpen()
config.logger.info(u'Port for communication with sensors is opened.')

actuator.Test()
print("act ok")
# pump.Initialization()
pump.Test()
print("pump ok")
exit()
therm_stat.SetCoolerTemp(4.0)
therm_stat.SetStandDown()
time.sleep(6)
therm_stat.GetStandState()
time.sleep(1)
therm_stat.SetStandUp()
time.sleep(6)
therm_stat.GetStandState()
time.sleep(1)
therm_stat.SetStandDown()
time.sleep(3)
therm_stat.GetStandState()
time.sleep(3)
therm_stat.GetStandState()
time.sleep(1)
cycler.SetThermalCyclerTemp(50)
time.sleep(10)
cycler.SetThermalCyclerTemp(90)
time.sleep(10)
cycler.SetThermalCyclerTemp(30)
for i in range(10):
    time.sleep(2)
    cycler.GetThermalCyclerData()
sensors.AskSensors()
therm_stat.SetStandUp()
# wash.Maintenance()

actuator.port.close()
config.logger.info(u'Port for communication with actuator is closed.')
pump.port.close()
config.logger.info(u'Port for communication with pump is closed.')
therm_stat.port.close()
config.logger.info(u'Port for communication with stand and cooler is closed.')
cycler.port.close()
config.logger.info(u'Port for communication with cycler is closed.')
sensors.port.close()
config.logger.info(u'Port for communication with sensors is closed.')
config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
                   u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

exit()
