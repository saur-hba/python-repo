numbers = [1,2,3,4,5,8,7,9]
print(numbers)

print(1 in numbers)       #checks for 1 in the list

numbers.sort()            #sorts list in inc order
print(numbers)

numbers.sort()            #sorts list in dec order
numbers.reverse()
print(numbers)


print(len(numbers))       #checks the number of elements in the given list


numbers.append(6)         #adds 6 in the last of the list
print(numbers)

numbers.pop()              #removes last element from the list
print(numbers)

numbers.pop(2)              #removes third element from the list
print(numbers)

numbers.insert(0, -1)     #inserting -1 at the 0th index of the list
print(numbers)

numbers.remove(8)         #removes 8 from the list not the 8th index element
print(numbers)

numbers2 = numbers.copy()
numbers.append(22)
print(numbers2)
print(numbers)

numbers.clear()           #deletes whole list objects
print(numbers)

