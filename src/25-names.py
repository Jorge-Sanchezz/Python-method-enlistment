name = input("What's your name? ")
names = []

#Here, "a" stands for append and avoids the last name to be deleted when added a new input
with open("names.csv", "a") as file:
    #Once the indented code is ran, the file is automatically closed
    file.write(f"{name}\n")
    
with open("names.csv") as file:
    for line in file:
        names.append(line.strip())

#We sort the list created at the beginning (which was assigned the txt file information)
for name in sorted(names):
    print(f"hello, {name}")