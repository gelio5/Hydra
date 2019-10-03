import time
from lib import sensors_lib
for i in range(100):
    sensors_lib.AskSensors()
    print(i)
    time.sleep(0.5)
