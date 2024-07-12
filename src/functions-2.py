#There is an easier way of using exponents in python with a built-in
#function called 'pow' but in this exercise, the problem is solved 
#this way to demonstrate how to return values on a function
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    
def square(n):
    return n * n

main()