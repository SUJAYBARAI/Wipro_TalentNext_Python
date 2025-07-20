# Que 1: Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result of division:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print("Unexpected error:", e)

# Que 2: Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.

try:
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not a prime number.")
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("It is a prime number.")
except ValueError:
    print("Error: Please enter a valid integer.")


# Que 3: Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.


try:
    filename = input("Enter the file name to open: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("File content in title case:")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Unexpected error:", e)

    

# Que 4: Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.


numbers = [5, -3, 7, -8, 0, 12, -1, 6, -4, 9]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    if value > 0:
        print("The number at index", index, "is positive.")
    elif value < 0:
        print("The number at index", index, "is negative.")
    else:
        print("The number at index", index, "is zero.")
except IndexError:
    print("Error: Invalid index. Please enter between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")
