import system_commands as hydra
import syringe_lib as pump
import config
numberOfActuatorPositions = 24


def Maintenance():
    config.logger.info(u'========       Maintenance wash is started         '
                       u'========')
    for j in range(2):
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
