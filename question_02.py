def check_number(num):
    if num>0 and num%2==0:
        print("Positive and Even")
    elif num>0 and num%2!=0:
        print("Positive and Odd")
    else:
        print("Zero or Negative")

check_number(4)
check_number(-4)
check_number(67)