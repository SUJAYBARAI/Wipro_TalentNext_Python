# Project 1: Tech Module: Data Structure

people_facts = {
    "Jeff": "Is afraid of dogs",
    "David": "Plays the piano",
    "Jason": "Can fly an airplane"
}

print("Initial List of People and Facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}.")

print("\nUpdating facts...\n")

people_facts["Jeff"] = "Is afraid of heights"

people_facts["Jill"] = "Can hula dance"

print("Updated List of People and Facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}.")


# Project 2:

def find_runner_up(scores):
    unique_scores = list(set(scores))  # Remove duplicates
    unique_scores.sort(reverse=True)   # Sort in descending order
    if len(unique_scores) >= 2:
        return unique_scores[1]        # Second highest
    else:
        return "No runner-up found"

scores = [2, 3, 6, 6, 5]
runner_up = find_runner_up(scores)
print("Runner-up score:", runner_up)




# Project 3:

def calculate_average(marks):
    return sum(marks) / len(marks)

student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}


name = input("Enter a name: ")

if name in student_marks:
    average = calculate_average(student_marks[name])
    print(f"Average percentage mark: {average:.2f}")
else:
    print("Student not found.")





# Project 4:
# Given a string of n words, help Alex to find out how many times his name appears in the string. 
# Constraint:1 <= n <= 200
# Sample input: Hi Alex WelcomeAlex Bye Alex.
# Sample output:3
# Explanation:Alex name appears 3 times in the string. Hi AlexWelcomeAlexBye Alex

def count_alex_occurrences(text):
    # Split string into words
    words = text.split()
    
    # Count exact matches of 'Alex'
    return words.count('Alex')

# Input string
input_string = input("Enter the string: ")

# Get count
count = count_alex_occurrences(input_string)

print("Alex appears", count, "times.")
