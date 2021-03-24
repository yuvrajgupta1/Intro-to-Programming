"""COMP-150 Lab 7a by Yuvraj Gupta on March 16,2021"""
# importing module
import string


def removePunct(line):
    # initialising required string
    new_str = ""

    # i takes all the values of elements in line if line is considered as a list of strings
    for i in line:

        # check to see if i is not equal to punctuations; string.punctuations includes all the punctuation marks
        if i not in string.punctuation:

            # concatenation of 2 strings
            new_str += i

    # return value to string
    return new_str


# Get input from user
line = input("Please enter a string: ")

# Printing the input
print("This is the input:", line)

# Printing the required output
print("This is after removing puncts:", removePunct(line))
