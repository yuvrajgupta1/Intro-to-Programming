"""COMP 150 Lab 8 written by Yuvraj Gupta on March 23, 2021"""


# Read file function
def readFile(filename, lst):
    # open file
    fhand = open(filename)

    # reading file and putting numbers into a list
    for line in fhand:
        lst.append(line)

    # file closed
    fhand.close()

    return lst


# comparing lists
def equal_num(lst1, lst2):
    # checking if two elements in a list are equal
    for i in lst1:
        for j in lst2:
            if i == j:
                lst3.append(i)

    return lst3


# Write into a file function
def writeFile(filename):
    # open/create file in write mode
    fhand = open(filename, "w")

    # writing data into file
    for i in lst3:
        fhand.write(i)

    # file close
    fhand.close()


# list initializations
lst1 = []
lst2 = []
lst3 = []

# function calls
readFile("primenumbers.txt", lst1)
readFile("happynumbers.txt", lst2)
equal_num(lst1, lst2)
writeFile("output.txt")
