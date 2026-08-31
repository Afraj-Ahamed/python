numbers = input("enter a number separated by comma:")
number_list = numbers.split(",")
print(number_list)
for num in range(len(number_list)):
    number_list[num]=int(number_list[num])

largest = number_list[0]
for lar in number_list:
    if lar > largest:
        largest=lar
print(f"maximum number is :{largest}")