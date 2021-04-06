def FindMax(lst, n):
    # if list has only 1 element
    if n == 1:
        return lst[0]

    # returns the max value with the two arguments inputted into the max function
    return max(lst[n - 1], FindMax(lst, n - 1))


def FindMin(lst, n):
    # if list has only 1 element
    if n == 1:
        return lst[0]

    # returns the min value with the 2 arguments inputted into the min function
    return min(lst[n - 1], FindMin(lst, n - 1))


# hard-coded lists
list1 = [3, 4, 50, 23, 45]
list2 = [12, 65, 21, 34, 88]

# print statements
print("Max and Min of", list1, "is", FindMax(list1, len(list1)), "and", FindMin(list1, len(list1)), "\n")
print("Max and Min of", list2, "is", FindMax(list2, len(list2)), "and", FindMin(list2, len(list2)))
