x = input("Enter numerator\n")
x = float(x)
y = input("Enter denominator (don't enter 0)\n")
y = float(y)

frac = x % y

if frac == 0:
    print("True")

else:
    print("False")
