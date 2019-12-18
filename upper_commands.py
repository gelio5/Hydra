from system_commands import PumpToFlowcell
from system_commands import PumpToActuator
from system_commands import AspirateFromBypass
from thermal_cycler_lib import SetThermalCyclerTemp
from time import sleep
from subprocess import Popen
from subprocess import PIPE


def BridgeAmplification():
    for i in range(24):
        print("Итерация №" + str(i + 1))
        print("Прокачка реагента №8")
        PumpToFlowcell(actPos=8,
                       volume=90)
        sleep(secs=8)
        print("Прокачка реагента №7")
        PumpToFlowcell(actPos=7,
                       volume=90)
        sleep(secs=8)
        print("Прокачка реагента №5")
        PumpToFlowcell(actPos=5,
                       volume=270)
        sleep(secs=19)
    return


def BufferWash():
    PumpToFlowcell(actPos=3,
                   volume=630)
    return


def Deblock():
    PumpToFlowcell(actPos=3,
                   volume=360)
    sleep(secs=3.1)
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=4,
                   volume=120)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(secs=10)
    return


def Snap():
    process = Popen("./TitleSnap.exe", stdout=PIPE)
    data = process.communicate()
    print(data[0].decode())


def End():
    PumpToFlowcell(actPos=3,
                   volume=360)
    sleep(secs=3.3)
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=4,
                   volume=270)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(secs=40)
    PumpToFlowcell(actPos=3,
                   volume=12)
    sleep(secs=35)


def EndRead():
    PumpToFlowcell(actPos=3,
                   volume=360)


def IncorporationWithoutDeblockBefore():
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=1,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    SetThermalCyclerTemp(temp=65)
    sleep(secs=30)
    PumpToFlowcell(actPos=3,
                   volume=12)
    sleep(secs=30)
    SetThermalCyclerTemp(temp=22)
    sleep(secs=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=2,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(secs=10)
    return


def IncorporationWithDeblockBefore():
    PumpToFlowcell(actPos=1,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    SetThermalCyclerTemp(temp=65)
    sleep(secs=30)
    PumpToFlowcell(actPos=3,
                   volume=12)
    sleep(secs=30)
    SetThermalCyclerTemp(temp=22)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=2,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(secs=10)
    return


def FirstBase():
    SetThermalCyclerTemp(temp=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=1,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    SetThermalCyclerTemp(temp=65)
    sleep(secs=30)
    PumpToFlowcell(actPos=3,
                   volume=12)
    sleep(secs=30)
    SetThermalCyclerTemp(temp=22)
    sleep(secs=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    PumpToFlowcell(actPos=2,
                   volume=180)
    PumpToFlowcell(actPos=3,
                   volume=48)
    sleep(secs=10)
    return


def SecondReadPreparation():
    PumpToFlowcell(actPos=8,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=65)
    sleep(secs=60)
    PumpToActuator(actPos=14)
    PumpToFlowcell(actPos=14,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=40)
    sleep(secs=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    return


def SecondLinearisation():
    PumpToActuator(actPos=10)
    PumpToFlowcell(actPos=10,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=38)
    sleep(secs=300)
    PumpToFlowcell(actPos=10,
                   volume=90,
                   aspirationRate=9)
    sleep(secs=300)
    PumpToFlowcell(actPos=10,
                   volume=90,
                   aspirationRate=9)
    sleep(secs=300)
    PumpToFlowcell(actPos=3,
                   volume=360)
    return


def PostResynthesisWash():
    PumpToFlowcell(actPos=3,
                   volume=720)
    SetThermalCyclerTemp(temp=20)
    sleep(secs=45)
    return


def Resynthesis():
    PumpToFlowcell(actPos=8,
                   volume=150,
                   aspirationRate=9)
    sleep(secs=7.2)
    PumpToFlowcell(actPos=3,
                   volume=150,
                   aspirationRate=9)
    sleep(secs=7.2)
    PumpToFlowcell(actPos=6,
                   volume=180,  # todo проверить объёмы в этом пункте
                   aspirationRate=9)
    sleep(secs=18.7)
    return


def PreresynthesisTempramp():
    PumpToActuator(actPos=6)
    PumpToFlowcell(actPos=3,
                   volume=720)
    SetThermalCyclerTemp(temp=50)
    return


def Denaturation():
    SetThermalCyclerTemp(temp=20)
    sleep(secs=25)
    PumpToFlowcell(actPos=8,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=65)
    sleep(secs=60)
    PumpToActuator(actPos=3)
    PumpToFlowcell(actPos=3,
                   volume=270)
    SetThermalCyclerTemp(temp=40)
    sleep(secs=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    return


def Deprotection():
    SetThermalCyclerTemp(temp=20)
    sleep(secs=120)
    PumpToActuator(actPos=11)
    PumpToFlowcell(actPos=11,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=38)
    sleep(secs=300)
    PumpToFlowcell(actPos=11,
                   volume=90,
                   aspirationRate=9)
    sleep(secs=300)
    PumpToFlowcell(actPos=3,
                   volume=360)
    return


def IndexOnePreparation():
    SetThermalCyclerTemp(temp=20)
    sleep(secs=25)
    PumpToFlowcell(actPos=8,
                   volume=270)
    SetThermalCyclerTemp(temp=65)
    sleep(secs=60)
    PumpToActuator(actPos=13)
    SetThermalCyclerTemp(temp=40)
    sleep(secs=60)
    PumpToFlowcell(actPos=3,
                   volume=360)
    return


def FirstReadPreparation():
    PumpToFlowcell(actPos=8,
                   volume=180)
    SetThermalCyclerTemp(temp=65)
    sleep(secs=60)
    PumpToActuator(actPos=12)
    PumpToFlowcell(actPos=12,
                   volume=180)
    SetThermalCyclerTemp(temp=40)
    sleep(secs=60)
    PumpToFlowcell(actPos=3, volume=360)
    return


def SBSPrime():
    SetThermalCyclerTemp(temp=20)
    PumpToActuator(actPos=1)
    PumpToActuator(actPos=2)
    PumpToActuator(actPos=4)
    PumpToFlowcell(actPos=3,
                   volume=720)
    return


def FirstLinearisation():
    PumpToActuator(actPos=9)
    PumpToFlowcell(actPos=9,
                   volume=270,
                   aspirationRate=9)
    SetThermalCyclerTemp(temp=46)
    sleep(secs=300)
    PumpToFlowcell(actPos=9,
                   volume=90,
                   aspirationRate=9)
    sleep(secs=300)
    PumpToFlowcell(actPos=9,
                   volume=90,
                   aspirationRate=9)
    sleep(300)
    PumpToFlowcell(actPos=3,
                   volume=360)
    return


def AmplificationWash():
    PumpToFlowcell(actPos=3,
                   volume=360)
    SetThermalCyclerTemp(temp=20)

    return


def FirstExtension():
    SetThermalCyclerTemp(temp=50)
    sleep(secs=30)
    PumpToFlowcell(actPos=5,
                   volume=520,
                   aspirationRate=9)
    sleep(secs=3)
    for i in range(5):
        PumpToFlowcell(actPos=5,
                       volume=24,
                       aspirationRate=9)
    sleep(secs=90)
    return


def TMPBufferWash():
    PumpToFlowcell(actPos=3,
                   volume=24,
                   aspirationRate=9)
    sleep(secs=18)
    return


def TMP300():
    sleep(secs=300)
    SetThermalCyclerTemp(temp=40)
    sleep(300)
    return


def InitialPrime():
    PumpToActuator(actPos=8)
    SetThermalCyclerTemp(temp=40)
    sleep(secs=30)
    PumpToActuator(actPos=5)
    PumpToActuator(actPos=7)
    PumpToFlowcell(actPos=3,
                   volume=720)
    SetThermalCyclerTemp(temp=75)
    sleep(secs=30)
    PumpToActuator(actPos=17)
    PumpToFlowcell(actPos=17,
                   volume=90)
    return


def PrimePR2ByPass():
    for i in range(3):
        AspirateFromBypass(volume=60,
                           aspirationRate=72,
                           dispenseRate=2000)
    return


def FlowCheck():
    PumpToActuator(actPos=15)
    PumpToActuator(actPos=16)
    PumpToActuator(actPos=3)