#! python

import pump as psd
import actuator_lib as actuator
import logging
import time


logging.basicConfig(format=u'%(asctime)s%(levelname)-8s%(funcName)-24s'
                           u'%(message)s',
                    level=logging.DEBUG,
                    filename=u'hydra.log')

reagentNames = {"IMS": "1", "SRE": "2", "PR2": "3", "CMS": "4", "AMS1": "5",
                "AMS2": "6", "LPM": "7", "LDR": "8", "LMX1": "9", "LMX2": "10",
                "RMF": "11", "HP10": "12", "HP12": "13", "HP11": "14",
                "PW1": "15", "PW2": "16", "TMP": "17", "C1": "18", "C2": "19",
                "C3": "20", "PW3": "21"}

lengths = {1: 300, 2: 315, 3: 780, 4: 340, 5: 270, 6: 290, 7: 310, 8: 340,
           9: 360, 10: 280, 11: 315, 12: 335, 13: 260, 14: 280, 15: 315,
           16: 335, 17: 280, 18: 300, 19: 320, 20: 340, 21: 290, 22: 345}


def PumpToActuator(actPos: int):
    logging.info(u'##########   Start pumping %s with volume %s   ##########' %
                 (actPos, lengths[actPos]))
    volume = lengths[actPos]
    if int(psd.AskSyrPos()[5:-9])+volume > 3000:
        logging.warning(u'###   Syringe would be overflow   ###')
        psd.SyrSetAbsoluteZero(psd.outPos, 2000)
    logging.warning(u'###   Syringe is free to pump   ###')
    actuator.TogglePos(actPos)
    time.sleep(0.5)
    psd.Aspirate(valvePos=psd.inpPos, volume=volume, rate=150)
    logging.info(u'######################################   Pump to actuator '
                 u'done!   ######################################')


def PumpToFlowcell(actPos: int,
                   volume: int,
                   aspirationRate: int = 72,
                   dispenseRate: int = 2000):
    logging.info(u'##########   Start pumping %s with volume %s, aspiration '
                 u'rate %s and dispense rate %s   ##########' %
                 (actPos, volume, aspirationRate, dispenseRate))
    # volume = int(volume*3000/1250) + 46
    if int(psd.AskSyrPos()[5:-9])+volume > 3000:
        logging.warning(u'###   Syringe would be overflow   ###')
        psd.SyrSetAbsoluteZero(psd.outPos, dispenseRate)
    logging.warning(u'###   Syringe is free to pump   ###')
    actuator.TogglePos(actPos)
    time.sleep(0.5)
    psd.Aspirate(valvePos=psd.inpPos, volume=volume, rate=aspirationRate)
    logging.info(u'######################################   Pump to flowcell '
                 u'done!   ######################################')


def AspirateFromBypass(volume: int, aspirationRate: int, dispenseRate: int):
    logging.info(u'##########   Start Aspirating from ByPass with volume %s, '
                 u'aspiration rate %s and dispense rate %s   ##########' %
                 (volume, aspirationRate, dispenseRate))
    if int(psd.AskSyrPos()[5:-9]) + volume > 3000:
        logging.warning(u'###   Syringe would be overflow   ###')
        psd.SyrSetAbsoluteZero(psd.outPos, dispenseRate)
    logging.warning(u'###   Syringe is free to pump   ###')
    actuator.TogglePos(23)
    psd.Aspirate(valvePos=psd.byPassPos, volume=volume, rate=aspirationRate)


def DispenseToFlowcell(actPos: int,
                       volume: int,
                       dispenseRate: int):
    logging.info(u'##########   Dispensing to Flowcell %s with volume %s, '
                 u'and dispense rate %s   ##########' %
                 (actPos, volume, dispenseRate))
    actuator.TogglePos(actPos)
    time.sleep(0.5)
    psd.SetValveAbsoluteSyrPos(valvePos=psd.inpPos,
                               syrPos=int(psd.AskSyrPos()[5:-9])-volume,
                               rate=dispenseRate)
    logging.info(u'######################################   Dispense to '
                 u'flowcell done!   ######################################')


# def DispenseAndWait(waiting_time: float, dispenseRate: int):
    # now = time.time()
