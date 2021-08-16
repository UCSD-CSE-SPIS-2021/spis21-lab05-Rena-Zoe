from PIL import Image

bear = Image.open("bear.png")

#Use the function "bear.show()" to view the modified image

#To save the the modified image use this:
#bear.save("tmp_Name.png") # create/overwrite tmp_Name.png with current image

#Basic PIL Functions

print(bear.size)
#"bear.size" tells you how many pixels are in your image

#pixel = bear.getpixel( ( 100, 200) )
#"getpixel()" allows you to look at a specific pixel (looking at x and y coordinates)

#print(pixel)
#This tells us the RBG of the code

#bear.putpixel( (100, 200), (0, 0, 0) )
#This is how we modify a pixel's color, making the pixel at 100,200 black
#"put pixel()" modifies one pixel at a time

#for i in range(100):

    #bear.putpixel( (i, 200) , (0, 0, 0) )
#This code shows that for a range of 100 (all the x's) in the y line of 200 turn it black

#bear.save("pilbasicbearzoe.png")
  #We want to see the modified Image


#Inverting the Colors
def invert( im ):

    ''' Invert the colors in the input image, im '''
    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image

    for x in range(width):

        for y in range(height):

            (red, green, blue) = im.getpixel((x, y))
            
            bear.putpixel((x, y), (255-int(red),255-int(green), 255-int(blue)))
            # Complete this function by adding your lines of code here.
            
            # You need to calculate the new pixel values and then to change them

            # in the image using putpixel()

invert(bear)
bear.save("pilbasicbearzoe.png")

#Inverting the Colors
def invert_block( im ):

    ''' Invert the colors in the input image, im '''
    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image

    for x in range(300, 600):
      #We wanted the upper right range to only invert
        for y in range(400):
          #We want only up to range 400 to invert
            (red, green, blue) = im.getpixel((x, y))
            
            bear.putpixel((x, y), (255-int(red),255-int(green), 255-int(blue)))
            # Complete this function by adding your lines of code here.
            
            # You need to calculate the new pixel values and then to change them

            # in the image using putpixel()

invert_block(bear)
bear.save("pilbasicbearzoe.png")

#After inverting the entire image then inverting just the upper right quadrant it returns the image to normal