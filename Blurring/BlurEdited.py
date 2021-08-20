from PIL import Image

bear = Image.open( "bear.png" )

#Edited one that takes too long
def blur(im):
 #Zoe wanted 25 pixels in a square and turn that into 1 color to be one square
 #Think of everything in x and y
 #For loop the 25 and then moving on
  (width, height) = im.size
  temp = Image.new('RGB', (width,height))
 
  for x in range(width-5): #This will have 150 squares
   for y in range(height-5): #This will have 200 squares

    #We did -5 because it's the number of rows and ensures it stays within bounds of the image

    #(red, green, blue) = im.getpixel((x,y))
    #average = ((int(red) + int(green) + int(blue))//3)
    #temp.putpixel((x,y), (average,average,average))

    #Zoe made the code Rena came up with longer in an effort to make the bear more blury. I made a table of 5 by 5 and figured out what I would need to add to x and y to fill the table.
    #Row 1
    (red1, green1, blue1) = im.getpixel((x,y))
    (red1a, green1a, blue1a) = im.getpixel((x+1,y))
    (red1b, green1b, blue1b) = im.getpixel((x+2,y))
    (red1c, green1c, blue1c) = im.getpixel((x+3,y))
    (red1d, green1d, blue1d) = im.getpixel((x+4,y))
    #Row 2
    (red2, green2, blue2) = im.getpixel((x,y+1))
    (red2a, green2a, blue2a) = im.getpixel((x+1,y+1))
    (red2b, green2b, blue2b) = im.getpixel((x+2,y+1))
    (red2c, green2c, blue2c) = im.getpixel((x+3,y+1))
    (red2d, green2d, blue2d) = im.getpixel((x+4,y+1))
    #Row 3
    (red3, green3, blue3) = im.getpixel((x,y+2))
    (red3a, green3a, blue3a) = im.getpixel((x+1,y+2))
    (red3b, green3b, blue3b) = im.getpixel((x+2,y+2))
    (red3c, green3c, blue3c) = im.getpixel((x+3,y+2))
    (red3d, green3d, blue3d) = im.getpixel((x+4,y+2))
    #Row 4
    (red4, green4, blue4) = im.getpixel((x,y+3))
    (red4a, green4a, blue4a) = im.getpixel((x+1,y+3))
    (red4b, green4b, blue4b) = im.getpixel((x+2,y+3))
    (red4c, green4c, blue4c) = im.getpixel((x+3,y+3))
    (red4d, green4d, blue4d) = im.getpixel((x+4,y+3))
    #Row 5
    (red5, green5, blue5) = im.getpixel((x,y+4))
    (red5a, green5a, blue5a) = im.getpixel((x+1,y+4))
    (red5b, green5b, blue5b) = im.getpixel((x+2,y+4))
    (red5c, green5c, blue5c) = im.getpixel((x+3,y+4))
    (red5d, green5d, blue5d) = im.getpixel((x+4,y+4))
    #Averages of above ^
    #We wanted the average of each color so I added all of the new red, green, and blue things I made into this and then divided by the amount (25)
    avg_red = (red1+red1a+red1b+red1c+red1d+red2+red2a+red2b+red2c+red2d+red3+red3a+red3b+red3c+red3d+red4+red4a+red4b+red4c+red4d+red5+red5a+red5b+red5c+red5d)//25
    avg_green = (green1+green1a+green1b+green1c+green1d+green2+green2a+green2b+green2c+green2d+green3+green3a+green3b+green3c+green3d+green4+green4a+green4b+green4c+green4d+green5+green5a+green5b+green5c+green5d)//25
    avg_blue = (blue1+blue1a+blue1b+blue1c+blue1d+blue2+blue2a+blue2b+blue2c+blue2d+blue3+blue3a+blue3b+blue3c+blue3d+blue4+blue4a+blue4b+blue4c+blue4d+blue5+blue5a+blue5b+blue5c+blue5d)//25
    #Next I organized how the sorted the putpixels by row This gives puts the average color into the 25 pixels chosen
    #Row 1 temp.putpixels
    temp.putpixel((x,y),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+1,y),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+2,y),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+3,y),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+4,y),(avg_red,avg_green,avg_blue))
    #Row 2 temp.putpixels
    temp.putpixel((x,y+1),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+1,y+1),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+2,y+1),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+3,y+1),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+4,y+1),(avg_red,avg_green,avg_blue))
    #Row 3 temp.putpixels
    temp.putpixel((x,y+2),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+1,y+2),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+2,y+2),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+3,y+2),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+4,y+2),(avg_red,avg_green,avg_blue))
    #Row 4 temp.putpixels
    temp.putpixel((x,y+3),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+1,y+3),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+2,y+3),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+3,y+3),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+4,y+3),(avg_red,avg_green,avg_blue))
    #Row 5 temp.putpixels
    temp.putpixel((x,y+4),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+1,y+4),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+2,y+4),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+3,y+4),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+4,y+4),(avg_red,avg_green,avg_blue))

  return temp
    #For loop - want it to take average colors of those 4 pixels and then turn all four the same color
    #Then once complete move onto the next four squares and repeat
  

blurbear = blur(bear)
blurbear.save("BlurBearEdited.png")