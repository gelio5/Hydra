import serial
import ports
from system_commands import PumpToFlowcell
import logging
import time

logger = logging.getLogger()
logging.basicConfig(format=u'%(asctime)s  %(levelname)-8s  %(funcName)-24s  %('
                           u'message)s', level=logging.DEBUG,
                    filename=u'flowResetTest.log')

sensor = serial.Serial(port=ports.sensors,
                       baudrate=115200,
                       bytesize=serial.EIGHTBITS,
                       parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE)


for i in range(10):
    msg = "FLOWRST\r\n".encode()
    sensor.write(msg)
    logging.info("Xmit Sensor : %s.", msg)
    answer = sensor.readline().decode()
    logging.info("Recv Sensor : %s.", answer)
    if answer.find("error") != -1:
        sensor.write(msg)
        logging.info("Xmit Sensor : %s.", msg)
        answer = sensor.readline().decode()
        logging.info("Recv Sensor : %s.", answer)
    elif answer.find("UNDEFINED"):
        sensor.write(msg)
        logging.info("Xmit Sensor : %s.", msg)
        answer = sensor.readline().decode()
        logging.info("Recv Sensor : %s.", answer)
    rate = 300
    vol = 600
    PumpToFlowcell(actPos=3,
                   volume=vol,
                   aspirationRate=rate,
                   dispenseRate=5800)
    time.sleep(vol/rate + 0.1)