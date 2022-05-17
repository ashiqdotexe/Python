list=[["Sohan",4],["Rohan",8],["Sajid",7]]
dic=dict(list)
for item,candy in dic.items():
    if str(candy).isnumeric() and candy>5:
        print(item,candy)
for item in dic:
    print(item,end=",")