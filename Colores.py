import cv2
from cv2 import cvtColor 

##capas imagenes
imagen = cv2.imread('colores.png')
#imagen=cvtColor(imagen,cv2.COLOR_BGR2RGB)
cv2.imshow('visualizacion imagen',imagen)
print(imagen[:,:,0])
cv2.imshow('Azul',imagen[:,:,0])
cv2.imshow('Verde',imagen[:,:,1])
cv2.imshow('Rojo',imagen[:,:,2])
cv2.waitKey(0)