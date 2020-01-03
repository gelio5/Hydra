# Filtration by date

f = open('hydra.log', 'r')
a = f.readlines()
f.close()
b = open('hydra_full_02.log', 'w')
print(len(a))
for i in range(len(a)):
    if a[i].find("2019-12-21") != -1 or a[i].find("2019-12-22") != -1 or a[i].find("2019-12-23") != -1 or a[i].find("2019-12-24") != -1:
        b.write(a[i])
b.close()

"""
# Status of pump filtration
f = open('./Cycle_Log/lg1.log', 'r')
a = f.readlines()
f.close()
b = open('./Cycle_Log/lg1.log', 'w')
for i in range(len(a) - 1):
    if i == 0:
        continue
    else:
        if (a[i].find("/1Q\\r") != -1 and a[i + 1].find("/0@(0x03)\\r\\n") != -1) or (a[i - 1].find("/1Q\\r") != -1 and a[i].find("/0@(0x03)\\r\\n") != -1):
            continue
        else:
            b.write(a[i])
b.close()
"""
"""
# Next filtration system

f = open('./Cycle_Log/Cycle1_Log.00.log', 'r')
a = f.readlines()
f.close()
b = open('./Cycle_Log/lg1.log', 'w')
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
