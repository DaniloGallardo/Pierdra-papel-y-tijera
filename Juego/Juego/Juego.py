import cv2
import random
import SeguimientoManos as sm  
import os
import imutils

fs = False
fu = False      
fd = False      
fj = False      
fr = False      
fgia = False    
fgus = False    
femp = False    
fder = False    
fizq = False    
conteo = 0

path = 'Imagenes'
images = []
clases = []
lista = os.listdir(path)

for lis in lista:
    imgdb = cv2.imread(f'{path}/{lis}')   
    images.append(imgdb)  
    clases.append(os.path.splitext(lis)[0])
print(clases)

cap = cv2.VideoCapture(0)

detector = sm.detectormanos(Confdeteccion=0.9)

while True: 
    ret, frame = cap.read()

    t = cv2.waitKey(1)

    al, an, c = frame.shape
    cx = int(an/2)
    cy = int(al/2)

    frame = cv2.flip(frame,1)

    frame = detector.encontrarmanos(frame, dibujar=True)
    lista1, bbox1, jug = detector.encontrarposicion(frame, ManoNum=0, dibujar=True, color = [0,255,0])

    if jug == 1:
        cv2.line(frame, (cx,0), (cx,480), (0,255,0), 2)

        cv2.rectangle(frame, (245, 25), (380, 60), (0, 0, 0), -1)
        cv2.putText(frame, '1 JUGADOR', (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.71,(0, 255, 0), 2)

        cv2.rectangle(frame, (145, 425), (465, 460), (0, 0, 0), -1)
        cv2.putText(frame, 'PRESIONA S PARA EMPEZAR', (150, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (0, 255, 0), 2)

        if t == 83 or t == 115 or fs == True:
            fs = True
            if len(lista1) != 0:
                x1, y1 = lista1[9][1:]
                if conteo <= 2:
                    img = images[conteo]
                    img = imutils.resize(img, width=240, height=240)
                    ali, ani, c = img.shape
                    if x1 < cx:
                        fizq = True
                        fder = False
                        frame[130: 130 + ali, 350: 350 + ani] = img
                        if y1 < cy - 40 and fd == False:
                            fu = True
                            cv2.circle(frame, (cx, cy), 5, (255, 255, 0), -1)

                        elif y1 > cy - 40 and fu == True:
                            conteo = conteo + 1
                            fu = False
                    elif x1 > cx:
                        fder = True
                        fizq = False
                        frame[130: 130 + ali, 30: 30 + ani] = img

                        if y1 < cy - 40 and fd == False:
                            fu = True
                            cv2.circle(frame, (cx,cy), 5, (255,255,0), -1)

                        elif y1 > cy - 40 and fu == True:
                            conteo = conteo + 1
                            fu = False

                elif conteo == 3:
                    if fj == False and fr == False:
                        juego = random.randint(3,5)
                        fj = True

                    if fizq == True and fder == False:
                        img = images[juego]
                        img = imutils.resize(img, width=240, height=240)
                        ali, ani, c = img.shape
                        frame[130: 130 + ali, 350: 350 + ani] = img
                        print(juego)
                        if fj == True and fr == False:
                            x2, y2 = lista1[8][1:]
                            x3, y3 = lista1[12][1:]
                            x4, y4 = lista1[16][1:]
                            x22, y22 = lista1[6][1:]
                            x33, y33 = lista1[10][1:]
                            x44, y44 = lista1[14][1:]
                            if x2 < x22 and x3 < x33 and x4 < x44:
                                if juego == 3:
                                    print('GANA LA IA')
                                    fgia = True
                                    fgus = False
                                    femp = False
                                    fr = True
                                elif juego == 4:
                                    print('EMPATE')
                                    fgia = False
                                    fgus = False
                                    femp = True
                                    fr = True

                                elif juego == 5:
                                    print('GANA EL HUMANO')
                                    fgia = False
                                    fgus = True
                                    femp = False
                                    fr = True
                            elif x2 > x22 and x3 > x33 and x4 > x44:
                                if juego == 3:
                                    print('EMPATE')
                                    fgia = False
                                    fgus = False
                                    fr = True
                                    femp = True
                                elif juego == 4:
                                    print('GANA EL HUMANO')
                                    fgia = False
                                    fgus = True
                                    femp = False
                                    fr = True
                                elif juego == 5:
                                    print('GANA LA IA')
                                    fgia = True
                                    fgus = False
                                    femp = False
                                    fr = True
                            elif x2 > x22 and x3 > x33 and x4 < x44:
                                if juego == 3:
                                    print('GANA EL HUMANO')
                                    fgia = False
                                    fgus = True
                                    femp = False
                                    fr = True
                                elif juego == 4:
                                    print('GANA LA IA')
                                    fgia = True
                                    fgus = False
                                    femp = False
                                    fr = True
                                elif juego == 5:
                                    print('EMPATE')
                                    fgia = False
                                    fgus = False
                                    femp = True
                                    fr = True
                        if fgia == True:
                            gan = images[6]
                            alig, anig, c = gan.shape
                            frame[70: 70 + alig, 180: 180 + anig] = gan
                            if t == 82 or t == 114:
                                fs = False
                                fu = False
                                fd = False
                                fj = False
                                fr = False
                                fgia = False
                                fgus = False
                                femp = False
                                fder = False
                                fizq = False
                                conteo = 0
                        elif fgus == True:
                            gan = images[7]
                            alig, anig, c = gan.shape
                            frame[70: 70 + alig, 180: 180 + anig] = gan
                            if t == 82 or t == 114:
                                fs = False
                                fu = False
                                fd = False
                                fj = False
                                fr = False
                                fgia = False
                                fgus = False
                                femp = False
                                fder = False
                                fizq = False
                                conteo = 0
                        elif femp == True:
                            gan = images[8]
                            alig, anig, c = gan.shape
                            frame[70: 70 + alig, 180: 180 + anig] = gan
                            if t == 82 or t == 114:
                                fs = False
                                fu = False
                                fd = False
                                fj = False
                                fr = False
                                fgia = False
                                fgus = False
                                femp = False
                                fder = False
                                fizq = False
                                conteo = 0
                    if fizq == False and fder == True:
                        img = images[juego]
                        img = imutils.resize(img, width=240, height=240)
                        ali, ani, c = img.shape
                        frame[130: 130 + ali, 30: 30 + ani] = img
                        print(juego)
                        if fj == True and fr == False:
                            x2, y2 = lista1[8][1:]
                            x3, y3 = lista1[12][1:]
                            x4, y4 = lista1[16][1:]
                            x22, y22 = lista1[6][1:]
                            x33, y33 = lista1[10][1:]
                            x44, y44 = lista1[14][1:]
                            if x2 > x22 and x3 > x33 and x4 > x44:
                                if juego == 3:
                                    print('GANA LA IA')
                                    fgia = True
                                    fgus = False
                                    femp = False
                                    fr = True
                                elif juego == 4:
                                    print('EMPATE')
                                    fgia = False
                                    fgus = False
                                    femp = True
                                    fr = True

                                elif juego == 5:
                                    print('GANA EL HUMANO')
                                    fgia = False
                                    fgus = True
                                    femp = False
                                    fr = True
                            elif x2 < x22 and x3 < x33 and x4 < x44:
                                if juego == 3:
                                    print('EMPATE')
                                    fgia = False
                                    fgus = False
                                    fr = True
                                    femp = True
                                elif juego == 4:
                                    print('GANA EL HUMANO')
                                    fgia = False
                                    fgus = True
                                    femp = False
                                    fr = True
                                elif juego == 5:
                                    print('GANA LA IA')
                                    fgia = True
                                    fgus = False
                                    femp = False
                                    fr = True
                            elif x2 < x22 and x3 < x33 and x4 > x44:
                                if juego == 3:
                                    print('GANA EL HUMANO')
                                    fgia = False
                                    fgus = True
                                    femp = False
                                    fr = True
                                elif juego == 4:
                                    print('GANA LA IA')
                                    fgia = True
                                    fgus = False
                                    femp = False
                                    fr = True
                                elif juego == 5:
                                    print('EMPATE')
                                    fgia = False
                                    fgus = False
                                    femp = True
                                    fr = True
                        if fgia == True:
                            gan = images[6]
                            alig, anig, c = gan.shape
                            frame[70: 70 + alig, 180: 180 + anig] = gan
                            if t == 82 or t == 114:
                                fs = False
                                fu = False
                                fd = False
                                fj = False
                                fr = False
                                fgia = False
                                fgus = False
                                femp = False
                                fder = False
                                fizq = False
                                conteo = 0
                        elif fgus == True:
                            gan = images[7]
                            alig, anig, c = gan.shape
                            frame[70: 70 + alig, 180: 180 + anig] = gan
                            if t == 82 or t == 114:
                                fs = False
                                fu = False
                                fd = False
                                fj = False
                                fr = False
                                fgia = False
                                fgus = False
                                femp = False
                                fder = False
                                fizq = False
                                conteo = 0
                        elif femp == True:
                            gan = images[8]
                            alig, anig, c = gan.shape
                            frame[70: 70 + alig, 180: 180 + anig] = gan
                            if t == 82 or t == 114:
                                fs = False
                                fu = False
                                fd = False
                                fj = False
                                fr = False
                                fgia = False
                                fgus = False
                                femp = False
                                fder = False
                                fizq = False
                                conteo = 0
    elif jug == 2:
        lista2, bbox2, jug2 = detector.encontrarposicion(frame, ManoNum=1, dibujar=True, color = [255,0,0])
        cv2.line(frame, (cx, 0), (cx, 240), (255, 0, 0), 2)
        cv2.line(frame, (cx, 240), (cx, 480), (0, 255, 0), 2)
        cv2.rectangle(frame, (245, 25), (408, 60), (0, 0, 0), -1)
        cv2.putText(frame, '2 JUGADORES', (250, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255, 0, 0), 2)
        cv2.rectangle(frame, (145, 425), (465, 460), (0, 0, 0), -1)
        cv2.putText(frame, 'PRESIONA S PARA EMPEZAR', (150, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255, 0, 0), 2)

        if t == 83 or t == 115:
            print('EMPEZAMOS')

    elif jug == 0:
        cv2.rectangle(frame, (225, 25), (388, 60), (0, 0, 0), -1)
        cv2.putText(frame, '0 JUGADORES', (230, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (0, 0, 255), 2)

        cv2.rectangle(frame, (115, 425), (480, 460), (0, 0, 0), -1)
        cv2.putText(frame, 'LEVANTA TU MANO PARA INICIAR', (120, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.71, (0, 0, 255), 2)


    # Mostramos frames
    cv2.imshow("JUEGO CON AI", frame)
    if t == 27:
        break
cap.release()
cv2.destroyAllWindows()
