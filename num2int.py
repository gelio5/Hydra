import ctypes
from bitstring import BitArray

# num1 = 24.900121688842773
# num2 = 23.712692260345423


def num2int(num):
    """
    Функция, которая вычесляет сумму байт числа для float
    """
    a = bin(ctypes.c_uint.from_buffer(ctypes.c_float(num)).value)
    a = a[2:]
    aa = []
    if len(a) < 32:
        a = (32 - len(a)) * '0' + a
    print(a[0:8], a[8:16], a[16:24], int(a[24:32]))
    for i in range(4):
        a1 = a[32 - 8 * (i + 1):32 - 8 * i]
        aa.append(BitArray(bin=a1).int)
    print(sum(aa))
    return sum(aa)
