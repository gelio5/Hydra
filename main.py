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
config.logger.info(u'Port for ПЕНИС with actuator is opened.')
pump.port.isOpen()
config.logger.info(u'Port for communication with pump is opened.')

pump.Initialization()
pump.Test()
actuator.Test()
pump.SetValveAbsoluteSyrPos(valvePos=pump.inpPos, rate=1500, syrPos=2300)
hydra.PumpToFlowcell(reagentName="PR2", volume=1500, aspirationRate=800,
                     dispenseRate=1600)

actuator.port.close()
config.logger.info(u'Port for communication with actuator is closed.')
pump.port.close()
config.logger.info(u'Port for communication with pump is closed.')
config.logger.info(u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Exit      '
             u'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

exit()
