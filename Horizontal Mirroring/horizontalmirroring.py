#Horizontal Mirroring

from PIL import Image

bear = Image.open( "bear.png" )
def mirrorHoriz(im):
  #We want to cut the image in half (x axis) and copy each pixel from above to below
 (width, height) = bear.size

 for x in range(int(width/2)):
  for y in range(height):
   (red, green, blue) = bear.getpixel((x,y))
   bear.putpixel((width-x-1, y), (red, green, blue))