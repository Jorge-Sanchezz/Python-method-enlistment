try:
    x = int(input("What's number x? "))
    print(f"x is {x}")
    
#Catch an value error if founded one
except ValueError:
    print("Your input is not an integer")