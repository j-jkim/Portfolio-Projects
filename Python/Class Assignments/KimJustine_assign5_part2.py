# Name: Justine Kim     # Date: 3/20/19
# NetID: jk5565         # Section: CSCI-UA.0002-1
# Assignment 5          # Program: Kilim Carpets


## spaced rectanges - tails of carpet
current = 0
while current < 2:
   current += 1
   for spaced_stars in range(25):
      print("*",end=' ')
   print()

## rectangle
for stars in range(49):
   print("*",end='')
print()

for stars in range(49):
   print("*",end='')
print()


## checkerboard 
count = 0
for stars in range(24):
   count+=1
   print("*",end='')
   while (count%3)==0:
      for space in range(3):
         print(" ",end='')
      break
print()

count = 0
for space in range(24):
   count+=1
   print(" ",end='')
   while (count%3)==0:
      for stars in range(3):
         print("*",end='')
      break
print()

count = 0
for stars in range(24):
   count+=1
   print("*",end='')
   while (count%3)==0:
      for space in range(3):
         print(" ",end='')
      break
print()


## diamond pattern
print()
counter = 0
while counter < 2:
   counter += 1
   # top part of diamonds
   for row in range(0,4):
      for extra_space in range(20):  
         print(" ",end='')
      for space in range(row,3):
         print(" ",end='')
      for star in range(0,row+1):
        print("* ",end='')
      print()
   # bottom part of diamonds
   for row in range(0,3):
      for extra_space in range(20):
         print(" ",end='')
      for space in range(0,row+1):
        print(" ",end='')
      for star in range(row,3):
        print("* ",end='')
      print()
print()

## checkerboard
count = 0
for stars in range(24):
   count+=1
   print("*",end='')
   while (count%3)==0:
      for space in range(3):
         print(" ",end='')
      break
print()

count = 0
for space in range(24):
   count+=1
   print(" ",end='')
   while (count%3)==0:
      for stars in range(3):
         print("*",end='')
      break
print()

count = 0
for stars in range(24):
   count+=1
   print("*",end='')
   while (count%3)==0:
      for space in range(3):
         print(" ",end='')
      break
print()

## rectangle
for stars in range(49):
   print("*",end='')
print()
for stars in range(49):
   print("*",end='')
print()

## spaced rectanges - tails of carpet
current = 0
while current < 2:
   current += 1
   for spaced_stars in range(25):
      print("*",end=' ')
   print()

