# Imports necessários para o programa
import cv2
import mediapipe as mp
# Import da biblioteca serial, que fará a comunicação com o Arduino
import serial

def envia_valor(contador):
    # Substitua 'COM3' pela porta serial correta do Arduino
    porta_serial = serial.Serial('COM1', 9600)  

    porta_serial.write(bytes([contador]))  # Envia o valor

    # Fecha a comunicação serial quando terminar
    porta_serial.close()  

def detecta_maos(img):
    # Prepara o frame
    frameRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # Processa o frame
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if handPoints:
        for points in handPoints:
            mpDwaw.draw_landmarks(img, points,hands.HAND_CONNECTIONS)
            # Enumera os pontos das mãos
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                # Adiciona os pontos à lista
                pontos.append((cx,cy))

            # Pontos de interesse nas mãos
            dedos = [8,12,16,20]

            # Inicializa o contador de dedos
            contador = 0

            # De acordo com cálculos de distância entre os pontos, indica quantos estão "em pé"
            if pontos:
                if pontos[4][0] < pontos[3][0]:
                    contador += 1
                for x in dedos:
                   if pontos[x][1] < pontos[x-2][1]:
                       contador +=1

            # Indica na tela a quantidade de dedos
            cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
            
            # Chama o método que enviará dados para o arduino, comentado para testes sem a placa, favor descomentar
            envia_valor(contador)

    cv2.imshow('Resultado',img)

# Entrada de vídeo, 0 para vídeo integrado (webcam), caminho completo do vídeo para gravação
video = cv2.VideoCapture('video.mp4')

# Variáveis para iniciar a detecção de mãos
hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mpDwaw = mp.solutions.drawing_utils

# Loop até cancelamento manual do usuário ou fim da gravação
while True:
    success, img = video.read()

    # Para comparar, descomente as próximas linhas:
    #preview = img
    #cv2.imshow('Preview',preview)
    
    # Chama o método de detectar gestos a cada frame
    detecta_maos(img)

    # Espera uma entrada do usuário
    key = cv2.waitKey(20)
    if key == 27: # ESC para sair
        break

# Encerra o programa
cv2.destroyAllWindows()
video.release()