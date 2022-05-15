"""
Some important funtions for list::>>
sort(): Sorts the list in ascending order.
type(list): It returns the class type of an object.
append(): Adds one element to a list.
extend(): Adds multiple elements to a list.
index(): Returns the first appearance of a particular value.
max(list): It returns an item from the list with a max value.
min(list): It returns an item from the list with a min value.
len(list): It gives the overall length of the list.
clear(): Removes all the elements from the list.
insert(): Adds a component at the required position.
count(): Returns the number of elements with the required value.
pop(): Removes the element at the required position.
remove(): Removes the primary item with the desired value.
reverse(): Reverses the order of the list.
copy():  Returns a duplicate of the list
"""
list=[5,7,1,4,9,1,90,87]
print(list)
print(type(list))
list.append(23)
print(list)
number=[80,90,70]
list.extend(number)
print(list)
print(max(list))
print(min(list))
print(len(list))
"""list.clear()
print(list)"""
print(list.count(90))
list.pop()
print(list)
list.remove(90)
print(list)
list.sort()
print("List after sorting: ", list)
list.reverse()
print("List after reversing: ", list)
values=number.copy()
print("Copied Numbers: ", values)