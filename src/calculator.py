#Asking for the user's x and y value
x = input("Insert x value ")
y = input("Insert y value ")

#Sum the values (we have to convert them to
#int to use the + character properly)
z = float(x) + float(y)

#Round the result to the nearest hundredth
z = round(z, 2)

#Print the final result
print("The sum of", x, "+", y, "=", f"{z:,}")

#f"{z}" is just another way of calling the funciton
#in this case to print. While the ':,' part will just
#add the needed commas according to the need or length
#of the number