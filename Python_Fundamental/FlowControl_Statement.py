# Que1: Write a program to check if a given number is Positive, Negative, or Zero.

a=int(input("Enter a Number: "))

if a>0:
    print("Postive")

elif a==0:
    print("Zero")

else:
    print("Negative")


# Que2: Write a program to check if a given number is odd or even.

a=int(input("Enter a Number: "))

if a%2==0:
    print("Even")

else :
    print("Odd")



# Que3: Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

def lastDigit(a,b):
    return a%10==b%10

a=int(input("Enter first Number: "))
b=int(input("Enter second Number: "))

print(lastDigit(a,b))


# Que4:  Write a program to print numbers from 1 to 10 in a single row with one tab space.

for i in range(1,11):
    print(i,"   ",end="")


# Que5: Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.

for i in range(23,58):
    if i%2==0:
        print(i)


# Que6:  Write a program to check if a given number is prime or not.

def prime(n):
    if n<=0:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

        
num= int(input("Enter a number: "))
if prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

# Que7: Write a program to print prime numbers between 10 and 99.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 10 and 99 are:")
for num in range(10, 100):
    if is_prime(num):
        print(num, end=' ')



# Que8: Write a program to print the sum of all the digits of a given number.
# Example:
# I/P:1234
# O/P:10

num= int(input("Enter a number: "))
sum=0
while num>0:
    digit=num%10

    sum=sum+digit

    num=num//10
print (sum)



# Que9: Write a program to reverse a given number and print.

# Example:1
# I/P: 1234
# O/P:4321

# Example:2
# I/P:1004
# O/P:4001

num= int(input("Enter a number: "))
rev=0
while num>0:
    digit=num%10

    rev=rev*10+digit

    num=num//10
print (rev)




# Que10: Write a program to find if the given number is palindrome or not

# Example:1
# I/P:110011
# O/P: 110011 is a palindrome.

# Example:2
# I/P:1234
# O/P: 1234 is not a palindrome.

num= int(input("Enter a number: "))
copy=num
rev=0
while num>0:
    digit=num%10

    rev=rev*10+digit

    num=num//10
if copy==rev:
    print("Palindrom")

else:
    print("Not Palindrom")