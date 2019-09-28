# import syringe_lib as pump
from lib import config, system_commands as hydra
import sys
numberOfActuatorPositions = 23

if sys.argv[1] == '1':
    config.logger.info(u'========       Postrun wash is started       '
                       u'========')
elif sys.argv[1] == '2':
    config.logger.info(u'========       Standby wash is started       '
                       u'========')
elif sys.argv[1] == '3':
    config.logger.info(u'========       Maintenance wash is started         '
                       u'========')


for j in range(int(sys.argv[1])):
    for k in range(8):
        config.logger.info(u'========        Stand by Wash %s of 8       '
                           u'========' % str(k + 1))
        for i in range(numberOfActuatorPositions):
            if i < 22:
                hydra.PumpToFlowcell(actPos=i+1,
                                     volume=600,
                                     aspirationRate=160,
                                     dispenseRate=800)
            elif i == 22:
                continue
            else:
                hydra.AspirateFromBypass(volume=600,
                                         aspirationRate=160,
                                         dispenseRate=800)
config.logger.info(u'========        Maintenance wash is complete        '
                   u'=======')
