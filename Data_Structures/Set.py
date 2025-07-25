# Que1: Write a program to remove a given item from the set.

my_set = {1, 2, 3, 4, 5}

my_set.discard(3)  

print("Set after removal:", my_set)

# Que2: Write a program to create an intersection of sets.
	
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1 & set2 

print("Intersection:", intersection)

# Que3: Write a program to create an union of sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}


union_set = set1 | set2 

print("Union:", union_set)

	
# Que4: Write a program to find the maximum and minimum value in a set.

my_set = {10, 25, 5, 100, 50}

max_value = max(my_set)
min_value = min(my_set)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
