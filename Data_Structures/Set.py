# Que1: Write a program to remove a given item from the set.

my_set = {1, 2, 3, 4, 5}

# Remove item 3 from the set
my_set.discard(3)  # Use discard to avoid error if item doesn't exist

print("Set after removal:", my_set)

# Que2: Write a program to create an intersection of sets.
	
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Intersection of set1 and set2
intersection = set1 & set2  # or set1.intersection(set2)

print("Intersection:", intersection)

# Que3: Write a program to create an union of sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of set1 and set2
union_set = set1 | set2  # or set1.union(set2)

print("Union:", union_set)

	
# Que4: Write a program to find the maximum and minimum value in a set.

my_set = {10, 25, 5, 100, 50}

# Find max and min values
max_value = max(my_set)
min_value = min(my_set)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
