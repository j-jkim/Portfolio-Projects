# Name: Justine Kim     # Date: 3/20/19
# NetID: jk5565         # Section: CSCI-UA.0002-1
# Assignment 5          # Program: 3A


# ask user to enter a number
pos_num = int(input("Enter a positive number to test: "))

# to ensure that user puts in valid input
while pos_num <= 0:
    print("Sorry, that's invalid. Please try again!")
    print()
    pos_num = int(input("Enter a positive number to test: "))
    
print()

if pos_num == 1:
    print("1 is technically not a prime number!")

elif pos_num == 2:
    print("2 is a prime number!")
    
# for looping!
for factor in range(2, pos_num): 
    if (pos_num % factor) != 0:
        print(str(factor)+" is NOT a divisor of "+str(pos_num)+" ... continuing")

        if factor == pos_num-1:
            print()
            print(str(pos_num)+" is a prime number!")
            
    else:
        print(str(factor)+" is a divisor of "+str(pos_num)+" ... stopping")
        print()
        print(str(pos_num)+" is not a prime number.")
        break

            
