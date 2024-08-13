name = input("What's your name? ")    

file = open("names.txt", "a")
#'a' stands for appending which will make a list without overwriting

file.write(f"{name}\n")
file.close()