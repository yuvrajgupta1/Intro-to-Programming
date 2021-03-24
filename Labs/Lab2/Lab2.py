# This is Lab2 (Comp150) written by Yuvraj Gupta, Jan 26,2021

# Problem definition: Manitoba Tax Calculation.

# Get input from user
salary = float(input("Please enter employee's annual taxable income ... CAD($) "))

# ensuring inputted salary is positive
if salary < 0:
    print("Error. It can not be negative")
    quit()

else:
    if salary >= 72164.01:
        salary *= 0.174
        tax = "17.40%"
        bracket = "[$72,164.01 ..)"

    elif salary >= 33389.01:
        salary *= 0.1275
        tax = "12.75%"
        bracket = "[$33,389.01 .. $72,164.01)"

    else:
        salary *= 0.108
        tax = "10.80%"
        bracket = "[$0 .. $33,389.01)"

# using salary variable as tax value
# rounds salary to 2 decimal places
salary = round(salary, 2)

# Print the tax value and bracket
print("Employee's provincial tax value : CAD($) ", salary)
print("Employee's provincial tax bracket : ", tax, bracket)
