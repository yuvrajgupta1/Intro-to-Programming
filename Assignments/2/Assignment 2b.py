"""
Assignment 2b is similar to Assignment 2a. Only difference is we use pre-defined functions mean and standard deviation
from statistics module in this Assignment

By Yuvraj Gupta

This code is being written to check whether the previous code calculates standard deviation and mean correctly through
the use of user-defined functions. In this code we will use pre-defined functions for mean and standard deviation by
importing statistics module
"""

import statistics


def input_income():
    # Get input from user
    gross_income = float(input("Please enter employee's gross income: "))

    # Loop to check that the user enters positive value or enter 'exit' to quit
    while gross_income < 0:
        # get gross_income as string
        gross_income = input("Error. Please enter a positive value or type 'exit' to quit: ")
        if gross_income == 'exit':
            # terminate program
            exit()
        else:
            # convert gross_income to float
            gross_income = float(gross_income)

    # returns value to the function
    return gross_income


def cal_cpp(gross_income):
    cpp = gross_income * 0.0525
    # Setting max value of cpp
    if cpp > 2898.00:
        cpp = 2898.00
    # returns the value to the function
    return cpp


def cal_ei(gross_income):
    ei = gross_income * 0.0158
    # setting max value of ei
    if ei > 856.36:
        ei = 856.36
    # returns the value to the function
    return ei


def cal_health_p(gross_income):
    health_p = 0.00
    if gross_income > 200000:
        health_p = 750 + (0.25 * (gross_income - 200000))

        # setting max value of health_p for respective bracket
        if health_p > 900.00:
            health_p = 900.00

    elif gross_income > 72000:
        health_p = 600 + (0.25 * (gross_income - 72000))

        # setting max value of health_p for respective bracket
        if health_p > 750.00:
            health_p = 750.00

    elif gross_income > 48000:
        health_p = 450 + (0.25 * (gross_income - 48000))

        # setting max value of health_p for respective bracket
        if health_p > 600.00:
            health_p = 600.00

    elif gross_income > 36000:
        health_p = 300 + (0.06 * (gross_income - 36000))

        # setting max value of health_p for respective bracket
        if health_p > 450.00:
            health_p = 450.00

    elif gross_income > 20000:
        health_p = (0.06 * (gross_income - 20000))

        # setting max value of health_p for respective bracket
        if health_p > 300.00:
            health_p = 300.00
    # returns the value to the function
    return health_p


# calculate provincial tax
def cal_p_tax(gross_income):
    x = gross_income
    p_tax = 0
    if x >= 220000.01:
        p_tax += (x - 2200000.01) * 0.1316
        x = 220000.01

    if x >= 150000.01:
        p_tax += (x - 150000.01) * 0.1216
        x = 150000.01

    if x >= 89482.01:
        p_tax += (x - 89482.01) * 0.1116
        x = 89482.01

    if x >= 44740.01:
        p_tax += (x - 44740.01) * 0.0915
        x = 44740

    if x >= 0:
        p_tax += x * 0.0505
    # returns the value to the function
    return p_tax


# calculate federal tax
def cal_f_tax(gross_income):
    x = gross_income
    f_tax = 0
    if x >= 214368.01:
        f_tax += (x - 214368.01) * 0.33
        x = 214368.01

    if x >= 150473.01:
        f_tax += (x - 150473.01) * 0.29
        x = 150473.01

    if x >= 97069.01:
        f_tax += (x - 97069.01) * 0.26
        x = 97069.01

    if x >= 48535.01:
        f_tax += (x - 48535.01) * 0.205
        x = 48535

    if x >= 0:
        f_tax += x * 0.15
    # returns value to the function
    return f_tax


def cal_net_income(x):
    # multiple function invocations
    net_income = x - (cal_p_tax(x) + cal_f_tax(x) + cal_ei(x) + cal_cpp(x) + cal_health_p(x))
    # returns value to the function after rounding off to 2 decimal places
    return round(net_income, 2)


def print_output():
    # print statements
    print()
    print()
    print("---------- Ontario's Tax Calculator ----------")
    print("Employees' taxable incomes CAD($):", gross_income_list)
    print("Employees' net incomes (after tax deductions) CAD($):", net_income_list)
    print("Mean of net incomes : CAD($)", round(statistics.mean(net_income_list), 2))  # round off to 2 decimal places
    print("Standard deviation of net incomes : CAD($)", round(statistics.pstdev(net_income_list), 2))


# Input number of employees
n = int(input("Enter the number of employees: "))

# Check if number of employees entered is positive
while n < 0:
    # Get input from user either number of employees or 'exit'
    n = input("Error. Please enter a positive value or type 'exit' to quit: ")
    # condition to terminate the program
    if n == 'exit':
        # terminate the program
        exit()
    else:
        # convert n to integer
        n = int(n)

# Initializations
gross_income_list = []
net_income_list = []

# print statements
print()
print("--------------- Enter Employee's Salaries(i.e., Gross Incomes) Below ---------------")

# Inputting elements into the list
for i in range(n):
    gross_income_list.append(input_income())
    net_income_list.append(cal_net_income(gross_income_list[i]))

# function invocation
print_output()
