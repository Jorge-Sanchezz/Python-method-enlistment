try:
    x = int(input("What's number x? "))
    print(f"x is {x}")
    
except ValueError:
    print("Your input is not an integer")