for i in range(0,101):
    if i%3==0 and i%5==0:
        print("fizz and bizz")
    elif i%5==0:
        print("bizz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)