import cv2
import numpy as np

cascade = 'Deteccao_com_webcam\Cascade\haarcascade_frontalface_default.xml'

detector_face = cv2.CascadeClassifier(cascade)

video_capture = cv2.VideoCapture(0)

#gerando captura
while True:

    ok, frame = video_capture.read()

    imagem_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    deteccoes = detector_face.detectMultiScale(imagem_cinza, minSize=(100,100))

#codigo para criação de area detectada
    for (x, y, w, h) in deteccoes:
        print(w, h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#mostrar resultado no video
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#liberando memória final
video_capture.realese()
cv2.destroyAllWindows()
