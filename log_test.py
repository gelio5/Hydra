# log_test.py
# -*- coding: utf-8 -*-
import struct
import sys
import num2int as nf
from bitstring import BitArray
import stand_cooler_lib
from struct import *
import time
import sensors_lib as sensors

"""
import logging

logging.basicConfig(format=u'%(asctime)s  %(levelname)-8s:  %(filename)s:%(lineno)d  %(message)s', level=logging.DEBUG, filename=u'hydra.log')

logging.debug(u'This is a debug message')
logging.info(u'This is an info message')
logging.warning(u'This is a warning')
logging.error(u'This is an error message')
logging.critical(u'FATAL')
"""
"""test_recv = b'\x08\x14\xbd\x9c\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x07\x02\x00\x00\x7b'
test_answer = unpack("<BBBiiiBBBBB", test_recv)
for i in range(len(test_answer)):
    print(str(test_answer[i]) + " - " + str(type(test_answer[i])) + " - " + str(sys.getsizeof(test_answer[i])))
print(test_answer)
a = 1
print(type(a))
print(sys.getsizeof(a))
print(test_answer[0] + test_answer[1] + test_answer[2] +
      test_answer[6] + test_answer[7] + test_answer[8] + test_answer[9])
print(stand_cooler_lib.IntToSumOfBytes(test_answer[3]))
print((test_answer[0] +
      test_answer[1] +
      test_answer[2] +
      stand_cooler_lib.IntToSumOfBytes(test_answer[3]) +
      stand_cooler_lib.IntToSumOfBytes(test_answer[4]) +
      stand_cooler_lib.IntToSumOfBytes(test_answer[5]) +
      test_answer[6] +
      test_answer[7] +
      test_answer[8] +
      test_answer[9]) % 256 == test_answer[10])"""
# print(stand_cooler_lib.IntToSumOfBytes(3245245))
"""print("art".find("r"))
n = 23.712692260345423
print((list(struct.pack("f", n))))
print(nf.num2int(n))
print(253 % 256)
print(str(0x90).encode('ascii'))
"""
"""
f = open('./Post_Run_Wash/MiSeqSoftware.00.log', 'r')
a = f.readlines()
f.close()
b = open('./Post_Run_Wash/lg4.log', 'w')
print(len(a))
for i in range(len(a)):
    if a[i].find("19-08-07") != -1:
        b.write(a[i])
b.close()
f = open('./Post_Run_Wash/lg4.log', 'r')
a = f.readlines()
f.close()
b = open('./Post_Run_Wash/lg4.log', 'w')
print(len(a))
for i in range(len(a)):
    if a[i].find("FPGA") == -1 and\
            a[i].find("LED") == -1 and\
            a[i].find("Instrument") == -1 and\
            a[i].find("Motor") == -1 and\
            a[i].find("Camera") == -1 and\
            a[i].find("Sensor") == -1 and\
            a[i].find("Control") == -1:
        b.write(a[i])
b.close()

"""
"""
print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('d'))
print(chr(96))
print(chr(64))
a = True
print(sys.getsizeof(a))
print(sys.getsizeof(ord('@')))
"""


sensors.AskSensors()
time.sleep(1)
sensors.AskSensors()
time.sleep(1)
sensors.AskSensors()
