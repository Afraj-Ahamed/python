"""
city = input("the city you grew up in:")
pet = input("The name of your first pet")

print(f"Your band name could be {city} {pet}")


bill = int(input("Total bill amount :"))
tips = int(input("Tip percentage :"))
guys = int(input("Number of people splitting :"))

tips = bill * (tips/100)

each_one = (bill + tips) / guys

print(each_one)

height = int(input("enter a height :"))

if(height>3):
    print("buy token")

else:
    print("no token")

number = int(input("enter number :"))

if number%2==0:
    print("the number is even")

else:
    print("the number is odd")


height = int(input("what is your height in feet :"))

if height>=3:
    bill = 0
    print("you can ride")
    age = int(input("enter your age:"))
    if age < 12:
        bill = 150
        print("pay 150 rupees")
    elif age <= 18:
        bill = 250
        print("pay 500 rupees")   
    else:
        bill = 250
        print("pay 500 rupees")

    want_photo = input("do you want to take photo(y/n)")
    if want_photo=='y' or want_photo=='y':
        bill = bill + 50
    print(f"your total bill is {bill}")
else:
    print("can not ride")

print("bye")
"""
"""
size = input("enter the size of pizza(s/m/l):")
bill = 0

if size == 's' or size == 's':
    bill = 500
    print("your bill is 500")
elif size == 'm' or size == 'm':
    bill = 750
    print("your bill is 750")
else:
    bill = 1000
    print("your bill is 1000")

peppeoni = input("do you want peppeoni(y/n):")

if peppeoni == 'y' or peppeoni == 'y':
    if size == 's' or size == 's':
        bill+= 50
        print(f"your bill is {bill}")
    else:
        bill+= 100
        print(f"your bill is {bill}")

extra_cheese = input("do you want(y/n):")
if extra_cheese == 'y' or extra_cheese == 'y':
    bill+= 50

print(f"your bill is {bill}")
"""
"""
name1 = input("what is your name:")
name2 = input("what is her name:")
combine_case_string = name1 + name1

t = combine_case_string.count('t')
r = combine_case_string.count('r')
u = combine_case_string.count('u')
e = combine_case_string.count('e')
true = t+r+u+e

l = combine_case_string.count('l')
o = combine_case_string.count('o')
v = combine_case_string.count('o')
e = combine_case_string.count('e')
love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score<10 or love_score>90:
    print(f"your score is {love_score}")
elif love_score>=40 & love_score<=50:
    print(f"your score is {love_score}")
else:
    print(f"your love score is {love_score}")
"""
"""
numbers = [10,0,-1,7,8,10,-67]
#names = ["naleer","mysara"]
#mix_list = [12,"afraj",10.01]
print(numbers.pop())
print(numbers)
#print(numbers[1:3])
#print(names)
#print(mix_list)
#print(type(mix_list))
"""
"""
import random
a = random.randint(0,1)
if a == 1:
    print("heads")
else:
    print("tails")
"""
#set1 = {'ram','shyam','jenny'}
#set2 = {'jenny','jiya','aakash'}
#set3 = {'ankur','pradeep'}
#print(set1.union(('ram','numa')))
#print(set1|set2|set3)
#set2.union(set1)
#set1.update(['jenny','mohan'])
#print(set1)
#print(set1.intersection(set2))
#print(set1&set2)
#set1.intersection_update(set2)
#print(set1)
#print(set1.difference(set2,set3))
#print(set1-set2)
#set1.difference_update(set2)
#print(set1)
#print(set1.symmetric_difference(set2))
#print(set1^set2^set3)
#set2.symmetric_difference_update(set1)
#print(set2)
"""
set1 = {1,2,3,4,5,7,10,8,-10,53}
set2 = {4,10,7,8,-10,1,2,3,4,5}
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))


name = "afraj"
for i in name:
    print(i)
    if i == "a":
        print("it is my first letter")


numbers = [2,3,5,-2,10]
squares = []
for i in numbers:
    square = i**2
    squares.append(square)
print(squares)
"""
"""
tuple1 = (2,3,5,56,353)
for i in tuple1:
    print(i)
    if i == 5:
        break
else:
    print("loop succcessfully completed")
"""
"""
a = range(10,0,-1)
#print(a[0])
for i in a:
    print(i)

total = 0
for i in range(1,101):
    total +=i
print(total)

total = 0
for i in range(0,100,2):
    total +=i
print(total)

total = 0
for i in range(0,101):
    if i%2==0:
        total +=i
print(total)
"""
"""
count = 1
while count<=5:
    print(count)
    count +=1
    if count==3:
        break

else:
    print("in else block")
print("out from loop")

number =int(input("enter a number : "))
while number != -1:
    print(number)
    number =int(input("enter a number : "))
else:
    print("in else block")
print("out from loop")

number = int(input("enter a number : "))
total = 0
while number!=-1 and number!=0:
    total += number
    number = int(input("enter a number : "))
print(total)


count = 1
while count<=10:
    print(count)
    count +=1
    if count==7:
        break
    print("hi")
print("out from loop")

list1 = ["hi","hello","welcome"]
names = ["krishn","ram","madhav"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name == "ram":
            continue
    print("out from inner loop")
print("out from outer loop")
"""
list = ['a','f','r','a','j']
print(len(list))
