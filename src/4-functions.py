def main():
    name = input("What's your name? ").strip().title()
    greet(name)

def greet(to="world"):
    print("Hello,", to)

main()