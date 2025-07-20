#  Que 1: Write a program to accept two numbers as command line arguments and display their sum.

# sum_two_numbers.py
import sys

if len(sys.argv) != 3:
    print("Usage: python sum_two_numbers.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum:", num1 + num2)


# Que 2: Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.


# welcome_message.py
import sys

if len(sys.argv) != 2:
    print("Usage: python welcome_message.py <welcome_message>")
else:
    print("File name:", sys.argv[0])
    print("Welcome message:", sys.argv[1])

# Que 3: Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

# sum_primes.py
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Usage: python sum_primes.py <10 numbers>")
else:
    numbers = list(map(int, sys.argv[1:]))
    prime_sum = sum(num for num in numbers if is_prime(num))
    print("Sum of prime numbers:", prime_sum)
