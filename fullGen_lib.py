from subprocess import Popen
from subprocess import PIPE
import config
from time import sleep
import redis

connection = redis.Redis(host="127.0.0.1", port=6379, db=1)


def Snap():
    config.logger.info(u'Start Snap')
    connection.set("wParam", '0')
    command = "32860"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)
    while 1:
        wParam = int(connection.get("wParam").decode())
        if wParam == 3:
            break
        elif wParam == 4:
            lParam = int(connection.get("wParam").decode())
            print("Was founded trouble in FullGen work. ErrorType = " +
                  str(lParam))
        else:
            sleep(0.1)
    config.logger.info(u'End Snap')


def Scan():
    config.logger.info(u'Start Scan')
    connection.set("wParam", '0')
    command = "32864"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)
    while 1:
        wParam = int(connection.get("wParam").decode())
        if wParam == 3:
            break
        elif wParam == 4:
            lParam = int(connection.get("wParam").decode())
            print("Was founded trouble in FullGen work. ErrorType = " +
                  str(lParam))
        else:
            sleep(0.1)


def StartOfNewWorkCycle():
    config.logger.info(u'Restart numeration of scans')
    command = "32865"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)


def GoToLoadPos():
    config.logger.info(u'Going cell to load position')
    command = "32866"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)


def KillFullGen():
    config.logger.info(u'Quit from FullGen')
    command = "18"
    Popen(["./FullGen_send_command.exe", command], stdout=PIPE)
