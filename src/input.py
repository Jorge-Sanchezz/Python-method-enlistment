#Ask the user for their name
#Then, remove possible whitespaces from the given input (strip function)
#and then, capitalize user's name and a possible second characters (title function)
name = input("What's your name?").strip().title()

#Say hello
print("Hello " + name + "!")