numbers = [1,2,3,4,5]
print(numbers)

print(1 in numbers)       #checks for 1 in the list


print(len(numbers))       #checks the number of elements in the given list


numbers.append(6)         #adds 6 in the last of the list
print(numbers)

numbers.insert(0, -1)     #inserting -1 at the 0th index of the list
print(numbers)

numbers.remove(3)         #removes 3 from the list not the 3th index element
print(numbers)

numbers.clear()           #deletes whole list objects
print(numbers)