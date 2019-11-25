# import syringe_lib as pump
import config
import system_commands as hydra
import sys
import time

numberOfActuatorPositions = 23
if len(sys.argv) > 1:
    if sys.argv[1] == '1':
        config.logger.info(u'========       Postrun wash is started       '
                           u'========')
    elif sys.argv[1] == '2':
        config.logger.info(u'========       Standby wash is started       '
                           u'========')
    elif sys.argv[1] == '3':
        config.logger.info(u'========       Maintenance wash is started         '
                           u'========')

'''int(sys.argv[1])'''
for j in range(1):
    for k in range(8):
        config.logger.info(u'========        Stand by Wash %s of 8       '
                           u'========' % str(k + 1))
        for i in range(numberOfActuatorPositions):
            if i < 22:
                hydra.PumpToFlowcell(actPos=i+1,
                                     volume=750,
                                     aspirationRate=500,
                                     dispenseRate=2000)
            elif i == 22:
                continue
            else:
                hydra.AspirateFromBypass(volume=7500,
                                         aspirationRate=500,
                                         dispenseRate=2000)
config.logger.info(u'========        Wash is complete        '
                   u'=======')
