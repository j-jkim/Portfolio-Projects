# Name: Justine Kim     # Date: 3/20/19
# NetID: jk5565         # Section: CSCI-UA.0002-1
# Assignment 5          # Program: 3B


# printing since 1 is not a prime number 
print("1 is technically not a prime number!")

# onto to the for loop!
for number in range(1, 1000+1):  # 1000+1 so 1000's not excluded 
   if number > 1:
      for factor in range(2, number):
         if (number % factor) == 0:  # check for each # to see if it has
            break              # other factors other than itself and 1

      else:
         print(str(number)+" is a prime number!") 
