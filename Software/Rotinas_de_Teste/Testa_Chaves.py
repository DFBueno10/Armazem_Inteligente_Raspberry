from gpiozero import Button # GPIOs
from time import sleep, time # Temporizacao

chaves = { "Danilo":Button(17),
           "Angelo":Button(27),
           "Professor":Button(22)
         }

while True:
    print("Danilo: ", chaves["Danilo"].is_pressed)
    print("Angelo: ", chaves["Angelo"].is_pressed)
    print("Professor: ", chaves["Professor"].is_pressed)
    sleep(0.3)
