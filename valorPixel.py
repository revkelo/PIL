from PIL import Image

imagenUno = Image.open("H:/PC/Downloads/perro.jpeg")
imagen = imagenUno.convert('L')

pixeles = imagen.load()
tamano = imagen.size
anchura = tamano[0]
altura = tamano[1]

min_valor = 255  # Valor máximo inicial para escala de grises
min_pixel = None
min_x = 0
min_y = 0

for y in range(altura):
    for x in range(anchura):
        pixel = pixeles[x, y]
        if pixel < min_valor:
            min_valor = pixel
            min_pixel = (x, y)
            min_x = x
            min_y = y

print("Ubicación del pixel de menor valor:", min_pixel)
print("Valor mínimo del pixel:", min_valor)
print("Coordenadas x:", min_x)
print("Coordenadas y:", min_y)
imagen.show()
