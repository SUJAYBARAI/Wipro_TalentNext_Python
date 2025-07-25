# Que1: Write a program to print the 4th element from first and 4th element from last in a tuple.

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

print("4th element from start:", my_tuple[3])

print("4th element from end:", my_tuple[-4])



# Que2: Write a program to check whether an element exists in a tuple or not.

my_tuple = (1, 2, 3, 4, 5)

element = 3

if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")


# Que3: Write a program to convert a list into a tuple.
	
my_list = [10, 20, 30, 40]

my_tuple = tuple(my_list)

print("Converted tuple:", my_tuple)


	
# Que4: Write a program to find the index of an item in a tuple.
	
my_tuple = ('a', 'b', 'c', 'd', 'e')

index = my_tuple.index('c')

print("Index of 'c':", index)


# Que5: Write a program to replace last value of tuples in a list to 100.  
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]



sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

modified_list = [t[:-1] + (100,) for t in sample_list]

print("Modified list:", modified_list)
