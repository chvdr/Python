# Program: stars.py
# Author: Chavdar Georgiev
# Last modified: Sun, Mar 15, 2020 12:12:43 PM

ch = '*'    # The symbol that will be iteratively printed
n = 7       # This is how many times printing will be iterated

# -- main program code --

for i in range(n):
    for j in range(n):
        print(ch, end='')
    print()

exit(0)
