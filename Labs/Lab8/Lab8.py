"""COMP 150 Lab 8 written by Yuvraj Gupta on March 23, 2021"""


def readFile(filename, lst):
    fhand = open(filename)
    for line in fhand:
        lst.append(int(line))
    fhand.close()
    return lst1, lst2


def equal_num(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                lst3.append(i)
    return lst3


def writeFile(filename):
    fhand = open(filename, "w")
    for i in lst3:
        fhand.write(str(i)+"\n")
    print(lst3)
    fhand.close()


lst1 = []
lst2 = []
lst3 = []
readFile("primenumbers.txt", lst1)
readFile("happynumbers.txt", lst2)
equal_num(lst1, lst2)
writeFile("output.txt")
