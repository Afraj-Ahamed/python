# def greet(name, dept , subject = "none"):
#     print(f"hi , {name}")
#     print(f"are you from {dept} department?")

# greet(name ="afrrj" , dept ="com")

def add(*numbers): #(5,6,7)
    c = 0
    for i in numbers:
        c = c+i
    print(f"sum is {c}")

add(5,6,7)