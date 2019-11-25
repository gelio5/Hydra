import config
from system_commands import PumpToFlowcell
from system_commands import AspirateFromBypass
from system_commands import DispenseToFlowcell

config.logger.info(u'========       Postrun wash is started       '
                   u'========')
for i in range(3):
    PumpToFlowcell(actPos=3,
                   volume=2400,
                   aspirationRate=500,
                   dispenseRate=2000)
    PumpToFlowcell(actPos=17,
                   volume=3000,
                   aspirationRate=500,
                   dispenseRate=2000)
    PumpToFlowcell(actPos=3,
                   volume=2400,
                   aspirationRate=500,
                   dispenseRate=2000)
    for j in range(8):
        PumpToFlowcell(actPos=3,
                       volume=600,
                       aspirationRate=500,
                       dispenseRate=2000)
        DispenseToFlowcell(actPos=17,
                           volume=600,
                           dispenseRate=500)
