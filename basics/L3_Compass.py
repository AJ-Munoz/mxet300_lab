import L2_compass_heading as compass
import L1_log as log
import time

def Cardinal(theta):
   if theta>-45 and theta<45:
     return "North"
   elif theta>45 and theta<135:
      return "West"
   elif theta>135 and theta<225:
      return "South"
   else:
      return "East"

try:
   while True:
      heading = compass.get_heading()
      log.tmpFile(heading,"head_variable.txt")
      log.stringTmpFile(Cardinal(heading),"head_str.txt")
      print(Cardinal(heading))
      time.sleep(0.1)

except:
   print("\n\n Bye Bye ,,,=^..^=,,")