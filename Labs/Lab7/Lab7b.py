"""COMP-150 Lab 7b by Yuvraj Gupta on March 16, 2021"""


def ones_places(x):
    # list for ones, hundreds and thousands places
    ones_place = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return ones_place[int(x)]


def tens_places(x):
    # list for tens places
    tens_place = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen']

    # condition to check if the number should be eleven to nineteen
    if x[-2] == '1':
        return tens[int(x[-2])]

    # condition to check if the ones place is greater than 0
    if x[-1] > '0':
        return tens_place[int(x[-2])] + " " + ones_places(x[-1])
    else:
        return tens_place[int(x[-2])]


def hundred_places(x):
    # condition to check if last 2 digits are 00
    if x[-3:] == '00':
        return ones_places(x[-3]) + " hundred"
    else:
        return ones_places(x[-3]) + " hundred " + tens_places(x)


def num2words(x):
    # converting int to string because will be executed on the basis of strings
    x = str(x)

    # condition check if length of numbers > 4
    if len(x) > 4:
        return 'numbers greater than 4 digits are not supported'

    elif len(x) == 1:
        # function invocation
        ones_places(x)

    elif len(x) == 2:
        # function invocation
        return tens_places(x)

    elif len(x) == 3:
        # function invocation
        return hundred_places(x)

    else:
        # number to words for 4 digit numbers
        if x[1:] == '000':
            return ones_places(x[0]) + " thousand "
        elif x[1:3] == '00':
            return ones_places(x[0]) + " thousand" + ones_places(x[-1])
        else:
            return ones_places(x[0]) + " thousand " + hundred_places(x[1:])


# get input as string
num = input("Enter a number: ")

# check if nothing is entered
if len(num) == 0:
    print("empty")

else:
    # convert num to int to remove starting zeros
    num = int(num)

    # printing the value of function
    print(num2words(num))
