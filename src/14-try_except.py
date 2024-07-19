def main():
    x = get_int("What's number x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        #Catch an value error if founded one
        except ValueError:
            print("Your input is not an integer")
    
main()