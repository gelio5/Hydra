#! python
#
# noinspection PyPep8Naming

import actuator_lib as actuator
import syringe_lib as pump
import system_commands as hydra
# import sensors_lib as sensors
import config
import wash
import time
import threading
import therm_lib as holod


config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Start of the '
                   u'program      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


actuator.port.isOpen()
config.logger.info(u'Port communication with actuator is opened.')
pump.port.isOpen()
config.logger.info(u'Port for communication with pump is opened.')
actuator.Test()
pump.Initialization()
pump.Test()
f = open('recipe.txt', 'r')
for line in f.readlines():
    if line.find('PumpToFlowCell') != -1:
        splitter = line.split(',')
        actPos = splitter[1]
        volume = splitter[2]
        aspirationRate = splitter[3]
        dispenseRate = splitter[4]
        hydra.PumpToFlowcell(int(actPos),
                             int(volume),
                             int(aspirationRate),
                             int(dispenseRate))

actuator.port.close()
config.logger.info(u'Port for communication with actuator is closed.')
pump.port.close()
config.logger.info(u'Port for communication with pump is closed.')
config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
                   u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

exit()
