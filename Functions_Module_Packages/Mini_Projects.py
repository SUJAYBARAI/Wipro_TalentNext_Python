# Project 1: Tech Module: Functions/Modules/Packages
def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()  
    return '-'.join(colors)

input_colors = input("Enter hyphen-separated colors: ")
sorted_colors = sort_colors(input_colors)
print("Sorted colors:", sorted_colors)


# Project 2: 

def is_palindrome(name):
    name = name.replace(" ", "")  
    return name == name[::-1]

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in name if char in vowels)

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char != ' ': 
            freq[char] = freq.get(char, 0) + 1
    return freq
