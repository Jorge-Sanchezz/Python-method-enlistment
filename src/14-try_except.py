def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's number x? "))
        #Catch an value error if founded one
        except ValueError:
            print("Your input is not an integer")
        else:
            break
    return x
    
main()