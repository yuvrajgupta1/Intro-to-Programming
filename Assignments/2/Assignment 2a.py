""" Assignment 2a written by Yuvraj Gupta

Problem Definition: Ontario Tax Calculator (revised)
****************************************************************************************************************
                                Program Design for input_income function
****************************************************************************************************************
****    Get gross_income                                                                                    ****
****    While (gross_income < 0) do                                                                         ****
****        Print message 'Error. Please enter a positive value or type 'exit' to quit: '                   ****
****        Get gross_income                                                                                ****
****        if (gross_income == 'exit') then                                                                ****
****            Stop                                                                                        ****
****        else                                                                                            ****
****            Convert gross_income type to float                                                          ****
****    End of loop                                                                                         ****
****    return gross_income                                                                                 ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                Program Design for cal_cpp function
****************************************************************************************************************
****    Get gross_income                                                                                    ****
****    Set the value of cpp to gross_income * 0.0525                                                       ****
****    If (cpp > 2898) then                                                                                ****
****        Set the value of cpp to 2898.00                                                                 ****
****    return cpp                                                                                          ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                Program Design for cal_ei function
****************************************************************************************************************
****    Get gross_income                                                                                    ****
****    Set the value of ei to gross_income * 0.0158                                                        ****
****    If (ei > 856.36) then                                                                               ****
****        Set the value of ei to 856.36                                                                   ****
****    return ei                                                                                           ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                Program Design for cal_health_p function
****************************************************************************************************************
****    Get gross_income                                                                                    ****
****    Set the value of health_p to 0                                                                      ****
****    If (gross_income > 200000) then                                                                     ****
****        Set the value of health_p to 750 + (0.25 * (gross_income - 200000))                             ****
****        If (health_p > 900) then                                                                        ****
****            Set the value of health_p to 900.00                                                         ****
****                                                                                                        ****
****    Else                                                                                                ****
****        If (gross_income > 72000) then                                                                  ****
****            Set the value of health_p to 600 + (0.25 * (gross_income - 72000))                          ****
****            If (health_p > 750) then                                                                    ****
****                Set the value of health_p to 750.00                                                     ****
****                                                                                                        ****
****        Else                                                                                            ****
****            If (gross_income > 48000) then                                                              ****
****                Set the value of health_p to 450 + (0.25 * (gross_income - 48000))                      ****
****                If (health_p > 600) then                                                                ****
****                    Set the value of health_p to 600.00                                                 ****
****                                                                                                        ****
****            Else                                                                                        ****
****                If (gross_income > 36000) then                                                          ****
****                    Set the value of health_p to 300 + (0.06 * (gross_income - 36000))                  ****
****                    If (health_p > 450) then                                                            ****
****                    Set the value of health_p to 450.00                                                 ****
****                                                                                                        ****
****                Else                                                                                    ****
****                    If (gross_income > 20000) then                                                      ****
****                        Set the value of health_p to (0.06 * (gross_income - 20000))                    ****
****                        If (health_p > 300) then                                                        ****
****                        Set the value of health_p to 300.00                                             ****
****    return health_p                                                                                     ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                Program Design for cal_p_tax function
****************************************************************************************************************
****    Get gross_income                                                                                    ****
****    Set x = gross_income                                                                                ****
****    Set p_tax = 0                                                                                       ****
****    if (x >= 220000.01) then                                                                            ****
****        Set p_tax = p_tax + ((x - 2200000.01) * 0.1316)                                                 ****
****        Set x = 220000.01                                                                               ****
****                                                                                                        ****
****    if (x >= 150000.01) then                                                                            ****
****        Set p_tax = p_tax + ((x - 150000.01) * 0.1216)                                                  ****
****        Set x = 150000.01                                                                               ****
****                                                                                                        ****
****    if (x >= 89482.01) then                                                                             ****
****       Set p_tax = p_tax + ((x - 89482.01) * 0.1116)                                                    ****
****       Set x = 89482.01                                                                                 ****
****                                                                                                        ****
****    if (x >= 44740.01) then                                                                             ****
****        Set p_tax = p_tax + ((x - 44740.01) * 0.0915)                                                   ****
****        Set x = 44740                                                                                   ****
****                                                                                                        ****
****    if x >= 0:                                                                                          ****
****        Set p_tax = p_tax + (x * 0.0505)                                                                ****
****    return p_tax                                                                                        ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                Program Design for cal_f_tax function
****************************************************************************************************************
****    Get gross_income                                                                                    ****
****    Set x = gross_income                                                                                ****
****    Set f_tax = 0                                                                                       ****
****    if (x >= 214368.01) then                                                                             ****
****       Set f_tax = f_tax + ((x - 214368.01) * 0.33)                                                     ****
****       Set x = 214368.01                                                                                ****
****                                                                                                        ****
****    if (x >= 150473.01) then                                                                            ****
****       Set f_tax = f_tax + ((x - 150473.01) * 0.29)                                                     ****
****       Set x = 150473.01                                                                                ****
****                                                                                                        ****
****    if (x >= 97069.01) then                                                                             ****
****       Set f_tax = f_tax + ((x - 97069.01) * 0.26)                                                      ****
****       Set x = 97069.01                                                                                 ****
****                                                                                                        ****
****    if (x >= 48535.01) then                                                                             ****
****       Set f_tax = f_tax + ((x - 48535.01) * 0.205)                                                     ****
****       Set x = 48535                                                                                    ****
****                                                                                                        ****
****    if (x >= 0) then                                                                                    ****
****       Set f_tax = f_tax + (x * 0.15)                                                                   ****
****    return f_tax                                                                                        ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                Program Design for cal_net_income function
****************************************************************************************************************
****    Get x                                                                                               ****
****    Set net_income = x - (cal_p_tax(x) + cal_f_tax(x) + cal_ei(x) + cal_cpp(x) + cal_health_p(x))       ****
****    Round net_income to 2 decimal places                                                                ****
****    return net_income                                                                                   ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                Program design for cal_mean function
****************************************************************************************************************
****    Get net_income_list                                                                                 ****
****    Set mean = sum(net_income_list)                                                                     ****
****    Set mean = mean / n                                                                                 ****
****    return mean                                                                                         ****
****    Stop                                                                                                ****
****************************************************************************************************************
                            Program Design for cal_standard_deviation function
****************************************************************************************************************
****    Get net_income_list, n                                                                              ****
****    Set standard_deviation = 0                                                                          ****
****    Set j = 0                                                                                           ****
****    While (j < n) do                                                                                    ****
****        Set standard_deviation = standard_deviation + (net_income_list[j] - cal_mean())^2               ****
****        Set j = j + 1                                                                                   ****
****    End of loop                                                                                         ****
****    Set standard_deviation = standard_deviation / n                                                     ****
****    Set standard_deviation = sqrt(standard_deviation)                                                   ****
****    Round standard_deviation to 2 decimal places                                                        ****
****    Return standard_deviation                                                                           ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                Program Design for print_output function
****************************************************************************************************************
****    Print 2 new lines                                                                                   ****
****    Print gross_income_list, net_income_list                                                            ****
****    Print cal_mean(), cal_standard_deviation()                                                          ****
****    Stop                                                                                                ****
****************************************************************************************************************
                                            Program Design
****************************************************************************************************************
****    Get n                                                                                               ****
****    While (n < 0) do                                                                                    ****
****        Print the message 'Error. Please enter a positive value or type 'exit' to quit: '               ****
****        Get n                                                                                           ****
****        if (n == 'exit') then                                                                           ****
****            Stop                                                                                        ****
****        else                                                                                            ****
****            Convert n to integer                                                                        ****
****    End of loop                                                                                         ****
****    Set gross_income_list = []                                                                          ****
****    Set net_income_list = []                                                                            ****
****    Print 2 new lines                                                                                   ****
****    Set i = 0                                                                                           ****
****    While (i < n) do                                                                                    ****
****        Set gross_income_list[i] = input_income()                                                       ****
****        Set net_income_list[i] = cal_net_income(gross_income_list[i])                                   ****
****        Set i = i + 1                                                                                   ****
****    End of loop                                                                                         ****
****    print_output()                                                                                      ****
****    Stop                                                                                                ****
****************************************************************************************************************
****************************************************************************************************************"""

# to use square root function
import math


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


def cal_mean():
    mean = sum(net_income_list)
    mean /= n
    # returns the value to the function
    return mean


def cal_standard_deviation():
    standard_deviation = 0
    # to do calculations on each item of the list
    for j in range(n):
        standard_deviation += pow(net_income_list[j] - cal_mean(), 2)
    standard_deviation /= n
    standard_deviation = math.sqrt(standard_deviation)
    # returns value to the function after rounding off to 2 decimal places
    return round(standard_deviation, 2)


def print_output():
    # print statements
    print()
    print()
    print("---------- Ontario's Tax Calculator ----------")
    print("Employees' taxable incomes CAD($):", gross_income_list)
    print("Employees' net incomes (after tax deductions) CAD($):", net_income_list)
    print("Mean of net incomes : CAD($)", round(cal_mean(), 2))  # function invocation and round off to 2 decimal places
    print("Standard deviation of net incomes : CAD($)", cal_standard_deviation())  # function invocation


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
