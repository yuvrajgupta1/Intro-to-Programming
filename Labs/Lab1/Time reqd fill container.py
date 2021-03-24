s = 0.4
v = input("Enter the volume of container in cubic metres\n")
v = float(v)
v *= 1000   #convert cubic metres to litres

time = (v / s) * 60

print("The time required to fill container is ", time, " seconds")
