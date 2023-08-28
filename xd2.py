# Script 01 - Mostrar la matriz de pixeles
from PIL import Image
imagenUno = Image.open("H:\PC\Downloads\perro.jpeg")
imagen = imagenUno.convert('L')

pixeles = imagen.load()
tamano = imagen.size
anchura = tamano [0]
altura = tamano [1]
print (anchura)
print (altura)
for x in range (anchura) :
    for y in range (altura) :
        pixel = pixeles [x, y]
        print (pixel)
imagen.show()