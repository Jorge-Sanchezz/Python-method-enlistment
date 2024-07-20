def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Goodbye, {name}")
    
#This part is madw to avoid running the main function when called
#an specific function like hello() from other document as a library
if __name__ == "__main__":
    main()