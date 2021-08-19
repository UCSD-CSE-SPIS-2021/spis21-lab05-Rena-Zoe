from PIL import Image

bear = Image.open( "bear.png" )

def grayscale(im):
  
 (width, height) = im.size

 #We want to be able to change the whole image or just part of an image

 for x in range(width):
  for y in range(height):
     #We used the same idea from the invert() in the warmup, but tried to make change based on the grayscale
    (red, green, blue) = im.getpixel((x, y))
      
    luminance = int(0.21*int(red) + 0.72*int(green)+ 0.07 *int(blue))
    #the luminance value that the colors, RGB, get modified
    bear.putpixel((x,y), (luminance, luminance, luminance))
     #(#,#,#) r b g
     #each color channel for every pixel is modified by the luminance value
grayscale(bear)
bear.save("bear1.png")