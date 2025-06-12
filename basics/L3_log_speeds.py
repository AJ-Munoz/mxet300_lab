import L1_log as log
import L2_kinematics as kin
import time

while True:
   C = kin.getPdCurrent()
   pdl = str(round(C.item(0),2))
   log.stringTmpFile(pdl, "a.txt")
   pdr = str(round(C.item(1),2))
   log.stringTmpFile(pdr, "b.txt")
   print(C)
   time.sleep(0.2)

print("SUCCESS!")