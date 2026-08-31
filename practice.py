"""
row1 = ['1','1','1']
row2 = ['1','1','1']
row3 = ['1','1','1']
matrix = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("where do you wnat to hide: ")
row_number = int(position[0])
cloumn_number = int(position[1])
row_selected = matrix[row_number-1]
row_selected[cloumn_number-1] = 'x'
print(f"{row1}\n{row2}\n{row3}")
"""

import random

rock = 0
paper = 1
scisser = 2
user_choice = int(input("enter a random number: "))
computer_choice = random.randint(0,2)
print(computer_choice)

if user_choice>2 or user_choice<0:
    print("invalid number! please try again")
else:
    if user_choice>computer_choice:
        print("user will win")
    elif user_choice<computer_choice:
        print("computer will win")
    elif user_choice==computer_choice:
        print("draw")
    elif user_choice==2 & computer_choice==0:
        print("computer will win")
    elif user_choice==0 & computer_choice==2:
        print("user will win")

#print("it's my first project")
     