# This is Lab3 (Comp150), written by Yuvraj Gupta on Feb 2,2021

# Problem Definition: Compute sum

#####################################################
#                   Pseudocode                      #
# 1. Set the value of s to 0                        #
# 2. Set the value of x to 1                        #
# 3. Get the value of n                             #
# 4. Set the value of i to the value of n           #
# 4. If n = 0                                       #
# 5.    print 0                                     #
# 6. Else                                           #
# 7.    If (n > 0)                                  #
# 8.        while (n > 0)                           #
# 9.            Set the value of s to n / x         #
# 10.           Set the value of x to x + 1         #
# 11.           Set the value of n to n - 1         #
#           End of the loop                         #
# 12.       round s to 2 decimal places             #
# 13.       print the value of i and s              #
# 14.   Else                                        #
# 15.       print "Please input positive number"    #
# 16. Stop                                          #
#####################################################

s = 0.0                                               # Variable for calculating sum
x = 1.0                                               # Variable for denominator
n = int(input("Enter positive number: "))             # Getting value from user
i = n                                                 # Setting value of i equals to n

if n == 0:                                            # if statement to check whether n is 0
    print(0)                                          # prints 0

elif n > 0:                                           # else if statement to check whether n > 0
    while n > 0:                                      # while loop
        s += n / x                                    # s = s + n / x
        x += 1                                        # x = x + 1
        n -= 1                                        # n = n - 1
    print("fractsum(", i, ") = ", round(s, 2))        # prints the value of s after rounding it to 2 decimals

else:                                                 # checks if n < 0
    print("Please input positive number")             # prints the message
