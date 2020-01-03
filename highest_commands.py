import config
from upper_commands import BridgeAmplification
from upper_commands import BufferWash
from upper_commands import Deblock
from upper_commands import Snap
from upper_commands import EndRead
from upper_commands import IncorporationWithoutDeblockBefore
from upper_commands import IncorporationWithDeblockBefore
from upper_commands import FirstBase
from upper_commands import SecondReadPreparation
from upper_commands import SecondLinearisation
from upper_commands import PostResynthesisWash
from upper_commands import Resynthesis
from upper_commands import PreresynthesisTempramp
from upper_commands import Denaturation
from upper_commands import Deprotection
from upper_commands import IndexOnePreparation
from upper_commands import FirstReadPreparation
from upper_commands import SBSPrime
from upper_commands import FirstLinearisation
from upper_commands import AmplificationWash
from upper_commands import FirstExtension
from upper_commands import TMPBufferWash
from upper_commands import TMP300
from upper_commands import InitialPrime
from upper_commands import PrimePR2ByPass
from upper_commands import FlowCheck


def OnBoardClusterGeneration():
    config.logger.info(u'Start OnBoardClusterGeneration')
    print('Start OnBoardClusterGeneration')
    FlowCheck()
    PrimePR2ByPass()
    InitialPrime()
    TMP300()
    TMPBufferWash()
    FirstExtension()
    BridgeAmplification()
    AmplificationWash()
    FirstLinearisation()
    SBSPrime()
    config.logger.info(u'End OnBoardClusterGeneration')
    print('End OnBoardClusterGeneration')
    return


def FirstRead():
    print('Start FirstRead')
    config.logger.info(u'Start FirstRead')
    FirstReadPreparation()
    FirstBase()
    print("Детекция")
    #h = ''
    #while h != "work":
    #    h = input(">>")
    #    print(h)
    Snap()
    for i in range(249):
        Deblock()
        BufferWash()
        IncorporationWithDeblockBefore()
        Snap()
        EndRead()
    config.logger.info(u'End FirstRead')
    print('End FirstRead')
    return


def EndDeblock():
    config.logger.info(u'Start EndDeblock')
    print('Start EndDeblock')
    Deblock()
    BufferWash()
    config.logger.info(u'End EndDeblock')
    print('End EndDeblock')
    return


def IndexReadOne():
    config.logger.info(u'Start IndexReadOne')
    print('Start IndexReadOne')
    IndexOnePreparation()
    FirstBase()
    Snap()
    for i in range(7):
        Deblock()
        BufferWash()
        IncorporationWithDeblockBefore()
        Snap()
        EndRead()
    config.logger.info(u'End Start IndexReadOne')
    print('End Start IndexReadOne')
    return


def Deprotection3rdEnds():
    config.logger.info(u'Start Deprotection3rdEnds')
    print('Start Deprotection3rdEnds')
    Deprotection()
    Denaturation()
    config.logger.info(u'End Deprotection3rdEnds')
    print('End Deprotection3rdEnds')
    return


def Index2FirstBaseDark():
    config.logger.info(u'Start Index2FirstBaseDark')
    print('Start Index2FirstBaseDark')
    IncorporationWithoutDeblockBefore()
    config.logger.info(u'End Index2FirstBaseDark')
    print('End Index2FirstBaseDark')
    return


def Index2CompleteCycleDarkTwo():
    config.logger.info(u'Start Index2CompleteDarkTwo')
    print('Start Index2CompleteDarkTwo')
    Deblock()
    BufferWash()
    IncorporationWithDeblockBefore()
    config.logger.info(u'End Index2CompleteCycleDarkTwo')
    print('End Index2CompleteCycleDarkTwo')
    return


def IndexRead2():
    config.logger.info(u'Start IndexRead2')
    print('Start IndexRead2')
    for i in range(8):
        Deblock()
        BufferWash()
        IncorporationWithDeblockBefore()
        Snap()
    config.logger.info(u'End IndexRead2')
    print('End IndexRead2')
    return


def PairEndTurnAround():
    config.logger.info(u'Start PairEndTurnAround')
    print('Start PairEndTurnAround')
    PreresynthesisTempramp()
    for i in range(12):
        Resynthesis()
    PostResynthesisWash()
    SecondLinearisation()
    config.logger.info(u'End PairEndTurnAround')
    print('End PairEndTurnAround')
    return


def SecondRead():
    config.logger.info(u'Start SecondRead')
    print('Start SecondRead')
    SecondReadPreparation()
    FirstBase()
    Snap()
    for i in range(249):
        Deblock()
        BufferWash()
        IncorporationWithDeblockBefore()
        Snap()
        EndRead()
    config.logger.info(u'End SecondRead')
    print('End SecondRead')
    return
