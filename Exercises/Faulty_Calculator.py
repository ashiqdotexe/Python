a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
oper=input("Enter the operation you wanna do: ")
if oper=="+":
    if(a!=56 and b!=9):
        print(a+b)
    else:
        print(77)
elif oper=="/":
    if (a != 56 and b != 6):
        print(a/b)
    else:
        print(4)
elif oper=="*":
    if (a != 45 and b != 3):
        print(a*b)
    else:
        print(555)
else:
    print("Invalid operation")