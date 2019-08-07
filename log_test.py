# log_test.py
# -*- coding: utf-8 -*-
import struct
import sys
import num2int as nf
from bitstring import BitArray

"""
import logging

logging.basicConfig(format=u'%(asctime)s  %(levelname)-8s:  %(filename)s:%(lineno)d  %(message)s', level=logging.DEBUG, filename=u'hydra.log')

logging.debug(u'This is a debug message')
logging.info(u'This is an info message')
logging.warning(u'This is a warning')
logging.error(u'This is an error message')
logging.critical(u'FATAL')
"""

"""print("art".find("r"))
n = 23.712692260345423
print((list(struct.pack("f", n))))
print(nf.num2int(n))
print(253 % 256)
print(str(0x90).encode('ascii'))
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
