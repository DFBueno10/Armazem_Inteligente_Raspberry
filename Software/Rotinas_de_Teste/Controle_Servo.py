from adafruit_servokit import ServoKit # PCA9685
from time import sleep

kit = ServoKit(channels=16)
servos = { "Danilo":kit.servo[6],
           "Angelo":kit.servo[7],
           "Professor":kit.servo[8]
         }

def Mover_Servo(canal, pi, pf):
    for pos in range(pi, pf+1, 1):
        canal.angle = pos # Incrementa a posicao
        sleep(0.01) # Atraso
    for pos in range(pi, pf+1, -1):
        canal.angle = pos # Incrementa a posicao
        sleep(0.01) # Atraso
    canal.angle = pos # Fixa a posicao final
    
nome = "Angelo"
#servos[nome].angle = 180
sleep(0.5)
Mover_Servo(servos[nome], 80,100)

# 120 fechado 80
# 180 aberto
