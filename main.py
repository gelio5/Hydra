#! python
#
# noinspection PyPep8Naming

import actuator_lib as actuator
import syringe_lib as pump
import system_commands as hydra
import config
import time


config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Start of the '
                   u'program      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


actuator.port.isOpen()
config.logger.info(u'Port communication with actuator is opened.')
pump.port.isOpen()
config.logger.info(u'Port for communication with pump is opened.')

# actuator.Test()
# pump.Initialization()
pump.Test()
for i in range(3):
    pump.Aspirate(valvePos=pump.inpPos, rate=5800, volume=3000)
    pump.SyrSetAbsoluteZero(valvePos=pump.outPos, rate=5800)
pump.Aspirate(valvePos=pump.inpPos, volume=2000, rate=300)
actuator.port.close()
config.logger.info(u'Port for communication with actuator is closed.')
pump.port.close()
config.logger.info(u'Port for communication with pump is closed.')
config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
                   u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

exit()
