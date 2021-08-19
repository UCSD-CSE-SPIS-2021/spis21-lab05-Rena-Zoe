#Vertical Mirroring

from PIL import Image

bear = Image.open( "bear.png" )

def mirrorVert(im):
  #We want to cut the image in half (y axis) and copy each pixel from above to below
 (width, height) = bear.size

 for x in range(width):
  for y in range(int(height/2)):
   (red, green, blue) = bear.getpixel((x,y))
   bear.putpixel((x, height-y-1), (red, green, blue))
  
mirrorVert(bear.png)
bear.save("bear3.png")
