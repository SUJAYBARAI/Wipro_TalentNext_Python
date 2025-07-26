# Que 1: Write  a program to find check if a string has only octal digits. Given string ['789','123','004']


import re

strings = ['789', '123', '004']
for s in strings:
    if re.fullmatch(r'[0-7]+', s):
        print(f"{s} is an octal number")
    else:
        print(f"{s} is NOT an octal number")


#Que 2: Extract the user id, domain name and suffix from the following email addresses.
# emails  =  """zuck@facebook.com
# sunder33@google.com
# jeff42@amazon.com"""	

import re

emails = """zuck@facebook.com sunder33@google.com jeff42@amazon.com"""
matches = re.findall(r'(\w+)@([\w]+)\.(\w+)', emails)
print(matches)




#Que 3: Split the following irregular sentence into proper words
# sentence = """A, very   very; irregular_sentence"""  ##  expected outout : A very very irregular sentence
	

import re

sentence = """A, very very; irregular_sentence"""
words = re.split(r'[;,_\s]+', sentence)
clean_sentence = ' '.join(words)
print(clean_sentence)



# Que 4: Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
# #tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# ##desired_output = 'Good advice What I would do differently if I was learning to code today'
	

import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''


tweet = re.sub(r'\bRT\b|\bcc\b', '', tweet)

tweet = re.sub(r'http\S+', '', tweet)

tweet = re.sub(r'[@#]\w+', '', tweet)

tweet = re.sub(r'[^\w\s]', '', tweet)

tweet = re.sub(r'\s+', ' ', tweet).strip()

print(tweet)


# Que 5: Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html

# Code to retrieve the HTML page is given below:
# import requests
# r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
# r.text  # html text is contained here

# desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']

import requests
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text


results = re.findall(r'>([^<]+)<', html)

results = [text.strip() for text in results if text.strip()]
print(results)




#Que 6:  Given below list of words, identify the words that begin and end with the same character. 
# civic
# trust
# widows
# maximum
# museums
# aa
# as


import re

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matching_words = [word for word in words if re.fullmatch(r'(?i)(\w)\w*\1', word)]
print(matching_words)

