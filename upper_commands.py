from system_commands import PumpToFlowcell
from system_commands import PumpToActuator
from system_commands import AspirateFromBypass
from thermal_cycler_lib import SetThermalCyclerTemp
from time import sleep
from subprocess import Popen
from subprocess import PIPE
import config


def BridgeAmplification():
    config.logger.info(u'Start BridgeAmplification')
    for i in range(24):
        print("Итерация №" + str(i + 1))
        print("Прокачка реагента №8")
        PumpToFlowcell(actPos=8,
                       volume=90)
        sleep(8)
        print("Прокачка реагента №7")
        PumpToFlowcell(actPos=7,
                       volume=90)
        sleep(8)
        print("Прокачка реагента №5")
        PumpToFlowcell(actPos=5,
                       volume=270)
        sleep(19)
        config.logger.info(u'End BridgeAmplification')
    return


def BufferWash():
    config.logger.info(u'Start BufferWash')
    PumpToFlowcell(actPos=3,
                   volume=630)
    config.logger.info(u'End BufferWash')
    return


def Deblock():
    config.logger.info(u'Start Deblock')
    PumpToFlowcell(actPos=3,
                   volume=360)
    sleep(3.1)
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=4,
                   volume=120)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(10)
    config.logger.info(u'End Deblock')
    return


def Snap():
    config.logger.info(u'Start Snap')
    process = Popen("./TitleSnap.exe", stdout=PIPE)
    data = process.communicate()
    print(data[0].decode())
    sleep(3.5)
    config.logger.info(u'End Snap')


def End():
    config.logger.info(u'Start End')
    PumpToFlowcell(actPos=3,
                   volume=360)
    sleep(3.3)
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=4,
                   volume=270)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(40)
    PumpToFlowcell(actPos=3,
                   volume=12)
    sleep(35)
    config.logger.info(u'End End')


def EndRead():
    config.logger.info(u'Start EndRead')
    PumpToFlowcell(actPos=3,
                   volume=360)
    config.logger.info(u'End EndRead')


def IncorporationWithoutDeblockBefore():
    config.logger.info(u'Start IncorporationWithoutDeblockBefore')
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=1,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    SetThermalCyclerTemp(temp=65)
    sleep(30)
    PumpToFlowcell(actPos=3,
                   volume=12)
    sleep(30)
    SetThermalCyclerTemp(temp=22)
    sleep(60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=2,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(10)
    config.logger.info(u'End IncorporationWithoutDeblockBefore')
    return


def IncorporationWithDeblockBefore():
    config.logger.info(u'Start IncorporationWithDeblockBefore')
    PumpToFlowcell(actPos=1,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    SetThermalCyclerTemp(temp=65)
    sleep(30)
    PumpToFlowcell(actPos=3,
                   volume=12)
    sleep(30)
    SetThermalCyclerTemp(temp=22)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=2,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(10)
    config.logger.info(u'End IncorporationWithDeblockBefore')
    return


def FirstBase():
    config.logger.info(u'Start FirstBase')
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=1,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    SetThermalCyclerTemp(temp=65)
    sleep(30)
    PumpToFlowcell(actPos=3,
                   volume=12)
    sleep(30)
    SetThermalCyclerTemp(temp=22)
    sleep(60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=2,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(10)
    config.logger.info(u'End FirstBase')
    return


def SecondReadPreparation():
    config.logger.info(u'Start SecondReadPreparation')
    PumpToFlowcell(actPos=8,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=65)
    sleep(60)
    PumpToActuator(actPos=14)
    PumpToFlowcell(actPos=14,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=40)
    sleep(60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    config.logger.info(u'End SecondReadPreparation')
    return


def SecondLinearisation():
    config.logger.info(u'Start SecondLinearisation')
    PumpToActuator(actPos=10)
    PumpToFlowcell(actPos=10,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=38)
    sleep(300)
    PumpToFlowcell(actPos=10,
                   volume=90,
                   aspirationRate=9)
    sleep(300)
    PumpToFlowcell(actPos=10,
                   volume=90,
                   aspirationRate=9)
    sleep(300)
    PumpToFlowcell(actPos=3,
                   volume=360)
    config.logger.info(u'End SecondLinearisation')
    return


def PostResynthesisWash():
    config.logger.info(u'Start PostResynthesisWash')
    PumpToFlowcell(actPos=3,
                   volume=720)
    SetThermalCyclerTemp(temp=20)
    sleep(45)
    config.logger.info(u'End PostResynthesisWash')
    return


def Resynthesis():
    config.logger.info(u'Start Resynthesis')
    PumpToFlowcell(actPos=8,
                   volume=150,
                   aspirationRate=9)
    sleep(7.2)
    PumpToFlowcell(actPos=3,
                   volume=150,
                   aspirationRate=9)
    sleep(7.2)
    PumpToFlowcell(actPos=6,
                   volume=180,  # todo проверить объёмы в этом пункте
                   aspirationRate=9)
    sleep(18.7)
    config.logger.info(u'End Resynthesis')
    return


def PreresynthesisTempramp():
    config.logger.info(u'Start PreresynthesisTempramp')
    PumpToActuator(actPos=6)
    PumpToFlowcell(actPos=3,
                   volume=720)
    SetThermalCyclerTemp(temp=50)
    config.logger.info(u'End PreresynthesisTempramp')
    return


def Denaturation():
    config.logger.info(u'Start Denaturation')
    SetThermalCyclerTemp(temp=20)
    sleep(25)
    PumpToFlowcell(actPos=8,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=65)
    sleep(60)
    PumpToActuator(actPos=3)
    PumpToFlowcell(actPos=3,
                   volume=270)
    SetThermalCyclerTemp(temp=40)
    sleep(60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    config.logger.info(u'End Denaturation')
    return


def Deprotection():
    config.logger.info(u'Start Deprotection')
    SetThermalCyclerTemp(temp=20)
    sleep(120)
    PumpToActuator(actPos=11)
    PumpToFlowcell(actPos=11,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=38)
    sleep(300)
    PumpToFlowcell(actPos=11,
                   volume=90,
                   aspirationRate=9)
    sleep(300)
    PumpToFlowcell(actPos=3,
                   volume=360)
    config.logger.info(u'End Deprotection')
    return


def IndexOnePreparation():
    config.logger.info(u'Start IndexOnePreparation')
    SetThermalCyclerTemp(temp=20)
    sleep(25)
    PumpToFlowcell(actPos=8,
                   volume=270)
    SetThermalCyclerTemp(temp=65)
    sleep(60)
    PumpToActuator(actPos=13)
    SetThermalCyclerTemp(temp=40)
    sleep(60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    config.logger.info(u'End IndexOnePreparation')
    return


def FirstReadPreparation():
    config.logger.info(u'Start FirstReadPreparation')
    PumpToFlowcell(actPos=8,
                   volume=180)
    SetThermalCyclerTemp(temp=65)
    sleep(60)
    PumpToActuator(actPos=12)
    PumpToFlowcell(actPos=12,
                   volume=180)
    SetThermalCyclerTemp(temp=40)
    sleep(60)
    PumpToFlowcell(actPos=3, volume=360)
    config.logger.info(u'End FirstReadPreparation')
    return


def SBSPrime():
    config.logger.info(u'Start SBSPrime')
    SetThermalCyclerTemp(temp=20)
    PumpToActuator(actPos=1)
    PumpToActuator(actPos=2)
    PumpToActuator(actPos=4)
    PumpToFlowcell(actPos=3,
                   volume=720)
    config.logger.info(u'End SBSPrime')
    return


def FirstLinearisation():
    config.logger.info(u'Start FirstLinearisation')
    PumpToActuator(actPos=9)
    PumpToFlowcell(actPos=9,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=46)
    sleep(300)
    PumpToFlowcell(actPos=9,
                   volume=90,
                   aspirationRate=9)
    sleep(300)
    PumpToFlowcell(actPos=9,
                   volume=90,
                   aspirationRate=9)
    sleep(300)
    PumpToFlowcell(actPos=3,
                   volume=360)
    config.logger.info(u'End FirstLinearisation')
    return


def AmplificationWash():
    config.logger.info(u'Start AmplificationWash')
    PumpToFlowcell(actPos=3,
                   volume=360)
    SetThermalCyclerTemp(temp=20)
    config.logger.info(u'End AmplificationWash')
    return


def FirstExtension():
    config.logger.info(u'Start FirstExtension')
    SetThermalCyclerTemp(temp=50)
    sleep(30)
    PumpToFlowcell(actPos=5,
                   volume=520,
                   aspirationRate=9)
    sleep(3)
    for i in range(5):
        PumpToFlowcell(actPos=5,
                       volume=24,
                       aspirationRate=9)
    sleep(90)
    config.logger.info(u'End FirstExtension')
    return


def TMPBufferWash():
    config.logger.info(u'Start TMPBufferWash')
    for i in range(15):
        PumpToFlowcell(actPos=3,
                       volume=24,
                       aspirationRate=9)
        sleep(18)
    config.logger.info(u'End TMPBufferWash')
    return


def TMP300():
    config.logger.info(u'Start TMP300')
    sleep(300)
    SetThermalCyclerTemp(temp=40)
    sleep(300)
    config.logger.info(u'End TMP300')
    return


def InitialPrime():
    config.logger.info(u'Start InitialPrime')
    PumpToActuator(actPos=8)
    SetThermalCyclerTemp(temp=40)
    sleep(30)
    PumpToActuator(actPos=5)
    PumpToActuator(actPos=7)
    PumpToFlowcell(actPos=3,
                   volume=720)
    SetThermalCyclerTemp(temp=75)
    sleep(30)
    PumpToActuator(actPos=17)
    PumpToFlowcell(actPos=17,
                   volume=90)
    config.logger.info(u'End InitialPrime')
    return


def PrimePR2ByPass():
    config.logger.info(u'Start PrimePR2ByPass')
    for i in range(3):
        AspirateFromBypass(volume=60,
                           aspirationRate=72,
                           dispenseRate=2000)
    config.logger.info(u'End PrimePR2ByPass')
    return


def FlowCheck():
    config.logger.info(u'Start FlowCheck')
    PumpToActuator(actPos=15)
    PumpToActuator(actPos=16)
    PumpToActuator(actPos=3)
    config.logger.info(u'End FlowCheck')
    return
