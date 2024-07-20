import sys

#'sys.argv[1]' gets the input from the command line
#after the initial 'python 17-command_line.py'
if len(sys.argv) < 2:
    sys.exit("No input written")

print("Hello, my name is", end=" ")
#We need to slice off the list because the first 
#character is the program's title
for arg in sys.argv[1:]:
    print(arg, end=" ")