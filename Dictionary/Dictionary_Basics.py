"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
#d1={}
#print(type(d1))
d2={"birth":"the emergence of a baby or other young from the body of its mother; the start of life as a physically separate being.","baby":"a very young child.",
    "young":"having lived or existed for only a short time.","offspring":"a person's child or children."}
print("Enter the word that you wanna search: ",end="")
userinput=input()
print(d2.get(userinput))