#! python
#
# noinspection PyPep8Naming

import actuator_lib as actuator
import syringe_lib as pump
import system_commands as hydra
# import sensors_lib as sensors
import interpretator as inter
import config
import wash
import time
import threading
import stand_cooler_lib as therm_stat


config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Start of the '
                   u'program      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

"""
actuator.port.isOpen()
config.logger.info(u'Port communication with actuator is opened.')
pump.port.isOpen()
config.logger.info(u'Port for communication with pump is opened.')"""
therm_stat.port.isOpen()
config.logger.info(
    u"Port for communication with sippers and cooler is opened.")
therm_stat.SetStandZero(0)
time.sleep(9)
therm_stat.GetStandState()
time.sleep(1)
"""
actuator.Test()
pump.Initialization()
pump.Test()
inter.Interpretator()
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
therm_stat.GetCoolerData()
time.sleep(2)
therm_stat.GetCoolerData()

actuator.port.close()
config.logger.info(u'Port for communication with actuator is closed.')
pump.port.close()
config.logger.info(u'Port for communication with pump is closed.')
"""
therm_stat.port.close()
config.logger.info(u'Port for communication with sippers and cooler is closed.')
config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
                   u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

exit()
