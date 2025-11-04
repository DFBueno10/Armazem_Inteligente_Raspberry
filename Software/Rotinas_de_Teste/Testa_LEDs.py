from gpiozero import LED # GPIOs
from time import sleep, time # Temporizacao

# led = LED(25)
# while True:
#     led.on()
#     sleep(0.5)
#     led.off()
#     sleep(0.5)

verdes = { "Danilo":LED(23),
           "Angelo":LED(24),
           "Professor":LED(25)
         }

vermelhos = { "Danilo":LED(8),
              "Angelo":LED(7),
              "Professor":LED(1)
            }

nomes = ["Danilo", "Angelo", "Professor"]

def Piscar(led, n, t):
    for i in range(n):
        led.on()
        sleep(t/2)
        led.off()
        sleep(t/2)
        
for n in nomes:
    verdes[n].off
    
for nome in nomes:
    print(nome)
    Piscar(verdes[nome], 10, 0.2)
    Piscar(vermelhos[nome], 10, 0.2)
    
verdes["Danilo"].on()
print("ON")
sleep(5)
verdes["Danilo"].off()
print("OFF")
sleep(5)

