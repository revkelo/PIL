from PIL import Image

# Open the images
image_path1 = "H:/PC/Downloads/perro1.jpeg"
image_path2 = "H:/PC/Downloads/perro.jpeg"

# Open and convert the images to grayscale
image1 = Image.open(image_path1).convert('L')
image2 = Image.open(image_path2).convert('L')

# Get pixel data and image sizes
pixels1 = image1.load()
pixels2 = image2.load()
size1 = image1.size
size2 = image2.size
width1, height1 = size1
width2, height2 = size2

# Check if the image sizes are the same
if size1 != size2:
    print("Las dos imágenes tienen diferente tamaño")
else:
    # Find differing pixels
    differing_pixels = []
    for x in range(width1):
        for y in range(height1):
            pixel1 = pixels1[x, y]
            pixel2 = pixels2[x, y]
            if pixel1 != pixel2:
                differing_pixels.append(((x, y), pixel1, pixel2))

    if not differing_pixels:
        print("Las imágenes son idénticas")
    else:
        
        for coords, pixel1, pixel2 in differing_pixels:
            print(f"Coordenadas: {coords}, Imagen 1: {pixel1}, Imagen 2: {pixel2}")
    print("Las imágenes no son idénticas. Píxeles diferentes:")
