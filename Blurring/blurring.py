from PIL import Image

bear = Image.open( "bear.png" )

#This is very minimal blur, we will come back and make more blue
def blur(im):
 #We want to take 4 pixels in a square and turn that into 1 color to be one square
 #Think of everything in x and y
 #For loop the 4 and then moving on
  (width, height) = im.size
  temp = Image.new('RGB', (width,height))
 
  for x in range(width-1): #This will have 150 squares
   for y in range(height-1): #This will have 200 squares
    #(red, green, blue) = im.getpixel((x,y))
    #average = ((int(red) + int(green) + int(blue))//3)
    #temp.putpixel((x,y), (average,average,average))
    (red1, green1, blue1) = im.getpixel((x,y))
    (red2, green2, blue2) = im.getpixel((x+1,y))
    (red3, green3, blue3) = im.getpixel((x,y+1))
    (red4, green4, blue4) = im.getpixel((x+1,y+1))
    avg_red = (red1+red2+red3+red4)//4
    avg_green = (green1+green2+green3+green4)//4
    avg_blue = (blue1+blue2+blue3+blue4)//4
    temp.putpixel((x,y),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+1,y),(avg_red,avg_green,avg_blue))
    temp.putpixel((x,y+1),(avg_red,avg_green,avg_blue))
    temp.putpixel((x+1,y+1),(avg_red,avg_green,avg_blue))

  return temp
    #For loop - want it to take average colors of those 4 pixels and then turn all four the same color
    #Then once complete move onto the next four squares and repeat
  

blurbear = blur(bear)
blurbear.save("BlurBear.png")

