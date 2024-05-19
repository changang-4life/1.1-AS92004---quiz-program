""" General knowledge quiz program that tests students' knowledge of 
New Zealand. The quiz is only meant for children from 5 to 11 years of age.

v1 - greeting and user's name, rules variable
"""

name = str(input("What is your name?: "))
name = name.capitalize()


rules = '1. The quiz is only meant for children whose ages are from 5 - 11 years\n\
\n2. Each quiz will consist of atleast 5 qustions\n\
\n3. There are two quiz sets available and you will be given a specific one\n\
    depending on your age (5-7 or 8-11). If you are older but you just want \n\
    something you canbreeze through, or you are younger and you would like a \n\
    challenge, pick a different age group <3'

print(f"Hello there, {name}. Welcome to the Kiwi Quiz!\nHere are the rules: ")

print(rules)

age = int(input("How old are you in years?: "))