"""
This is COMP-150 Lab 5
by Yuvraj Gupta, March 2,2021

**********************************************************************
            Program Design for totalSum function
***********************************************************************
***    Get lst                                                      ***
***    add = 0                                                      ***
***    counter = 0                                                  ***
***    size = len(lst)                                              ***
***    while(counter < size) do                                     ***
***        element = lst[i]                                         ***
***        add = add + element                                      ***
***        counter = counter + 1                                    ***
***    return add                                                   ***
***    Stop                                                         ***
***********************************************************************
        Program Design for greaterSumList function
***********************************************************************
***    Get lst1 and lst2                                            ***
***    if(len(lst1) == 0 or len(lst2) == 0) then                    ***
***        return []                                                ***
***    else                                                         ***
***        if(totalSum(lst1) > totalSum(lst2)) then                 ***
***            return lst1                                          ***
***        else                                                     ***
***            if(totalSum(lst2) > totalSum(lst1)) then             ***
***                return lst2                                      ***
***            else                                                 ***
***                return lst1                                      ***
***    Stop                                                         ***
***********************************************************************
                        Program Design
***********************************************************************
***    Get lst1 and lst2                                            ***
***    greaterSumList(lst1, lst2)                                   ***
***    Print the value of lst1, lst2,and greaterSumList(lst1, lst2) ***
***    Stop                                                         ***
***********************************************************************
***********************************************************************"""


# create function to calculate sum of list
def totalSum(lst):
    add = 0
    for element in lst:
        add += element
    # returns the value of add to the function
    return add


# create function to compare sums of two list and then return the list with the greater sum
def greaterSumList(lst1, lst2):
    if len(lst1) | len(lst2) == 0:
        # returns the value of [] to the function
        return []

# function invocation
    elif totalSum(lst1) > totalSum(lst2):
        # returns the value of lst1 to the function
        return lst1

# function invocation
    elif totalSum(lst2) > totalSum(lst1):
        # returns the value of lst2 to the function
        return lst2

    else:
        # returns the value of lst1 to the function
        return lst1


# inputs as list
lst1 = []
lst2 = []
lst3 = [-20, 2, 5, 6]
lst4 = [-20, 2, 5, 6, 7]
lst5 = [-20, 3, 4, 5, 6]

# print statements and function invocations
print("Greater sum of lists", lst1, "and", lst2, "is :", greaterSumList(lst1, lst2))
print("Greater sum of lists", lst2, "and", lst5, "is :", greaterSumList(lst2, lst5))
print("Greater sum of lists", lst3, "and", lst5, "is :", greaterSumList(lst3, lst5))
print("Greater sum of lists", lst4, "and", lst5, "is :", greaterSumList(lst4, lst5))
