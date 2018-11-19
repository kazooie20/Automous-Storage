import l293d
import time
# Motor 1 uses Pin 22, Pin 18, Pin 16
motor1 = l293d.DC(22,18,16)
# Run the motors so visible
for i in range(0,150):
  motor1.anticlockwise()




  
l293d.cleanup()
