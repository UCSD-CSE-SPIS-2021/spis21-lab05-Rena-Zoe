#binarize:

from PIL import Image

bear = Image.open( "bear.png" )

def binarize(im, thresh, startx, starty, endx, endy):
  (width, height) = im.size

  for x in range(startx, endx):
    for y in range(starty, endy):
      (red, green, blue) = im.getpixel((x,y))
      
      luminance = int(0.21*int(red) + 0.72*int(green)+ 0.07 *int(blue))
      #We still need the luminance because we want to be able to determine how bright each pixel is

      if luminance > thresh:
        #bear.putpixel((x,y), (255, 255, 255))
        #We want anything above the threshhold to be white
      else:
        #bear.putpixel((x,y), (0,0,0))
        #We want anything below the threshhold to be black
binarize(bear, 127, 0, 0, 600, 800)
bear.save("bear2.png")