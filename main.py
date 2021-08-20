#print("Running lab05Warmup_Rena.py") # let us know it's running lab05Warmup_Felix.py

#import lab05Warmup_Rena              # this will cause lab05Warmup_Felix.py to run

#print("Running lab05Warmup_Zoe.py")  # let us know it's running lab05Warmup_Ryan.py

#import lab05Warmup_Zoe               # this will cause lab05Warmup_Ryan.py to run

from PIL import Image

bear = Image.open( "bear.png" )

#Control slash = everything highlighted = comment

#Random Grid

import random.shuffle

def grid(im, n=25):
  #Giving image and number
    #They can set n to something else in their parameter, but for default this would make it split by 25

  #Convenient constants
  (width, height) = im.size
  num_blocks_x = width//n
  num_blocks_y = height//n

  #Shuffle input blocks to get output blocks
  blocks_nums = list(range(num_blocks_x*num_blocks_y))
  random.shuffle(in_block_nums)
  #We can then randomly shuffle the list to tell us where to copy over
  temp = Image.new('RGB', (width,height))

  #For each block of output, copy from input
  for out_block_num in range(num_blocks_x*num_blocks_y):
    in_block_nums = in_block_nums[out_block_num]
    #copy inblocknum to the corresponding output block
  return

  #Number of vertical blocks you have is height//n
    #This splits up how many blocks height-wise you will have, and you can do the same with width
