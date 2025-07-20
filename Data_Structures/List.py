#  Que1: Write a program to create a list of 5 integers and display the list items. Access individual elements through index.

 # Creating a list of 5 integers
numbers = [10, 20, 30, 40, 50]

# Display the list
print("List:", numbers)

# Accessing individual elements by index
print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Fourth element:", numbers[3])
print("Fifth element:", numbers[4])



#  Que2: Write a program to append a new item to the end of the list.
	
numbers = [1, 2, 3, 4, 5]

# Appending a new item
numbers.append(6)

print("Updated list:", numbers)



#  Que3: Write a program to reverse the order of the items in the list.

numbers = [1, 2, 3, 4, 5]

# Reversing the list
numbers.reverse()

print("Reversed list:", numbers)


#  Que4: Write a program to print the number of occurrences of a specified element in a list.

numbers = [1, 2, 3, 2, 4, 2, 5]

# Count occurrences of 2
count = numbers.count(2)

print("Number of occurrences of 2:", count)


	
#  Que5: Write a program to append the items of list1 to list2 in the front.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Append list1 to the front of list2
list2 = list1 + list2

print("Updated list2:", list2)



#  Que6: Write a program to insert a new item before the second element in an existing list.

numbers = [10, 20, 30, 40]

# Insert 15 before second element (index 1)
numbers.insert(1, 15)

print("List after insertion:", numbers)


	
#  Que7: Write a program to remove the item from a specified index in a list.

numbers = [10, 20, 30, 40, 50]

# Remove item at index 2 (which is 30)
del numbers[2]

print("List after deletion:", numbers)



#  Que8: Write a program to remove the first occurrence of a specified element from a list.
numbers = [10, 20, 30, 20, 40]

# Remove first occurrence of 20
numbers.remove(20)

print("List after removing first occurrence of 20:", numbers)
