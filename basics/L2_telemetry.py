import time as time
import L1_ina as ina

text = open("a_file.txt","w")

try:
	while True:
    		volts = str(ina.readVolts())
    		print("Volts: " + volts)
    		text.write(volts+"\n")
    		time.sleep(1)

except:
	text.close()
	print(" Terminated by Keyboard")
