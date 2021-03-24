""" This is Assignment 1 (COMP-150) written by Yuvraj Gupta

Problem definition : Ontario's Income Tax Calculator

****************************************************************************************************************
                                        Program Design (Pseudocode)
****************************************************************************************************************
****                                                                                                        ****
****    Get the value of tax_income                                                                         ****
****    While (tax_income < 0) do                                                                           ****
****        Print 'Error. Please enter positive value'                                                      ****
****        Get the value of tax_income                                                                     ****
****    End of loop                                                                                         ****
****                                                                                                        ****
****    Set the value of p_tax to tax_income                                                                ****
****    If (tax_income > 220000.01) then                                                                    ****
****        Set the value of p_tax to p_tax * 0.1316                                                        ****
****        Set p_bracket to '13.16% [$220,000.01 +)'                                                       ****
****    Else                                                                                                ****
****        If (tax_income > 150000.01) then                                                                ****
****            Set the value of p_tax to p_tax * 0.1216                                                    ****
****            Set p_bracket to '12.16% [$150,000.01 ... $220,000.01)'                                     ****
****        Else                                                                                            ****
****            If (tax_income > 89482.01) then                                                             ****
****                Set the value of p_tax to p_tax * 0.1116                                                ****
****                Set p_bracket to '11.16% [$89,482.01 ... $150,000.01)'                                  ****
****            Else                                                                                        ****
****                If (tax_income > 44740.01) then                                                         ****
****                    Set the value of p_tax to p_tax * 0.0915                                            ****
****                    Set p_bracket to '9.15% [$44,740.01 ... $89,482.01)'                                ****
****                Else                                                                                    ****
****                    Set the value of p_tax to p_tax * 0.0505                                            ****
****                    Set p_bracket to '5.05% [$0 ... $44,740.01)'                                        ****
****                                                                                                        ****
****    Set the value of f_tax to tax_income                                                                ****
****    If (tax_income > 214368.01) then                                                                    ****
****        Set the value of f_tax to f_tax * 0.33                                                          ****
****        Set f_bracket to '33.0% [$214,368.01 +)'                                                        ****
****    Else                                                                                                ****
****        If (tax_income > 150473.01) then                                                                ****
****            Set the value of f_tax to f_tax * 0.29                                                      ****
****            Set f_bracket to '29.0% [$150,473.01 ... $214,368.01)'                                      ****
****        Else                                                                                            ****
****            If (tax_income > 97069.01) then                                                             ****
****                Set the value of f_tax to f_tax * 0.26                                                  ****
****                Set f_bracket to '26.0% [$97,069.01 ... $150,473.01)'                                   ****
****            Else                                                                                        ****
****                If (tax_income > 48535.01) then                                                         ****
****                    Set the value of f_tax to f_tax * 0.205                                             ****
****                    Set f_bracket to '20.5% [$48,535.01 ... $97,069.01)'                                ****
****                Else                                                                                    ****
****                    Set the value of f_tax to f_tax * 0.15                                              ****
****                    Set f_bracket to '15.0% [$0 ... $48,535.01)'                                        ****
****                                                                                                        ****
****    Set the value of cpp to tax_income * 0.0525                                                         ****
****    If (cpp > 2898) then                                                                                ****
****        Set the value of cpp to 2898.00                                                                 ****
****                                                                                                        ****
****    Set the value of ei to tax_income * 0.0158                                                          ****
****    If (ei > 856.36) then                                                                               ****
****        Set the value of ei to 856.36                                                                   ****
****                                                                                                        ****
****    Set the value of health_p to 0                                                                      ****
****    If (tax_income > 200000) then                                                                       ****
****        Set the value of health_p to 750 + (0.25 * (tax_income - 200000))                               ****
****        If (health_p > 900) then                                                                        ****
****            Set the value of health_p to 900.00                                                         ****
****                                                                                                        ****
****    Else                                                                                                ****
****        If (tax_income > 72000) then                                                                    ****
****            Set the value of health_p to 600 + (0.25 * (tax_income - 72000))                            ****
****            If (health_p > 750) then                                                                    ****
****                Set the value of health_p to 750.00                                                     ****
****                                                                                                        ****
****        Else                                                                                            ****
****            If (tax_income > 48000) then                                                                ****
****                Set the value of health_p to 450 + (0.25 * (tax_income - 48000))                        ****
****                If (health_p > 600) then                                                                ****
****                    Set the value of health_p to 600.00                                                 ****
****                                                                                                        ****
****            Else                                                                                        ****
****                If (tax_income > 36000) then                                                            ****
****                    Set the value of health_p to 300 + (0.06 * (tax_income - 36000))                    ****
****                    If (health_p > 450) then                                                            ****
****                    Set the value of health_p to 450.00                                                 ****
****                                                                                                        ****
****                Else                                                                                    ****
****                    If (tax_income > 20000) then                                                        ****
****                        Set the value of health_p to (0.06 * (tax_income - 20000))                      ****
****                        If (health_p > 300) then                                                        ****
****                        Set the value of health_p to 300.00                                             ****
****                                                                                                        ****
****    Set the value of deductions to p_tax + f_tax + cpp + ei + health_p                                  ****
****    Set the value of net_income to tax_income - deductions                                              ****
****    Print the value of tax_income, net_income, cpp, ei, health_p, p_tax, p_bracket, f_tax, f_bracket    ****
****    Stop                                                                                                ****
****                                                                                                        ****
****************************************************************************************************************
****************************************************************************************************************"""

# get user input for taxable income
tax_income = float(input("Please enter employee's annual taxable income ... CAD($) "))

# check that taxable income is positive, if not then program asks for positive input
while tax_income < 0:
    tax_income = float(input("Error. Please enter positive value ... CAD($) "))

# Calculating provincial tax (p_tax)
p_tax = tax_income
if tax_income > 220000.01:
    p_tax *= 0.1316
    p_bracket = '13.16% [$220,000.01 +)'

elif tax_income > 150000.01:
    p_tax *= 0.1216
    p_bracket = '12.16% [$150,000.01 ... $220,000.01)'

elif tax_income > 89482.01:
    p_tax *= 0.1116
    p_bracket = '11.16% [$89482.01 ... $150,000.01)'

elif tax_income > 44742.01:
    p_tax *= 0.0915
    p_bracket = '9.15% [$44,742.01 ... $89,482.01)'

else:
    p_tax *= 0.0505
    p_bracket = '5.05% [$0 ... $44,742.01)'

# Calculating federal tax (f_tax)
f_tax = tax_income
if tax_income > 214368.01:
    f_tax *= 0.33
    f_bracket = '33.0% [$214,368.01 +)'

elif tax_income > 150473.01:
    f_tax *= 0.29
    f_bracket = '29.0% [$150,473.01 ... $214,368.01)'

elif tax_income > 97069.01:
    f_tax *= 0.26
    f_bracket = '26.0% [$97,069.01 ... $150,473.01)'

elif tax_income > 48535.01:
    f_tax *= 0.205
    f_bracket = '20.5% [$48,535.01 ... $97,069.01)'

else:
    f_tax *= 0.15
    f_bracket = '15.0% [$0 ... $48,535.01)'

# Calculating Canadian Pension Plan (cpp)
cpp = tax_income * 0.0525

# setting the max value of cpp
if cpp > 2898.00:
    cpp = 2898.00

# calculating Employment Insurance (ei)
ei = tax_income * 0.0158

# setting the max value of ei
if ei > 856.36:
    ei = 856.36

# calculating health premium (heath_p)
health_p = 0.00
if tax_income > 200000:
    health_p = 750 + (0.25 * (tax_income - 200000))

    # setting max value of health_p for respective bracket
    if health_p > 900.00:
        health_p = 900.00

elif tax_income > 72000:
    health_p = 600 + (0.25 * (tax_income - 72000))

    # setting max value of health_p for respective bracket
    if health_p > 750.00:
        health_p = 750.00

elif tax_income > 48000:
    health_p = 450 + (0.25 * (tax_income - 48000))

    # setting max value of health_p for respective bracket
    if health_p > 600.00:
        health_p = 600.00

elif tax_income > 36000:
    health_p = 300 + (0.06 * (tax_income - 36000))

    # setting max value of health_p for respective bracket
    if health_p > 450.00:
        health_p = 450.00

elif tax_income > 20000:
    health_p = (0.06 * (tax_income - 20000))

    # setting max value of health_p for respective bracket
    if health_p > 300.00:
        health_p = 300.00

# calculating total of deductions that need to be subtracted from taxable income
deductions = p_tax + f_tax + cpp + ei + health_p

# calculating net income
net_income = tax_income - deductions

# printing all values and ensuring that all values print with 2 decimal places
print()
print('************* Income Values *************')
print()
print("Employee's annual taxable income : CAD($) "+"{:.2f}".format(round(tax_income, 2)))
print("Employee's net income : CAD($) "+"{:.2f}".format(round(net_income, 2)))
print()
print("************** Deductions ***************")
print()
print("Employee's CPP : CAD($) "+"{:.2f}".format(round(cpp, 2)))
print("Employee's EI : CAD($) "+"{:.2f}".format(round(ei, 2)))
print("Employee's Health premium : CAD($) "+"{:.2f}".format(round(health_p, 2)))
print()
print("Employee's provincial tax value : CAD($) "+"{:.2f}".format(round(p_tax, 2)))
print("Employee's provincial tax bracket : ", p_bracket)
print()
print("Employee's federal tax value : CAD($) "+"{:.2f}".format(round(f_tax, 2)))
print("Employee's federal tax bracket : ", f_bracket)
