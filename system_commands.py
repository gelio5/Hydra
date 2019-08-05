#! python

import actuator_lib as actuator
import syringe_lib as psd
import logging

logging.basicConfig(format=u'%(asctime)s%(levelname)-8s%(funcName)-24s'
                           u'%(message)s',
                    level=logging.DEBUG,
                    filename=u'hydra.log')

reagentNames = {"IMS": "1", "SRE": "2", "PR2": "3", "CMS": "4", "AMS1": "5",
                "AMS2": "6", "LPM": "7", "LDR": "8", "LMX1": "9", "LMX2": "10",
                "RMF": "11", "HP10": "12", "HP12": "13", "HP11": "14",
                "PW1": "15", "PW2": "16", "TMP": "17", "C1": "18", "C2": "19",
                "C3": "20", "PW3": "21"}


def PumpToFlowcell(actPos, aspValvePos, volume, aspirationRate, dispenseRate):
    logging.info(u'##########   Start pumping %s with volume %s, aspiration '
                 u'rate %s and dispense rate %s   ##########' %
                 (actPos, volume, aspirationRate, dispenseRate))
    if int(psd.AskSyrPos()[5:-9])+volume > 3000:
        logging.warning(u'###   Syringe would be overflow   ###')
        psd.SyrSetAbsoluteZero(psd.outPos, dispenseRate)
        logging.warning(u'###   Syringe is free to pump   ###')
    else:
        logging.warning(u'###   Syringe is free to pump   ###')
    actuator.TogglePos(actPos)
    psd.Aspirate(valvePos=aspValvePos, volume=volume, rate=aspirationRate)
    logging.info(u'######################################   Pump to flowcell '
                 u'done!   ######################################')
