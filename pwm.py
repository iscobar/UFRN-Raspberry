import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from time import sleep  # pull in the sleep function from time module  
      
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  
      
GPIO.setup(25, GPIO.OUT)# set GPIO 25 as output for white led  
GPIO.setup(24, GPIO.OUT)# set GPIO 24 as output for red led  
      
white = GPIO.PWM(25, 100)    # create object white for PWM on port 25 at 100 Hertz  
red = GPIO.PWM(24, 100)      # create object red for PWM on port 24 at 100 Hertz  
      
white.start(0)              # start white led on 0 percent duty cycle (off)  
red.start(100)              # red fully on (100%)  
      
# now the fun starts, we'll vary the duty cycle to   
# dim/brighten the leds, so one is bright while the other is dim  
      
pause_time = 0.02           # you can change this to slow down/speed up  
      
try:  
	while True: 
                for i in range(0,100):
			white.ChangeDutyCycle(i)  
			red.ChangeDutyCycle(100-i)  
			sleep(1)  
			white.ChangeDutyCycle(100-i)  
			red.ChangeDutyCycle(i)  
			sleep(1)  
	      
except KeyboardInterrupt:  
	white.stop()            # stop the white PWM output  
        red.stop()              # stop the red PWM output  
        GPIO.cleanup()          # clean up GPIO on CTRL+C exit  
