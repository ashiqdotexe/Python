print("Enter your age: ", end="")
age=int(input())
if age>7 and age<100:
    if age > 18:
        print("You are elligible for driving licence")
    elif age == 18:
        print("We cant decide")
    else:
        print("You are not elligible for driving licence")
else:
    print("Invalid age")

