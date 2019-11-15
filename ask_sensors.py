"""import time
import sensors_lib
i: int = 0
while 1:
    sensors_lib.AskSensors()
    time.sleep(0.5)
    i += 1
    print(i)"""

import time
import redis
import sensors_lib

conn = redis.Redis(host='127.0.0.1', port=6379, db=1)
bubble_on = 0 # пузыри включены
bubble_need = 0 # пузырьки должны быть включены
conn.set("bubble_need", bubble_need)
conn.set("bubble_on", bubble_on)
counter = 0
while 1:
    data = sensors_lib.AskSensors()
    data = dict(item.split("=") for item in data.split(" "))
    conn.hmset("sensors", data)
    if conn.get("bubble_need").decode() == '1' and\
            conn.get("bubble_on").decode() == "0":
        sensors_lib.BubOn()
        conn.set("bubble_on", 1)
    if conn.get("bubble_need").decode() == '0' and\
            conn.get("bubble_on").decode() == "1":
        sensors_lib.BubOff()
        conn.set("bubble_on", 0)
    if counter != 10:
        counter += 1
    else:
        counter = 1
        if conn.get("bubble_need").decode() == '1' and \
                conn.get("bubble_on").decode() == "1":
            sensors_lib.BubAsk()
    # TODO: add inversion for some sensors data
    # print(data)

    time.sleep(0.5)
