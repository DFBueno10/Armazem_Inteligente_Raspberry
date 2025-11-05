import requests # Lidar com protocolo HTTP
import datetime # Datas, horarios
from gpiozero import LED, Button # GPIOs
from adafruit_servokit import ServoKit # PCA9685
from time import sleep, time # Temporizacao
import face_recognition # Reconhecimento Facial
import cv2
import numpy as np # Numpy
from picamera2 import Picamera2
import pickle
# -------------------- Fim Bibliotecas --------------------

# -------------------- Variaveis Globais --------------------
nomes = ["Danilo", "Angelo", "Professor"]
status = { "Danilo":1,
           "Angelo":1,
           "Professor":1
         }
# Posicoes dos servos:
POS_A = 178
POS_F = 120
# Camera:
cv_scaler = 4 # this has to be a whole number

face_locations = []
face_encodings = []
face_names = []
frame_count = 0
start_time = time()
fps = 0
# Ubidots:
TOKEN = "BBUS-O9gbiSyONRtSLih9u5wy9SASYAtMKl" # Token
DEVICE_LABEL = "cofre" # Nome
URL = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}" # URL
HEADERS = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"} # Cabecalho do json
nomes_payload = { "Danilo": "Status_1",
                 "Angelo" : "Status_2",
                 "Professor": "Status_3"
              }

TD = 20 # Janela de detectcao (s)
last_time = time() - TD # Ultimo instante que alguem passou em frente ao sensor
# -------------------- Fim Variaveis Globais --------------------

# -------------------- Mapeamento de Hardware --------------------
# Saidas:
verdes = { "Danilo":LED(23),
           "Angelo":LED(24),
           "Professor":LED(25)
         }
vermelhos = { "Danilo":LED(8),
              "Angelo":LED(7),
              "Professor":LED(1)
            }
# Entradas:
D80NK = Button(5) # Sensor D80NK
chaves = { "Danilo":Button(17),
           "Angelo":Button(27),
           "Professor":Button(22)
         }

kit = ServoKit(channels=16)
servos = { "Danilo":kit.servo[6],
           "Angelo":kit.servo[7],
           "Professor":kit.servo[8]
         }
# -------------------- Fim Mapeamento de Hardware --------------------

# -------------------- Funcoes e Procedimentos --------------------
def Mover_Servo(canal, pi, pf):
    for pos in range(pi, pf+1, 1):
        canal.angle = pos # Incrementa a posicao
        sleep(0.01) # Atraso
    for pos in range(pi, pf+1, -1):
        canal.angle = pos # Incrementa a posicao
        sleep(0.01) # Atraso
    canal.angle = pos # Fixa a posicao final
    
def Fechar(nome):
    if nome == "Angelo":
        Mover_Servo(servos[nome], 129, 80)
    else:
        Mover_Servo(servos[nome], POS_A, POS_F)

def Abrir(nome):
    if nome == "Angelo":
        Mover_Servo(servos[nome], 80, 129)
    else:
        Mover_Servo(servos[nome],POS_F, POS_A)

def Retirar_Gaveta(nome):
    print("Bem-vindo, ", nome)
    Abrir(nome)
    print("Gaveta Liberada")
    vermelhos[nome].off()
    verdes[nome].off()
    #Enviar_Status_Gaveta(nome, 0)
    start = time()
    while time() - start <= 5:
        vermelhos[nome].toggle()
        verdes[nome].toggle()
        print("Retire sua maleta...")
        if chaves[nome].is_pressed == 0:
            status[nome] = 0 # Retirou a gaveta
            break
        sleep(0.1)
    vermelhos[nome].off()
    verdes[nome].off()
    if status[nome] == 1:
        print("Gaveta nao retirada")
        print("Travando...")
        Fechar(nome)
        vermelhos[nome].off()
        verdes[nome].on()
        Enviar_Status_Gaveta(nome, 1)
    else:
        print("Gaveta Retirada")
        vermelhos[nome].on()
        verdes[nome].off()
        Enviar_Status_Gaveta(nome, 0)

def send_to_ubidots(data: dict):
    try:
        r = requests.post(URL, json=data, headers=HEADERS, timeout=5)
        print(f"Status {r.status_code} | {r.text}")
    except Exception as e:
        print("Erro ao enviar:", e)
        
def Enviar_Status_Gaveta(nome, status):
    payload = {nomes_payload[nome]:status}
    send_to_ubidots(payload)
# Camera:
def process_frame(frame):
    global face_locations, face_encodings, face_names
    
    # Resize the frame using cv_scaler to increase performance (less pixels processed, less time spent)
    resized_frame = cv2.resize(frame, (0, 0), fx=(1/cv_scaler), fy=(1/cv_scaler))
    
    # Convert the image from BGR to RGB colour space, the facial recognition library uses RGB, OpenCV uses BGR
    rgb_resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)    
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_resized_frame)
    face_encodings = face_recognition.face_encodings(rgb_resized_frame, face_locations, model='large')
    
    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    
    return frame

def draw_results(frame):
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled
        top *= cv_scaler
        right *= cv_scaler
        bottom *= cv_scaler
        left *= cv_scaler
        
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (244, 42, 3), 3)
        
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left -3, top - 35), (right+3, top), (244, 42, 3), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, top - 6), font, 1.0, (255, 255, 255), 1)
    
    return frame

def calculate_fps():
    global frame_count, start_time, fps
    frame_count += 1
    elapsed_time = time() - start_time
    if elapsed_time > 1:
        fps = frame_count / elapsed_time
        frame_count = 0
        start_time = time()
    return fps
# -------------------- Fim Funcoes e Procedimentos --------------------

# -------------------------- Setup --------------------------
# Load pre-trained face encodings
print("[INFO] loading encodings...")
with open("encodings.pickle", "rb") as f:
    data = pickle.loads(f.read())
known_face_encodings = data["encodings"]
known_face_names = data["names"]
# Iniciar a camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (800, 480)}))
picam2.start()

for nome in nomes:
    verdes[nome].on()
    vermelhos[nome].off()
    Fechar(nome)
    #servos[nome].angle = 0
    Enviar_Status_Gaveta(nome, 1)
    sleep(0.5)

start_time = time()
last_time = time() - TD - 1 # Ultimo instante que alguem passou em frente ao sensor
# -------------------------- Fim Setup --------------------------

while True:
    print("Rotina")
    if D80NK.is_pressed: # Alguem na frente do sensor!
        print("Pessoa detectada!")
        last_time = time()
    else: # Ninguem :(
        print("Waiting for someone...")
    while time() - last_time <= TD: # Janela de deteccao
        frame = picam2.capture_array() # Captura uma imagem
        processed_frame = process_frame(frame) # Processa a imagem
        # Get the text and boxes to be drawn based on the processed frame
        display_frame = draw_results(processed_frame)
        current_fps = calculate_fps() # Atualiza o FPS    
        # Attach FPS counter to the text and boxes
        cv2.putText(display_frame, f"FPS: {current_fps:.1f}", (display_frame.shape[1] - 150, 30), 
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Video', display_frame) # Exibe tudo
        # Break the loop and stop the script if 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
            break
        nome = ""
        detectado = False
        for nome in nomes:
            if nome in face_names: # Detectou alguem!
                print(f"{nome} detectado!")
                detectado = True
                break # Sai do laco
        if detectado and status[nome]: # Detectou e a gaveta esta no lugar
            Retirar_Gaveta(nome) # Libera a gaveta correspondente
        last_time = last_time - TD
        sleep(0.12)
    for nome in nomes:
        if status[nome] == 0 and chaves[nome].is_pressed: # Alguem colocou a gaveta no lugar
            print("Obrigado, ", nome)
            print("Gaveta devolvida")
            sleep(0.5)
            Fechar(nome)
            vermelhos[nome].off()
            verdes[nome].on()
            status[nome] = 1 # Atualiza o status da gaveta
            Enviar_Status_Gaveta(nome, 1)
    sleep(0.15)
#Retirar_Gaveta("Danilo")

while True:
    for nome in nomes:
        if status[nome] == 0 and chaves[nome].is_pressed: # Alguem colocou a gaveta no lugar
            print("Obrigado, ", nome)
            print("Gaveta devolvida")
            sleep(0.5)
            Mover_Servo(servos[nome], POS_A, POS_F)
            vermelhos[nome].off()
            verdes[nome].on()
            status[nome] = 1 # Atualiza o status da gaveta
            Enviar_Status_Gaveta(nome, 1)
    sleep(0.1)

