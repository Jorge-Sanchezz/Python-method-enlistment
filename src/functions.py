def main():
    #Asks for the user's name via an input
    name = input("What's your name? ").strip().title()
    #We call the greet function
    greet(name)

#We create a function which prints 'hello'
#and we determine to greet the world as default
#in case of not receiving an argument
def greet(to="world"):
    print("Hello,", to)

main()