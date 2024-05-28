""" General knowledge quiz program that tests students' knowledge of 
New Zealand. The quiz is only meant for children from 5 to 11 years of age.

v8 ABCD check and list
"""

quizA_ques = ["1. What is the capital of New Zealand?\n", "2. Which city is known as 'The Garden City'?\n", "3. Where did L&P soda originally come from?\n", "4. In what month is Matariki celebrated?\n", "5. What colour is kakariki?\n"]
    # List for each question in Quiz A. Each question will be printed out when needed with its corresponding index number.

quizB_ques = ["1. What is the name of the stretch of water that seperates the North and South Islands?\n", "2. Which New Zealand city houses the Beehive?\n", "3. Which town has a giant carrot as a landmark?\n", "4. Where is 90-mile beach?\n", "5. When was the Treaty of Waitangi signed?\n"]
    # List for each question in Quiz B. Each question will be printed out when needed with its corresponding index number.

quizA_answers = ['B', 'B', 'C', 'C', 'A'] # Quiz answers placed in a list for ease of editing
    # The answers for quiz A. The program will decide whether a user's answer is right or wrong using these answers and their index number depending on which question is being marked.

quizB_answers = ['C', 'A', 'D', 'A', 'B'] 
    # The answers for quiz B. The program will decide whether a user's answer is right or wrong using these answers and their index number depending on which question is being marked.

ABCD = ['A','B', 'C', 'D'] # Creating a list for possible answers makes programming error-handeling way easier / less tedious

# Lists of options created for each question in the quizes so programmers can go back and edit questions as they please easily. Makes the functions more concise.
quizA_ques1_op = ["A) Auckland", "B) Wellington", "C) Christchurch", "D) Hamilton\n"]
quizA_ques2_op = ["A) Wellington", "B) Christchurch", "C) Paeroa", "D) Auckland\n"]
quizA_ques3_op = ["A) Putaruru", "B) Waihi", "C) Paeroa", "D) Auckland\n"]
quizA_ques4_op = ["A) April", "B) May", "C) May, June, July", "D) July\n"]
quizA_ques5_op = ["A) Green", "B) Blue", "C) Black", "D) Grey\n"]

quizB_ques1_op = ["A) Wellington Strait", "B) Tasman Channel", "C) Cook Strait", "D) Kaikoura Strait"]
quizB_ques2_op = ["A) Wellington", "B) Christchurch", "C) Paeroa", "D) Auckland"]
quizB_ques3_op = ["A) Taihape", "B) Waihi", "C) Paeroa", "D) Ohakune"]
quizB_ques4_op = ["A) Top of the North Island", "B) Bottom of the South Island", "C) Bottom of the North Island", "D) Top of the South Island"]
quizB_ques5_op = ["A) 1815", "B) 1840", "C) 1855", "D) 1875"]


def name_check(name):
    while True:
        if name.isalpha() and len(name) >= 3:
            break
        else:
            name = input("Enter a valid name: ")
    return name.capitalize()

def age_check(question):
    """ Checks for valid integer """
    int_error = "\nSorry, you must enter a valid integer."
    age_ = ''
    while not age_:
        try:
            age_ = int(input(question))
        except ValueError:
            print(int_error)
    return age_


def quizA():
    """ Quiz A's Program """

    score = 0
    print(quizA_ques[0]) # Question 1 is called
    
    for options in quizA_ques1_op:
        print(options) # Question 1's options are displayed

    user_answer = str(input(">> ")) # Program takes the user's input answer

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break
        
    if user_answer.capitalize() == quizA_answers[0]: # If the user's answer matches this quiz's first answer (index 0)
        print('Well done, you got that right!') # ...then they get that question right
        score += 1 # 1 point is added

    if user_answer.capitalize() != quizA_answers[0]: # However, if the user's answer does NOT match the first answer of this quiz's answer list...
        print('Sorry, that was incorrect.') # ...they get that question wrong


    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizA_ques[1]) # Question 2 is called

    for options in quizA_ques2_op:
        print(options) # Question 2's options are displayed

    user_answer = str(input(">> ")) # Program takes the user's input answer

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    if user_answer.capitalize() == quizA_answers[1]: # If the user's answer matches this quiz's second answer (index 1)...
        print("Well done, you got that right!") # ... then they get that question right
        score += 1 # 1 point is added

    elif user_answer.capitalize() != quizA_answers[1]: # However, if the user's answer does NOT match the second answer of this quiz's answer list...
        print('Sorry, that was incorrect.')

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizA_ques[2]) # Question 3 is called

    for options in quizA_ques3_op:
        print(options) # Question 3's options are displayed

    user_answer = str(input(">> ")) # Program takes the user's answer input

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    if user_answer.capitalize() == quizA_answers[2]: # If the user's answer matches this quiz's third answer (index 2)...
        print("Wel done, you got that right!") # ... then they get that question right
        score += 1

    elif user_answer.capitalize() != quizA_answers[2]: # However, if the user's answer does NOT match the third answer of this quiz's answer list...
        print("Sorry, that was incorrect.") # ... they get that quesiton wrong

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizA_ques[3]) # Question 4 is called

    for options in quizA_ques4_op:
        print(options) # Question 4's options are displayed

    user_answer = str(input(">> ")) # Program takes the user's answer input

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    if user_answer.capitalize() == quizA_answers[3]: # If the user's answer matches this quiz's fourth answer (index 3)...
        print("Well done, you got right!") # ... then they get that question right
        score += 1

    elif user_answer.capitalize() != quizA_answers[3]: # However, if the user's answer does NOT match the fourth answer of this quiz's answer list...
        print("Sorry, that was incorrect.") # ... they get that question wrong

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizA_ques[4]) # Question 5 is called

    for options in quizA_ques5_op:
        print(options)

    user_answer = str(input(">> ")) # Program takes the user's answer input

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    if user_answer.capitalize() == quizA_answers[4]: # If the user's answer matches this quiz's fifth answer (index 4) 
        score += 1 # ... they get that question right and their score is incremented by 1

    elif user_answer.capitalize() != quizA_answers[4]: # However, if the user's answer does NOT match the fifth answer of this quiz's answer list...
        print("Sorry, that was incorrect.")

    if score >= 3:
        print(f"You scored {score} points out of 5! Well done!")
    elif score != 1:
        print(f"You scored {score} out of 5 points... better luck next time!")
        
        if score == 1:
            print(f"You scored 1 out of 5 points... better luck next time!")


def quizB(): # For Quiz B
    score = 0

    print(quizB_ques[0]) # Question 1 is called
    for options in quizB_ques1_op:
        print(options)

    user_answer = str(input(">> ")) # Program takes the user's answer input

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[0]: # If the user's answer matches this quiz's first answer (index 0)...
        print("Well done, you got that right!") # ... they get that question right
        score += 1

    elif user_answer != quizB_answers[0]: # However, if the user's answer does NOT match the first answer of this quiz's answer list...
        print("Sorry, that was wrong.")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizB_ques[1])
    for options in quizB_ques2_op:
        print(options)

    user_answer = str(input(">> "))

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[1]:
        print("Well done, you got that right!")
        score += 1

    elif user_answer != quizB_answers[1]:
        print("Sorry, that was wrong.")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizB_ques[2])
    for options in quizB_ques3_op:
        print(options)

    user_answer = str(input(">> "))

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[2]:
        print("Well done, you got that right!")
        score += 1

    elif user_answer != quizB_answers[2]:
        print("Sorry, that was wrong.")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizB_ques[3])
    for options in quizB_ques4_op:
        print(options)

    user_answer = str(input(">> "))

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[3]:
        print("Well done, you got that right!")
        score += 1

    elif user_answer != quizB_answers[3]:
        print("Sorry, that was wrong.")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    print(quizB_ques[4])
    for options in quizB_ques5_op:
        print(options)

    user_answer = str(input(">> "))

    if user_answer.capitalize() not in ABCD: # If the user enters something other than A, B C, or D

        while user_answer.capitalize() not in ABCD:
            print("\nPlease enter either A, B, C, or D.")
            user_answer = str(input(">> "))

            if user_answer.capitalize() in ABCD:
                break

    user_answer = user_answer.capitalize()

    if user_answer == quizB_answers[4]:
        print("Well done, you got that right!")
        score += 1

    elif user_answer != quizB_answers[4]:
        print("Sorry, that was wrong.")

    if score >= 3:
        print(f"You scored {score} points out of 5! Well done!")

    elif score != 1:
        print(f"You scored {score} out of 5 points.... better luck next time!")

        if score == 1:
            print(f"You scored 1 out of 5 points... better luck next time!")

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Main Routine

print("\n= = = = = = = = = = Kiwi Quiz = = = = = = = = = =\n")
print()
print("1. The quizes are only meant for children whose ages are from 5 - 11 years\n\
\n2. Each quiz will consist of atleast 5 qustions\n\
\n3.  There are two quiz sets available and you have been given a specific one\n\
    depending on your age (5-7 or 8-11). If you are older but you just want \n\
    something you can breeze through, or you're younger and you would like a \n\
    challenge, pick the opposite age group.\n") # Prints quiz rules

name = input("Please enter your name: ") # Program asks for user input name
name = name_check(name) # name_check function checks that the name is valid. Function will return the capitalized name once it confirms it is valid. This is what the function will return

age = age_check("What's your age in years?: ") # Takes age input and checks that it is valid

valid_age = False # Variable that helps the program determine whether the user's age is considered valid (True) or invalid (False). If it's invalid, it prints an error message and asks them to re-enter

quizA_age = False # Helps the program decide which quiz to run
quizB_age = False # (Same as above)

if age <= 7 and age >= 5: # If the user's age is less than or equal to 7 AND greater than or equal to 5 (5 - 7), they get Quiz A
    quizA_age = True
    valid_age = True
    
if age > 7 and age <= 11: # If the user's age is greater than 7 AND less than or equal to 11 (7 - 11), they get Quiz B
    quizB_age = True
    valid_age = True
    
while valid_age == False: # If their age is anything out of the required age range, they get kicked out
    print("\nSorry, this program is only meant for children aged from 5 - 11 years.")
    age = age_check("What's your age in years?: ")

    if age <= 7 and age >= 5: # If the user's age is less than or equal to 7 AND greater than or equal to 5 (5 - 7), they get Quiz A
        quizA_age = True
        valid_age = True
    
    if age > 7 and age <= 11: # If the user's age is greater than 7 AND less than or equal to 11 (7 - 11), they get Quiz B
        quizB_age = True
        valid_age = True

if valid_age == True:
    print(f"\nHey there, {name}. Welcome to the Kiwi Quiz!\n\tLet's begin...\n") # Welcome

if quizA_age == True:
    quizA()
elif quizB_age == True:
    quizB()
