#Asking for the user's x and y value
x = input("Insert x value ")
y = input("Insert y value ")

#Sum the values (we have to convert them to
#int to use the + character properly)
z = float(x) + float(y)

#Round the result to the nearest int
z = round(z)

#Print the final result
print("The sum of", x, "+", y, "=", z)