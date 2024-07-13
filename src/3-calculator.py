x = float(input("Insert x value "))
y = float(input("Insert y value "))

z = x + y

z = round(z, 2)

print("The sum of", x, "+", y, "=", f"{z:,}")
#f"{z}" is just another way of calling the funciton
#in this case to print. While the ':,' part will just
#add the needed commas according to the need or length
#of the number