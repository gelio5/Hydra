from upper_commands import End
from highest_commands import OnBoardClusterGeneration
from highest_commands import FirstRead
from highest_commands import EndDeblock
from highest_commands import IndexReadOne
from highest_commands import Deprotection3rdEnds
from highest_commands import Index2FirstBaseDark
from highest_commands import Index2CompleteCycleDarkTwo
from highest_commands import IndexRead2
from highest_commands import PairEndTurnAround
from highest_commands import SecondRead
from stand_cooler_lib import SetStandDown
from stand_cooler_lib import SetStandUp
import time
import redis

conn = redis.Redis(host='127.0.0.1', port=6379, db=1)

print("Старт")
n = time.time()
SetStandDown()
time.sleep(7)
print("Установите на рабочее место штатив с реагентами и чип")
h = ''
while h != "work":
    h = input(">>")
    print(h)
SetStandUp()
time.sleep(7)
print("Начало отрабатывания циклограммы")
conn.set("bubble_need", 1)

print("OnBoardClusterGeneration")
OnBoardClusterGeneration()
print("First Read")
FirstRead()
print("EndDeblock")
EndDeblock()
print("Index Read One")
IndexReadOne()
print("EndDeblock")
EndDeblock()
print("Deprotection 3rd Ends")
Deprotection3rdEnds()
print("Index2FirstBaseDark")
Index2FirstBaseDark()
for j in range(6):
    print(str(j+1) + "Index2CompleteCycleDarkTwo")
    Index2CompleteCycleDarkTwo()
print("IndexRead2")
IndexRead2()
print("EndDeblock")
EndDeblock()
print("PairEndTurnAround")
PairEndTurnAround()
print("SecondRead")
SecondRead()
print("EndDeblock")
EndDeblock()
print('End')
End()
conn.set("bubble_need", 0)
print(time.time()-n)
print("ENDED")
