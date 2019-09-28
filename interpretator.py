import time
from lib import config, system_commands as hydra


def TempTest(duration, temperature):
    config.logger.info(u'Therm starts working')
    time.sleep(duration + temperature/10)
    config.logger.info(u'End of therm work')
    return()


def Wait(duration):
    config.logger.info(u'Start waiting %s seconds' % time)
    time.sleep(duration / 1000)
    config.logger.info(u'End of waiting')
    return


def Block():

    return


def Interpreter():
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

        if line.find('TempTest') != -1:
            splitter = line.split(',')
            duration = int(splitter[1])
            temperature = int(splitter[2])
            TempTest(duration, temperature)

        if line.find('Wait'):
            splitter = line.split(',')
            duration = int(splitter[1])
            Wait(duration)
