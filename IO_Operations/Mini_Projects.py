# Project 1: IO Operations

from collections import Counter
import string

def get_meeting_time(line_count):
    if line_count == 0:
        return "Unknown"
    elif line_count <= 12:
        return f"{line_count} AM"
    else:
        return f"{line_count % 12 or 12} PM"

def clean_word(word):
    return word.strip(string.punctuation).lower()

def find_secret_message():
    try:
        filename = input("Enter the file name:\n")
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        line_count = len(lines)
        all_words = []

        for line in lines:
            words = line.strip().split()
            cleaned = [clean_word(word) for word in words if word.strip()]
            all_words.extend(cleaned)

        if not all_words:
            print("No words found in the file.")
            return

        word_freq = Counter(all_words)
        meeting_word, freq = word_freq.most_common(1)[0]
        meeting_place = meeting_word.capitalize() + " Street"
        meeting_time = get_meeting_time(line_count)

        print(f"Meeting time: {meeting_time}")
        print(f"Meeting place: {meeting_place}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

find_secret_message()
