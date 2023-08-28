from PIL import Image
img = Image.new("RGB" ,(200,100) ,(255,0,0))
for x in range (200) :
    img.putpixel((x, 50) ,(0,255,0))
   
img.show( )