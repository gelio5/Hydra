import ctypes
from bitstring import BitArray


def IntToSumOfBytes(num: int) -> int:
    """
    Функция, которая вычесляет сумму байт числа для integer
    """
    numInBinary = bin(ctypes.c_uint.from_buffer(ctypes.c_int(num)).value)[2:]
    if len(numInBinary) < 32:
        numInBinary = (32 - len(numInBinary)) * '0' + \
                      numInBinary
    numInBytes = [BitArray(bin=numInBinary[0:8]).uintbe,
                  BitArray(bin=numInBinary[8:16]).uintbe,
                  BitArray(bin=numInBinary[16:24]).uintbe,
                  BitArray(bin=numInBinary[24:32]).uintbe]
    return sum(numInBytes) % 256


def FloatToSumOfBytes(num: float) -> int:
    """
    Функция, которая вычесляет сумму байт числа для float
    """
    numInBinary = bin(ctypes.c_uint.from_buffer(ctypes.c_float(num)).value)[2:]
    if len(numInBinary) < 32:
        numInBinary = (32 - len(numInBinary)) * '0' + numInBinary
    numInBytes = [BitArray(bin=numInBinary[0:8]).uintbe,
                  BitArray(bin=numInBinary[8:16]).uintbe,
                  BitArray(bin=numInBinary[16:24]).uintbe,
                  BitArray(bin=numInBinary[24:32]).uintbe]
    return sum(numInBytes) % 256