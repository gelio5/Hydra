# Filtration by date
"""
f = open('./Special_Post_Run_Wash/MiSeqSoftware.01.log', 'r')
a = f.readlines()
f.close()
b = open('./Special_Post_Run_Wash/lg4.log', 'w')
print(len(a))
for i in range(len(a)):
    if a[i].find("19-11-18") != -1:
        b.write(a[i])
b.close()
"""

# Status of pump filtration
f = open('./Special_Post_Run_Wash/lg4.log', 'r')
a = f.readlines()
f.close()
b = open('./Special_Post_Run_Wash/lg4.log', 'w')
for i in range(len(a) - 1):
    if i == 0:
        continue
    else:
        if a[i].find("/1Q\\r") == -1 and \
                a[i + 1].find("/0@(0x03)\\r\\n") == -1 or \
                a[i - 1].find("/1Q\\r") == -1 and \
                a[i].find("/0@(0x03)\\r\\n") == -1:
            b.write(a[i])
b.close()

# Next filtration system
"""
f = open('./Special_Post_Run_Wash/lg4.log', 'r')
a = f.readlines()
f.close()
b = open('./Special_Post_Run_Wash/lg4.log', 'w')
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
