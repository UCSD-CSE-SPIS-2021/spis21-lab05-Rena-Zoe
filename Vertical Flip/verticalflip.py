#Vertical Flip
from PIL import Image

bear = Image.open( "bear.png" )

def FlipVert(im):
  (width, height) = bear.size
  for x in range(width):
   for y in range(int(height/2)):
     #Divide by 2 because the middle line is the "same", taking the top half and putting it in the bottom half, taking the bottom half and putting it in the top half
    (temp_red, temp_green, temp_blue) = bear.getpixel((x,y))
    #We need to put new pixel into original x-place
    bear.putpixel((x,y),(bear.getpixel((x,height-y-1))))
    bear.putpixel((x, height-y-1), (temp_red, temp_green, temp_blue))

FlipVert(bear.png)
bear.save("bear5.png")