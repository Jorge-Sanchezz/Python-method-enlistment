try:
    x = int(input("What's number x? "))
    
#Catch an value error if founded one
except ValueError:
    print("Your input is not an integer")

else:
    print(f"x is {x}")