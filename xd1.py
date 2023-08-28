from PIL import Image

def es_formato_de_imagen(filename):
    formatos_de_imagen = ['JPEG', 'PNG', 'GIF']  # Agrega otros formatos si es necesario
    try:
        img = Image.open(filename)
        return img.format in formatos_de_imagen
    except:
        return False

archivo = "D:\PC\DOCUMENTOS\Programas\PYTHON\PIL\perro.jpeg"

if es_formato_de_imagen(archivo):
    imagen = Image.open(archivo)
    # Resto de tu código aquí
    print(imagen.format)
    print(imagen.size)
    print(imagen.mode)
    imagenUno = imagen.convert('L')
    imagenUno.show()
    print(imagenUno.size, imagenUno.mode)
else:
    print("El archivo no es un formato de imagen válido.")
