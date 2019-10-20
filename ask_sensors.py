import time
import sensors_lib
i: int = 0
while 1:
    sensors_lib.AskSensors()
    time.sleep(0.5)
    i += 1
    print(i)
