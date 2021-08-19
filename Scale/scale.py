#Scale

from PIL import Image

bear = Image.open( "bear.png" )

def scale(im):
 
  (width, height) = im.size
  temp = Image.new('RGB', (width//2,height//2))

  for x in range(width):
    for y in range(height):
      
      temp.putpixel((x//2, y//2), im.getpixel((x, y)))
  
  return temp

minibear = scale(bear)
#Called then returns picture to Mini Bear
minibear.save("MiniBear.png")
print(minibear.size)