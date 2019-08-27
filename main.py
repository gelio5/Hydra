#! python
#
# noinspection PyPep8Naming

import actuator_lib as actuator
import syringe_lib as pump
import system_commands as hydra
import sensors_lib as sensors
import config
import wash
import time
import threading


config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Start of the '
                   u'program      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


actuator.port.isOpen()
config.logger.info(u'Port communication with actuator is opened.')
pump.port.isOpen()
config.logger.info(u'Port for communication with pump is opened.')
askTimer = threading.Event()
sensors.AskSensors(askTimer)
actuator.Test()
pump.Initialization()
pump.Test()
f =open('C:/Users/808872/PycharmProjects/Hydra/recipe.txt', 'r')
for line in f.readlines():
    if not line.find('PumpToFlowCell') == -1:
        spliter = line.split(',')
        actPos = spliter[1]
        volume = spliter[2]
        aspirationRate = spliter[3]
        dispenseRate = spliter[4]
        hydra.PumpToFlowcell(actPos,volume,aspirationRate,dispenseRate)

actuator.port.close()
config.logger.info(u'Port for communication with actuator is closed.')
pump.port.close()
config.logger.info(u'Port for communication with pump is closed.')
config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
                   u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

exit()
