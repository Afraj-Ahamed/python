"""
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = [1,2,3,4,5,6,7,8,9]
symbols = ["@","#","$","%","^","&","*","()","-","+","="]

n_numbers = int(input("how many numbers would you like : "))
n_letters = int(input("how many letters would you like : "))
n_symbols = int(input("how many symbols would you like : "))

numbers_results = random.choices(numbers,k=n_numbers)
letter_results = random.choices(letters,k=n_letters)
symbol_results = random.choices(symbols,k=n_symbols)

password = numbers_results + letter_results + symbol_results
random.shuffle(password)

print(numbers_results)
print(letter_results)
print(symbol_results)
print(type(letter_results))

for i in password:
    print(i,end="")

# i tried by using ai
"""
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
           'O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','^','%','&','*','()','-','+','=']

n_number = int(input("how many number would you like : "))
n_letter = int(input("how many letter would you like : "))
n_symbol = int(input("how many symbol would you like : "))
password_list = []

for i in range(1,n_number+1):
    char = random.choice(numbers)
    password_list += char

for i in range(1,n_letter+1):
    char = random.choice(letters)
    password_list += char

for i in range(1,n_symbol+1):
    char = random.choice(symbols)
    password_list += char

print(password_list)
random.shuffle(password_list)
print(password_list)
pasword = ""
for i in password_list:
    pasword += i
print(pasword)


