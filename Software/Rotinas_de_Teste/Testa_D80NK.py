from gpiozero import Button # Library for GPIO
from time import sleep, time # Library for time functions


# Hardware map:
D80NK = Button(5)
#--------------------

# Global parameters:
DT = 20 # Maximum detection time in seconds
#-------------------
last_time = time() - DT# Last time a person was in front of the sensor
print("Starting...")
sleep(1)
while True:
    print(time())
    if D80NK.is_pressed: # Person in front of the sensor
        print("Person detected!")
        last_time = time()
    else: # Nobody :(
        print("Waiting for someone...")
    while time() - last_time <= DT: # Detection time!
        print("Trying for matches...")
        sleep(0.1)
    sleep(0.1) # Wait 0.1 s (10 Hz rate) 
