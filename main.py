#! python
#
# noinspection PyPep8Naming

import actuator_lib as actuator
import syringe_lib as pump
import system_commands as hydra
import config


config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Start of the '
                   u'program      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


actuator.port.isOpen()
config.logger.info(u'Port communication with actuator is opened.')
pump.port.isOpen()
config.logger.info(u'Port for communication with pump is opened.')

actuator.Test()
pump.Initialization()
pump.Test()
pump.Status()
pump.SetValvePos(valvePos=pump.outPos)
pump.AskSyrPos()
pump.AbsoluteSyrPos(rate=500, SyrPos=0)
pump.Status()
pump.Status()
pump.Status()

actuator.port.close()
config.logger.info(u'Port for communication with actuator is closed.')
pump.port.close()
config.logger.info(u'Port for communication with pump is closed.')
config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit  '
                   u'    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

exit()
