def main():
    number = get_number()
    greet(number)
    
def get_number():
    while True:
        n = int(input("Input a positive value: "))
        if n > 0:
            break
    return n
    
def greet(n):
    for _ in range(n):
        print("Hi")
 
main()