import config
from system_commands import PumpToFlowcell
from system_commands import AspirateFromBypass
from system_commands import DispenseToFlowcell
import time

config.logger.info(u'========       Postrun wash is started       '
                   u'========')
n = time.time()
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
for i in range(2):
    for j in range(14):
        if j < 12:
            PumpToFlowcell(actPos=j+5,
                           volume=600,
                           aspirationRate=500,
                           dispenseRate=2000)
        else:
            PumpToFlowcell(actPos=j+9,
                           volume=600,
                           aspirationRate=500,
                           dispenseRate=2000)
for i in range(3):
    PumpToFlowcell(actPos=1,
                   volume=600,
                   aspirationRate=500,
                   dispenseRate=2000)
    PumpToFlowcell(actPos=2,
                   volume=600,
                   aspirationRate=500,
                   dispenseRate=2000)
    PumpToFlowcell(actPos=4,
                   volume=600,
                   aspirationRate=500,
                   dispenseRate=2000)
for i in range(6):
    PumpToFlowcell(actPos=17,
                   volume=600,
                   aspirationRate=500,
                   dispenseRate=2000)
    PumpToFlowcell(actPos=18,
                   volume=600,
                   aspirationRate=500,
                   dispenseRate=2000)
    PumpToFlowcell(actPos=19,
                   volume=600,
                   aspirationRate=500,
                   dispenseRate=2000)
    PumpToFlowcell(actPos=20,
                   volume=600,
                   aspirationRate=500,
                   dispenseRate=2000)
for i in range(4):
    AspirateFromBypass(volume=600,
                       aspirationRate=500,
                       dispenseRate=2000)
    PumpToFlowcell(actPos=3,
                   volume=600,
                   aspirationRate=500,
                   dispenseRate=2000)
print(time.time() - n)
