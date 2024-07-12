#Remove possible whitespaces from the given input (strip function)
#Capitalize user's name and a possible second characters (title function)
name = input("What's your name?").strip().title()

print("Hello " + name + "!")