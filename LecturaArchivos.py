import cv2

##Lectura de Imágenes

imagen = cv2.imread('img2.jpg')
#datos leidos
print(imagen)
#tamaño de la imagen
print(imagen.shape)

#visualizar imagen cv2.imshow('titulo ventana', imagen)
cv2.imshow('visualizacion imagen',imagen)
#waitkey para espera de tecla y cerrar ventana
cv2.waitKey(0)
#cerrar todas las ventanas
cv2.destroyAllWindows

##Guardar imagen escala de grises
imagen = cv2.imread('img2.jpg',0)
cv2.imwrite('imagenGris.png',imagen)
cv2.imshow('visualizacion imagen gris',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows

##Lectura de video
cap=cv2.VideoCapture('video.mp4')

while True:
    #.read() retorna dos valores, lectura correcta e imagen
    lec,img=cap.read()
    cv2.imshow('Video',img)
    #oprimir tecla para terminar proceso
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

#Para lectura de camara se coloca como parametro 0 en VideoCapture(0)

cap=cv2.VideoCapture(0)
#.set para modificar parametros de camara
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cap.set(cv2.CAP_PROP_BRIGHTNESS,100)
#probar con otras caracteristicas