# def greet(name, dept , subject = "none"):
#     print(f"hi , {name}")
#     print(f"are you from {dept} department?")

# greet(name ="afrrj" , dept ="com")

# def add(*numbers): #(5,6,7)
#     c = 0
#     for i in numbers:
#         c = c+i
#     print(f"sum is {c}")

# add(5,6,7)

# def print_user_details(**details):
#     for key , value in details.items():
#         print(f"{key} : {value}")

# print_user_details(name="Afraj", dept="CS", year=3)

def display_info(title, *args, **kwargs):
    print("Title:", title)
    print("Args:", args)
    print("Kwargs:", kwargs)

display_info("Student Profile", "Tamil", "English", age=20, city="Chennai")