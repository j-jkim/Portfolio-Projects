# Name: Justine Kim     # Date: 3/20/19
# NetID: jk5565         # Section: CSCI-UA.0002-1
# Assignment 5          # Program: Clock Simulator


# set up hour
for hour in range(0,24):
   
   # set up minute for every hour
   for minute in range(0,60):
      
      # set up second for every minute
      for second in range(0,60):
         
         # printing out times from midnight to 23:59:59
         print(hour, minute, sep=":",end='')
         print(":"+str(second))
            
         


