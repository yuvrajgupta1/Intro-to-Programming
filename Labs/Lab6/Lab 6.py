"""Lab 6 COMP-150 Yuvraj Gupta
***********************************************************************
            Program Design for evenindexedElements function
***********************************************************************
***    Get lst                                                      ***
***    i = 0                                                        ***
***    k = 0                                                        ***
***    size = len(lst)                                              ***
***    while i < size                                               ***
***            evenList[k] = lst[i]                                 ***
***            k = k + 1                                            ***
***            i = i + 2                                            ***
***    End of loop                                                  ***
***    return evenList                                              ***
***    Stop                                                         ***
***********************************************************************
            Program Design for oddindexedElements function
***********************************************************************
***    Get lst                                                      ***
***    i = 1                                                        ***
***    k = 0                                                        ***
***    size = len(lst)                                              ***
***    while i < size                                               ***
***            oddList[k] = lst[i]                                  ***
***            k = k + 1                                            ***
***            i = i + 2                                            ***
***    End of loop                                                  ***
***    return oddList                                               ***
***    Stop                                                         ***
***********************************************************************
             Program Design for greaterSumList function
***********************************************************************
***    Get lst1 and lst2                                            ***
***    if(len(lst1) == 0 or len(lst2) == 0) then                    ***
***        return []                                                ***
***    else                                                         ***
***        if(sum(lst1) > sum(lst2)) then                           ***
***            return lst1                                          ***
***        else                                                     ***
***            if(sum(lst2) > sum(lst1)) then                       ***
***                return lst2                                      ***
***            else                                                 ***
***                return lst1, lst2                                ***
***    Stop                                                         ***
***********************************************************************
            Program Design for user_input function
***********************************************************************
***    Get the value of n                                           ***
***    i = 0                                                        ***
***    while i < n                                                  ***
***            Get the value of lst[i]                              ***
***            i = i + 1                                            ***
***    End of loop                                                  ***
***    return lst                                                   ***
***    Stop                                                         ***
***********************************************************************
                        Program Design
***********************************************************************
***    lst = []                                                     ***
***    evenList = []                                                ***
***    oddList = []                                                 ***
***    user_input()                                                 ***
***    oddindexedElements(lst)                                      ***
***    evenindexedElements(lst)                                     ***
***    print greaterSumList(oddList, evenList)                      ***
***    Stop                                                         ***
***********************************************************************
***********************************************************************"""


def evenindexedElements(x):
    i = 0
    while i < len(x):
        # adding elements of the existing list to another list to separate even indexed elements
        evenList.append(x[i])
        # i remains odd
        i += 2
    return evenList


def oddindexedElements(x):
    i = 1
    while i < len(x):
        # adding elements of the existing list to another list to separate even indexed elements
        oddList.append(x[i])
        # i remains odd
        i += 2
    return oddList


def greaterSumList(lst1, lst2):
    if len(lst1) | len(lst2) == 0:
        # returns the value of [] to the function
        return []

    # function invocation and comparison
    elif sum(lst1) > sum(lst2):
        # returns the value of lst1 to the function
        return lst1

    # function invocation and comparison
    elif sum(lst2) > sum(lst1):
        # returns the value of lst2 to the function
        return lst2

    else:
        # returns the value of lst1 to the function
        return lst1, lst2


def user_input():
    # ask user the number of elements
    n = int(input("Enter the number of elements you want to enter: "))

    # ask user for input and arranging it in a list
    for i in range(n):
        lst.append(int(input("Enter number: ")))

    return lst


# list initialization
lst = []
evenList = []
oddList = []

# function invocation
user_input()

# print and function invocation
print(greaterSumList(oddindexedElements(lst), evenindexedElements(lst)))
