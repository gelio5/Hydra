# log_test.py
# -*- coding: utf-8 -*-
import struct
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

print("art".find("r"))
n = 23.712692260345423
print((list(struct.pack("f", n))))
print(nf.num2int(n))
print(253 % 256)
print(str(0x90).encode('ascii'))
