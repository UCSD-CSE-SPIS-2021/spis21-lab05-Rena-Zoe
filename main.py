#print("Running lab05Warmup_Rena.py") # let us know it's running lab05Warmup_Felix.py

#import lab05Warmup_Rena              # this will cause lab05Warmup_Felix.py to run

#print("Running lab05Warmup_Zoe.py")  # let us know it's running lab05Warmup_Ryan.py

#import lab05Warmup_Zoe               # this will cause lab05Warmup_Ryan.py to run

#Gray Scale:
from PIL import Image

bear = Image.open( "bear.png" )

#def grayscale(im):
  
 #(width, height) = im.size

 #We want to be able to change the whole image or just part of an image

 #for x in range(width):
  #for y in range(height):
     #We used the same idea from the invert() in the warmup, but tried to make change based on the grayscale
    #(red, green, blue) = im.getpixel((x, y))
      
    #luminance = int(0.21*int(red) + 0.72*int(green)+ 0.07 *int(blue))
    #the luminance value that the colors, RGB, get modified by
    #bear.putpixel((x,y), (luminance, luminance, luminance))
     #(#,#,#) r b g
     #each color channel for every pixel is modified by the luminance value
#grayscale(bear)
#bear.save("bear1.png")

#binarize:
#def binarize(im, thresh, startx, starty, endx, endy):
  #(width, height) = im.size

  #for x in range(startx, endx):
    #for y in range(starty, endy):
      #(red, green, blue) = im.getpixel((x,y))
      
      #luminance = int(0.21*int(red) + 0.72*int(green)+ 0.07 *int(blue))
      #We still need the luminance because we want to be able to determine how bright each pixel is

      #if luminance > thresh:
        #bear.putpixel((x,y), (255, 255, 255))
        #We want anything above the threshhold to be white
      #else:
        #bear.putpixel((x,y), (0,0,0))
        #We want anything below the threshhold to be black
#binarize(bear, 127, 0, 0, 600, 800)
#bear.save("bear2.png")

#Vertical Mirroring

#def mirrorVert(im):
  #We want to cut the image in half (y axis) and copy each pixel from above to below
 #(width, height) = bear.size

 #for x in range(width):
  #for y in range(int(height/2)):
   #(red, green, blue) = bear.getpixel((x,y))
   #bear.putpixel((x, height-y-1), (red, green, blue))
  
#mirrorVert(bear.png)
#bear.save("bear3.png")

#def mirrorHoriz(im):
  #We want to cut the image in half (x axis) and copy each pixel from above to below
 #(width, height) = bear.size

 #for x in range(int(width/2)):
  #for y in range(height):
   #(red, green, blue) = bear.getpixel((x,y))
   #bear.putpixel((width-x-1, y), (red, green, blue))
  
#mirrorHoriz(bear.png)
#bear.save("bear4.png")

#def FlipVert(im):
  #(width, height) = bear.size
  #for x in range(width):
   #for y in range(int(height/2)):
     #Divide by 2 because the middle line is the "same", taking the top half and putting it in the bottom half, taking the bottom half and putting it in the top half
    #(temp_red, temp_green, temp_blue) = bear.getpixel((x,y))
    #We need to put new pixel into original x-place
    #bear.putpixel((x,y),(bear.getpixel((x,height-y-1))))
    #bear.putpixel((x, height-y-1), (temp_red, temp_green, temp_blue))

#FlipVert(bear.png)
#bear.save("bear5.png")
#Scale
#(temp_red, temp_green, temp_blue) = bear.getpixel((x,y))

#bear.putpixel((x, y), (bear.getpixel((x//2, y//2))))
      
#bear.putpixel((x//2, y//2), (temp_red, temp_green, temp_blue))

#if x >= 300 or y >= 401:
#bear.removepixel((x,y))

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
