import time as time
import L1_ina as ina

try:
   while True:
      volts = round(float(ina.readVolts()),2)
      print("Volts: " + str(volts))
      text = open("Lab2_file.txt","w")
      text.flush()
      text.write(str(volts))
      text.flush()
      text.close()
      time.sleep(0.2)

except:
      text.close()
      print(" Don")
