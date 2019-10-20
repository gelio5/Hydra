import pump as syringe
import actuator_lib as actuator
import sys


print(sys.argv[1])


def Actuator():
    actuator.port.isOpen()
    print(actuator.Test())
    actuator.port.close()


def pump():
    syringe.port.isOpen()
    print(syringe.Test())
    syringe.port.close()


if sys.argv[1] == 'act':
    Actuator()
elif sys.argv[1] == 'pump':
    pump()