# Project 1: Tech Module: Command Line Arguments

import sys

def calculate_happiness():
    try:
        if len(sys.argv) != 4:
            print("Usage: python script.py <like-string> <dislike-string> <given-string>")
            return

        like_str = sys.argv[1]
        dislike_str = sys.argv[2]
        given_str = sys.argv[3]

        like_set = set(like_str.split('-'))
        dislike_set = set(dislike_str.split('-'))
        given_list = given_str.split('-')

        happiness = 0
        for num in given_list:
            if num in like_set:
                happiness += 1
            elif num in dislike_set:
                happiness -= 1

        print(happiness)

    except Exception as e:
        print(f"Error occurred: {e}")

calculate_happiness()
