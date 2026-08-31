"""
height = input("enter a height separated by comma:")
height_list = height.split(",")

total = 0
count = 0

for i in height_list:
    total += int(i)
    count += 1

average = total/count

average_in_int = round(average,0)
print(average_in_int)
"""

heights = input("enter a height separated by comma:")
height_list = heights.split(",")

count = 0
for height in height_list:3

count = count + 1
print(count)

for i in range(count):
    height_list[i] = int(height_list[i])

total = 0
for person in height_list:
    total += person
avg = total / count

print(avg)