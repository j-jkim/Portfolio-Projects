# Name: Justine Kim     # Date: 3/20/19
# NetID: jk5565         # Section: CSCI-UA.0002-1
# Assignment 5          # Program: 3D


# ask user for input
start = int(input("Start number: "))
end   = int(input("End number: "))

# making sure user puts valid input
while start < 0 or end < 0:
   print("Start and end must be positive")
   print()
   start = int(input("Start number: "))
   end   = int(input("End number: "))

   # for when user puts positive values but end < start
   if start > 0 and end > 0:  
      while start > end:
         print("End number must be greater than start number")
         print()
         start = int(input("Start number: "))
         end   = int(input("End number: "))

count = 0
# onto to the for loop!
for number in range(start, end+1):
   if number > 1:
      for factor in range(2, number):
         if (number % factor) == 0:  # check for each # to see if it has
            break                    # other factors other than itself and 1
      else:
         count+=1
         print(format(number, ">5d"),end=' ')
         
         if count % 10 == 0:
            print()


