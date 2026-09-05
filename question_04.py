"""def greet_user(name):
    print(f"hello , {name}")

greet_user("afraj")
"""
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Testing default argument
greet_user("Alice")

# Testing custom argument overriding default
greet_user("Bob", "Welcome")