""" General knowledge quiz program that tests students' knowledge of 
New Zealand. The quiz is only meant for children from 5 to 11 years of age.

v4 - Score Mechanics Set Up
"""

name = str(input("What is your name?: "))
name = name.capitalize()


rules = '1. The quiz is only meant for children whose ages are from 5 - 11 years\n\
\n2. Each quiz will consist of atleast 5 qustions\n\
\n3.  There are two quiz sets available and you will be given a specific one\n\
    depending on your age (5-7 or 8-11). If you are older but you just want \n\
    something you can breeze through, or youre younger and you would like a \n\
    challenge, pick your opposite age group. \n'

print(f"Hello there, {name}. Welcome to the Kiwi Quiz!\nHere are the rules: ")

print(rules)

age = int(input("How old are you in years?: "))
print()

quizA_ques = ["1. What is the capital of New Zealand?\n", "2. Which city is known as 'The Garden City'?\n", "3. Where did L&P soda originally come from?\n", "4. In what month is Matariki celebrated?\n", "5. What colour is Kakariki?\n"]
    # List for each question in Quiz A. Each question will be printed out when needed with its corresponding index number.

quizB_ques = ["1. What is the anme of the stretch of water that seperates the North and South Islands?\n", "2. Which New Zealand city houses the Beehive?\n", "3. Which town has a giant carrot as a landmark?\n", "4. Where is 90 mile beach?\n", "5. When was the Treaty of Waitangi signed?\n"]
    # List for each question in Quiz B. Each question will be printed out when needed with its corresponding index number.

quizA_answers = ['B', 'B', 'C', 'C', 'A'] # Quiz answers placed in a list for ease of editing
    # The answers for quiz A. The program will decide whether a user's answer is right or wrong using these answers and their index number depending on which question is being marked.

quizB_answers = ['C', 'A', 'D', 'A', 'B'] 
    # The answers for quiz B. The program will decide whether a user's answer is right or wrong using these answers and their index number depending on which question is being marked.

# Lists of options created for each question in the quizes so programmers can go back and edit questions as they please easily. Makes the functions more concise.
quizA_ques1_op = ["A) Auckland", "B) Wellington", "C) Christchurch", "D) Hamilton\n"] 
quizA_ques2_op = ["A) Wellington", "B) Christchurch", "C) Paeroa", "D) Auckland\n"]
quizA_ques3_op = ["A) Putaruru", "B) Waihi", "C) Paeroa", "D) Auckland\n"]
quizA_ques4_op = ["A) April", "B) May", "C) May, June, July", "D) July\n"]
quizA_ques5_op = ["A) Green", "B) Blue", "C) Black", "D) Grey"]

quizB_ques1_op = ["A) Wellington Strait", "B) Tasman Chennel", "C) Cook Strait", "D) Kaikoura Strait"]
quizB_ques2_op = ["A) Wellington", "B) Christchurch", "C) Paeroa", "D) Auckland"]
quizB_ques3_op = ["A) Taihape", "B) Waihi", "C) Paeroa", "D) Ohakune"]
quizB_ques4_op = ["A) Top of the North Island", "B) Bottom of the South Island", "C) Bottom of the North Island", "D) Top of the South Island"]
quizB_ques5_op = ["A) 1815", "B) 1840", "C) 1855", "D) 1875"]


def quizA(): # For Quiz A

    score = 0
    print(quizA_ques[0]) # Question 1 is called
    
    for options in quizA_ques1_op:
        print(options) # Question 1's options are displayed

    user_answer = str(input(">> ")) # Program takes the user's input answer

    if user_answer.capitalize() == quizA_answers[0]: # If the user's answer matches this quiz's first answer (index 0)
        print('Well done, you got that right!') # ...then they get that question right
        score += 1 # 1 point is added

    elif user_answer.capitalize() != quizA_answers[0]: # However, if the user's answer does NOT match the first answer of this quiz's answer list...
        print('Sorry, that was incorrect.') # ...they get that question wrong
    
    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizA_ques[1]) # Question 2 is called

    for options in quizA_ques2_op:
        print(options) # Question 2's options are displayed

    user_answer = str(input(">> ")) # Program takes the user's input answer

    if user_answer.capitalize() == quizA_answers[1]: # If the user's answer matches this quiz's second answer (index 1)...
        print("Well done, you got that right!") # ... then they get that question right
        score += 1 # 1 point is added
    
    if user_answer.capitalize() != quizA_answers[1]: # However, if the user's answer does NOT match the second answer of this quiz's answer list...
        print('Sorry, that was incorrect.')

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizA_ques[2]) # Question 3 is called

    for options in quizA_ques3_op:
        print(options) # Question 3's options are displayed

    user_answer = str(input(">> ")) # Program takes the user's answer input

    if user_answer.capitalize() == quizA_answers[2]: # If the user's answer matches this quiz's third answer (index 2)...
        print("Wel done, you got that right!") # ... then they get that question right
        score += 1

    if user_answer.capitalize() != quizA_answers[2]: # However, if the user's answer does NOT match the third answer of this quiz's answer list...
        print("Sorry, that was incorrect.") # ... they get that quesiton wrong

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizA_ques[3]) # Question 4 is called

    for options in quizA_ques4_op:
        print(options) # Question 4's options are displayed

    user_answer = str(input(">> ")) # Program takes the user's answer input

    if user_answer.capitalize() == quizA_answers[3]: # If the user's answer matches this quiz's fourth answer (index 3)...
        print("Well done, you got right!") # ... then they get that question right
        score += 1

    if user_answer.capitalize() != quizA_answers[3]: # However, if the user's answer does NOT match the fourth answer of this quiz's answer list...
        print("Sorry, that was incorrect.") # ... they get that question wrong

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizA_ques[4]) # Question 5 is called

    for options in quizA_ques5_op:
        print(options)

    user_answer = str(input(">> ")) # Program takes the user's answer input

    if user_answer.capitalize() == quizA_answers[4]: # If the user's answer matches this quiz's fifth answer (index 4)...
        print("Wow! Good Job!") # ... they get that question right
        score += 1

    if user_answer.capitalize() != quizA_answers[4]: # However, if the user's answer does NOT match the fifth answer of this quiz's answer list...
        print("Sorry, that was incorrect.")

quizA()

def quizB(): # For Quiz B

    print(quizB_ques[0]) # Question 1 is called
    for options in quizB_ques1_op:
        print(options)

    user_answer = str(input(">> ")) # Program takes the user's answer input
    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[0]: # If the user's answer matches this quiz's first answer (index 0)...
        print("Well done, you got that right!") # ... they get that question right
        score += 1

    if user_answer != quizB_answers[0]: # However, if the user's answer does NOT match the first answer of this quiz's answer list...
        print("Sorry, that was wrong)")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizB_ques[1])
    for options in quizB_ques2_op:
        print(options)

    user_answer = str(input(">> "))
    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[1]:
        print("Well done, you got that right!")
        score += 1

    if user_answer != quizB_answers[1]:
        print("Sorry, that was wrong.")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizB_ques[2])
    for options in quizB_ques3_op:
        print(options)

    user_answer = str(input(">> "))
    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[2]:
        print("Well done, you got that right!")
        score += 1

    if user_answer != quizB_answers[2]:
        print("Sorry, that was wrong.")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizB_ques[3])
    for options in quizB_ques4_op:
        print(options)

    user_answer = str(input(">> "))
    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[3]:
        print("Well done, you got that right!")
        score += 1

    if user_answer != quizB_answers[3]:
        print("Sorry, that was wrong.")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    
    print(quizB_ques[4])
    for options in quizB_ques5_op:
        print(options)

    user_answer = str(input(">> "))
    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[4]:
        print("Well done, you got that right!")
        score += 1

    if user_answer != quizB_answers[4]:
        print("Sorry, that was wrong.")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    
    quizB()