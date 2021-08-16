
from PIL import Image

bear = Image.open( "bear.png" )

#Basic PIL Functions:
#bear.size
#this command shows how many pixels are in the image
#pixel = bear.getpixel( ( 100, 200) )
#this step stores the RGB value of the pixel at x=100 and y=200 in the "pixel" variable
#print(pixel)
#prints the tuple which contains the RGB value of "pixel"
#bear.putpixel( (100, 200), (0, 0, 0) )
#changes the picel color of x=100 and y=200 to black
#for i in range(200):
    #bear.putpixel( (i, 200) , (0, 0, 0) )
#makes a horizontal black line

#bear.save("pilbasicbearrena.png")


#Inverting the colors:
def invert( im ):

    ''' Invert the colors in the input image, im '''

    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image

    for x in range(width):

        for y in range(height):

            (red, green, blue) = im.getpixel((x, y))
            
            bear.putpixel((x, y), (255-int(red),255-int(green), 255-int(blue)))
            #by doing 255 minus the original RGB values o the image, it inverts the color of all the pixels in the image 

invert(bear)
#calls the function
bear.save("pilbasicbearrena.png")
#saves the modified image into a different file so we could view the changes

def invert_block( im ):
  for x in range(300, 600):
  #for x values from 300 to 600; this is the right portion of the image

    for y in range(400):
    #for y values from 0 to 400; this gets right upper part of the image
    #so only the upper right portion of the image will have its color inverted instead of the whole image
      (red, green, blue) = im.getpixel((x, y))
            
      bear.putpixel((x, y), (255-int(red),255-int(green), 255-int(blue)))

invert_block(bear)
bear.save("pilbasicbearrena.png")
#Rena is Cool - Zoe