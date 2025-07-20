# Que 1: Write a function to return the sum of all numbers in a list.  
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def sum_of_list(numbers):
    return sum(numbers)

# Example:
print(sum_of_list([8, 2, 3, 0, 7])) 



# Que 2: Write a function to return the reverse of a string.  
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_string(s):
    return s[::-1]

# Example:
print(reverse_string("1234abcd"))  


# Que:3 Write a function to calculate and return the factorial of a number (a non-negative integer).


def factorial(n):
    if n < 0:
        return "Error: Negative number not allowed"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact


print(factorial(5))  


# Que 4: Write a function that accepts a string and prints the number of upper case letters and lower case letters in it. 


def count_case(s):
    upper = lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

# Example:
count_case("Hello World")  



# Que 5: Write a function to print the even numbers from a given list. List is passed to the function as an argument. 
#  Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
	

def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Example:
print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))  



# Que 6: Write a function that takes a number as a parameter and checks whether the number is prime or not.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example:
print(is_prime(7))   
print(is_prime(10))  