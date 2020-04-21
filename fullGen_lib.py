from subprocess import Popen
from subprocess import PIPE
import config
from time import sleep


def Snap():
    config.logger.info(u'Start Snap')
    command = "32860"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)
    sleep(3.5)
    config.logger.info(u'End Snap')


def Scan():
    config.logger.info(u'Start Scan')
    command = "32864"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)


def StartOfNewWorkCycle():
    config.logger.info(u'Restart numeration of scans')
    command = "32865"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)


def GoToLoadPos():
    config.logger.info(u'Going cell to load position')
    command = "32866"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)
