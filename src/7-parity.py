def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even number")
    else:
        print("Odd number")
        
def is_even(n):
    return n % 2 == 0
    
main()