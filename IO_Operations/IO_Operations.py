# Que 1: Write a program to read the entire content from a txt file and display it to the user.

filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found.")


# Que 2: Write a program to read first n lines from a txt file. Get n as user input.


filename = input("Enter the filename: ")
n = int(input("Enter the number of lines to read: "))

try:
    with open(filename, 'r') as file:
        for i in range(n):
            line = file.readline()
            if line:
                print(line.strip())
            else:
                break
except FileNotFoundError:
    print("Error: File not found.")

# Que 3: Write a program to accept input from user and append it to a txt file.

filename = input("Enter the filename: ")
text = input("Enter the text to append: ")

try:
    with open(filename, 'a') as file:
        file.write(text + '\n')
        print("Text appended successfully.")
except Exception as e:
    print("An error occurred:", e)

	
# Que 4: Write a program to read contents from a txt file line by line and store each line into a list.

filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
        print("Lines stored in list:\n", lines)
except FileNotFoundError:
    print("Error: File not found.")

	
# Que 5: Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.


filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        print("Longest word:", longest_word)
except FileNotFoundError:
    print("Error: File not found.")

# Que 6: Write a program to count the frequency of a user entered word in a txt file.


filename = input("Enter the filename: ")
search_word = input("Enter the word to search: ")

try:
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        count = words.count(search_word)
        print(f"The word '{search_word}' appears {count} times.")
except FileNotFoundError:
    print("Error: File not found.")
