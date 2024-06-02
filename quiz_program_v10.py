"""General knowledge kiwi quiz program.

Tests students' knowledge of New Zealand.

The quiz is only meant for children from 5 to 11 years of age.

v10 - Finishing touches, end-user improvements, PEP8
"""
# List for each question in Quiz A. Each question will be printed out when
# needed with its corresponding index number.
quiz_a_ques = ["\n─── ⋆⋅☆⋅⋆ ── 1. What is the capital of New Zealand? \
─── ⋆⋅☆⋅⋆ ──\n", " ─── ⋆⋅☆⋅⋆ ── 2. Which city is known as 'The Garden City'\
? ─── ⋆⋅☆⋅⋆ ──\n", "─── ⋆⋅☆⋅⋆ ── 3. Where did L&P soda originally come from? \
─── ⋆⋅☆⋅⋆ ──\n", "─── ⋆⋅☆⋅⋆ ── 4. In what month is Matariki celebrated? \
─── ⋆⋅☆⋅⋆ ──\n", "─── ⋆⋅☆⋅⋆ ── 5. What colour is kakariki? ─── ⋆⋅☆⋅⋆ ──\n"]

# List for each question in Quiz B. Each question will be printed out
# when needed with its corresponding index number.
quiz_b_ques = [" ─── ⋆⋅☆⋅⋆ ── 1. What is the name of the stretch of water \
that seperates the North and South Islands? ─── ⋆⋅☆⋅⋆ ── \n", " ─── ⋆⋅☆⋅⋆ ── \
2. Which New Zealand city houses the Beehive? ─── ⋆⋅☆⋅⋆ ── \n", "\
─── ⋆⋅☆⋅⋆ ── 3. Which town has a giant carrot as a landmark? ─── ⋆⋅☆⋅⋆ ── \
\n", " ─── ⋆⋅☆⋅⋆ ── 4. Where is 90-mile beach? ─── ⋆⋅☆⋅⋆ ── \n", " ─── ⋆⋅☆⋅⋆ \
── 5. When was the Treaty of Waitangi signed? ─── ⋆⋅☆⋅⋆ ── \n"]


# Quiz answers placed in a list for ease of editing

# The answers for quiz A. The program will decide whether a user's answer
# is right or wrong using these answers and their index number depending
# on which question is being marked.
quiz_a_ans = ['B', 'B', 'C', 'C', 'A']


# The answers for Quiz B
quiz_b_ans = ['C', 'A', 'D', 'A', 'B']

# Creating a list for possible answers makes programming error-handeling
# way easier / less tedious.
ABCD = ['A', 'B', 'C', 'D']

# Lists of options created for each question in the quizes so programmers can
# go back and edit questions as they please easily. Makes the quiz
# functions more concise.

# For Quiz A
quiz_a_ques1_op = ["A. Auckland", "B. Wellington", "C. Christchurch", "D. \
Hamilton\n"]
quiz_a_ques2_op = ["A. Wellington", "B. Christchurch", "C. Paeroa", "D. \
Auckland\n"]
quiz_a_ques3_op = ["A. Putaruru", "B. Waihi", "C. Paeroa", "D. Auckland\n"]
quiz_a_ques4_op = ["A. April", "B. May", "C. May, June, July", "D. July\n"]
quiz_a_ques5_op = ["A. Green", "B. Blue", "C. Black", "D. Grey\n"]

# For Quiz B
quiz_b_ques1_op = ["A. Wellington Strait", "B. Tasman Channel", "C. Cook \
Strait", "D. Kaikoura Strait"]
quiz_b_ques2_op = ["A. Wellington", "B. Christchurch", "C. Paeroa", "\
D. Auckland"]
quiz_b_ques3_op = ["A. Taihape", "B. Waihi", "C. Paeroa", "D. Ohakune"]
quiz_b_ques4_op = ["A. Top of the North Island", "B. Bottom of the \
South Island", "C. Bottom of the North Island", "D. Top of the South Island"]
quiz_b_ques5_op = ["A. 1815", "B. 1840", "C. 1855", "D. 1875"]


def name_check(name):
    """Check for valid name."""
    while True:
        if name.isalpha() and len(name) >= 3: # if name is completely a string
            # and its length is equal to or more than 3, the name is considered
            # valid
            break # and the loop breaks
        else:
            name = input("Enter a valid name: ")
            # else, the loop asks them to input a valid name
    return name.capitalize() # when the loop finishes, the user's capitalized
    # name is returned


def age_check(question):
    """Check for valid integer."""
    int_error = "\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Sorry, you must enter a valid \
integer. 🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨" # error message that will print if the user
# does not enter a number
    age_ = ''
    while not age_:
        try:
            age_ = int(input(question))
        except ValueError: # if there is a value error
            print(int_error) # the message pritns
    return age_ # age is returned when loop terminates


def quiz_a():
    """Control Quiz A."""
    while True:
        score = 0
        print(quiz_a_ques[0])  # Question 1 is called
        for options in quiz_a_ques1_op:
            print(options)  # Question 1's options are displayed

        user_answer = str(input(">> "))  # Program takes the user's input
        # answer.

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D.

            while user_answer.capitalize() not in ABCD: # if their answer is
                # not in the ABCD list,
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨") # an error message prints out
                user_answer = str(input(">> ")) # loop where they have to
                # enter a valid answer ( ABCD ) to break

                if user_answer.capitalize() in ABCD: # if their answer is valid
                    break

        if user_answer.capitalize() == quiz_a_ans[0]:  # If the user's
            # answer matches this quiz's first answer (index 0)
            print('Well done, you got that right!\n')  # ...then they get that
            # question right
            score += 1  # 1 point is added

        if user_answer.capitalize() != quiz_a_ans[0]:  # However, if the
            # user's answer does NOT match the first answer of this quiz's
            # answer list...
            print('Sorry, that was incorrect.\n')  # ...they get that question
            # wrong.

        # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        print(quiz_a_ques[1])  # Question 2 is called
        for options in quiz_a_ques2_op:
            print(options)  # Question 2's options are displayed

        user_answer = str(input(">> "))  # Program takes the user's input
        # answer.

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        if user_answer.capitalize() == quiz_a_ans[1]:  # If the user's
            # answer matches this quiz's second answer (index 1)...
            print("Well done, you got that right!\n")  # ... then they get
            # that question right
            score += 1  # 1 point is added

        elif user_answer.capitalize() != quiz_a_ans[1]:  # However, if the
            # user's answer does NOT match the second answer of this quiz's
            # answer list...
            print('Sorry, that was incorrect.\n')

        # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        print(quiz_a_ques[2])  # Question 3 is called
        for options in quiz_a_ques3_op:
            print(options)  # Question 3's options are displayed

        user_answer = str(input(">> "))  # Program takes the user's answer
        # input

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        if user_answer.capitalize() == quiz_a_ans[2]:  # If the user's
            # answer matches this quiz's third answer (index 2)...
            print("Wel done, you got that right!\n")  # ... then they get that
            # question right
            score += 1

        elif user_answer.capitalize() != quiz_a_ans[2]:  # However, if the
            # user's answer does NOT match the third answer of this quiz's
            # answer list...
            print("Sorry, that was incorrect.\n")  # ... they get that
            # question wrong

        # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        print(quiz_a_ques[3])  # Question 4 is called
        for options in quiz_a_ques4_op:
            print(options)  # Question 4's options are displayed

        user_answer = str(input(">> "))  # Program takes the user's answer
        # input.

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        if user_answer.capitalize() == quiz_a_ans[3]:  # If the user's
            # answer matches this quiz's fourth answer (index 3)...
            print("Well done, you got right!\n")  # ... then they get that
            # question right
            score += 1

        elif user_answer.capitalize() != quiz_a_ans[3]:  # However, if the
            # user's answer does NOT match the fourth answer of this quiz's
            # answer list...
            print("Sorry, that was incorrect.\n")  # ... they get that
            # question wrong
    # . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . .

        print(quiz_a_ques[4])  # Question 5 is called
        for options in quiz_a_ques5_op:
            print(options)

        user_answer = str(input(">> "))  # Program takes the user's answer
        # input.

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        if user_answer.capitalize() == quiz_a_ans[4]:  # If the user's
            # answer matches this quiz's fifth answer (index 4)
            score += 1  # ... they get that question right and their score is
            # incremented by 1

        elif user_answer.capitalize() != quiz_a_ans[4]:  # However, if the
            # user's answer does NOT match the fifth answer of this quiz's
            # answer list...
            print("Sorry, that was incorrect.\n")

        if score >= 3:
            print(f"You scored {score} points out of 5! Well done!")
        elif score != 1:
            print(f"You scored {score} points out of 5 points... better \
luck next time!")
            
        if score == 1:
            print(f"You scored 1 out of 5 points... better luck next time!")

        # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        replay = str(input("Do you want to play again? (Y / N): ")) # takes
        # the user input, Y or N if they want to replay the game or not

        while replay.capitalize() != 'Y' or replay.capitalize() != 'N':
            # checks if they input anything other than Y or N
            if replay.capitalize() == 'Y' or replay.capitalize() == 'N':
                break # if their input == Y or N, then the loop breaks
            else:
                replay = str(input("Please enter either Y or N: "))
                # else, the program asks them to input Y or N again


        if replay.capitalize() == 'Y': # if the user's input == Y, then the
            continue
            # quiz restarts

        elif replay.capitalize() == 'N':
            # if they input N
            break
            # the program finishes


def quiz_b(): 
    while True:
        """ Quiz B's Program """
        score = 0
        print(quiz_b_ques[0])  # Question 1 is called
        for options in quiz_b_ques1_op:
            print(options) # options for the question are printed

        user_answer = str(input(">> "))  # Program takes the user's answer
        # input

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        user_answer = user_answer.capitalize()

        if user_answer == quiz_b_ans[0]:  # If the user's answer matches
            # this quiz's first answer (index 0)...
            print("Well done, you got that right!\n")  # ... they get that
            # question right
            score += 1

        elif user_answer != quiz_b_ans[0]:  # However, if the user's answer
            # does NOT match the first answer of this quiz's answer list...
            print("Sorry, that was wrong.\n")

        # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        print(quiz_b_ques[1]) # question is printed
        for options in quiz_b_ques2_op: # options for the question are printed
            print(options)

        user_answer = str(input(">> "))

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        user_answer = user_answer.capitalize()

        if user_answer == quiz_b_ans[1]:
            print("Well done, you got that right!\n")
            score += 1

        elif user_answer != quiz_b_ans[1]:
            print("Sorry, that was wrong.\n")

        # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        print(quiz_b_ques[2]) # question is printed
        for options in quiz_b_ques3_op: # options for the question are pritned
            print(options)

        user_answer = str(input(">> "))

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        user_answer = user_answer.capitalize()

        if user_answer == quiz_b_ans[2]:
            print("Well done, you got that right!\n")
            score += 1

        elif user_answer != quiz_b_ans[2]:
            print("Sorry, that was wrong.\n")

        # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        print(quiz_b_ques[3]) # question is printed
        for options in quiz_b_ques4_op: # options for the questions are printed
            print(options)

        user_answer = str(input(">> "))

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        user_answer = user_answer.capitalize()

        if user_answer == quiz_b_ans[3]:
            print("Well done, you got that right!\n")
            score += 1

        elif user_answer != quiz_b_ans[3]:
            print("Sorry, that was wrong.\n")

        # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        print(quiz_b_ques[4]) # options are printed
        for options in quiz_b_ques5_op: # options for the questions are printed
            print(options)

        user_answer = str(input(">> "))

        if user_answer.capitalize() not in ABCD:  # If the user enters
            # something other than A, B C, or D

            while user_answer.capitalize() not in ABCD:
                print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨 Please enter either A, B, C, \
or D.🚨 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
                user_answer = str(input(">> "))

                if user_answer.capitalize() in ABCD:
                    break

        user_answer = user_answer.capitalize()

        if user_answer == quiz_b_ans[4]:
            print("Well done, you got that right!\n")
            score += 1

        elif user_answer != quiz_b_ans[4]:
            print("Sorry, that was wrong.\n")

        if score >= 3:
            print(f"You scored {score} points out of 5! Well done!")
            
        elif score != 1:
            print(f"You scored {score} out of 5 points.... better luck next\
time!")

            if score == 1:
                print(f"You scored 1 out of 5 points... better luck next\
time!")

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

        replay = str(input('Do you want to play again? (Y / N): ')) # takes
        # the user input, Y or N, asks if they want to replay the game or not

        while replay.capitalize() != 'Y' or replay.capitalize() != 'N':
            # checks if they input anything other than Y or N
            if replay.capitalize() == 'Y' or replay.capitalize() == 'N':
                break # if their input == Y or N, then the loop breaks
            else:
                replay = str(input("Please enter either Y or N: "))
                # else the program asks the user to input Y or N again

            if replay.capitalize() == 'Y': # if the user input == Y, then the
                # quiz restarts
                continue

            elif replay.capitalize() == 'N':
                # else, if the input == N, the program finishes.
                break


# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Main Routine

print("\n⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆ 𝒦𝒾𝓌𝒾 𝒬𝓊𝒾𝓏 ⋆꙳•̩̩͙❅*̩̩͙‧͙\
‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
print()
print("╰┈➤  1. The quizes are only meant for children whose ages are from 5 - \
11 years\n\n╰┈➤  2. Each quiz will consist of atleast 5 questions\n\n╰┈➤  3. \
There are two quiz sets available and you have been given a specific one\n \
\tdepending on your age (5-7 or 8-11). If you are older but you just want \
\n\tsomething you can breeze through, or you're younger and you would\n\tjust \
like a challenge, pick the opposite age group.\n")
# Prints the Game Rules

name = input("‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾。Please enter your name: ") # Program asks for user input name

name = name_check(name)
# name_check function checks that the name is valid.
# Function will return the capitalized name once it confirms it is valid.
# This is what the function will return

age = age_check("°⋆.ೃ࿔*:･☁️. What's your age in years?: ")
# Takes age input and checks 
# that it is valid

valid_age = False
# Variable that helps the program determine whether the
# user's age is considered valid (True) or invalid (False). If it's
# invalid, it prints an error message and asks them to re-enter

quiz_a_age = False
# Helps the program decide which quiz to run

quiz_b_age = False
# (Same as above)

if age <= 7 and age >= 5:
    quiz_a_age = True
    valid_age = True
# If the user's age is less than or equal to 7 AND greater than or equal
# to 5, (5 - 7), they get Quiz A

if age > 7 and age <= 11:
    quiz_b_age = True
    valid_age = True
# If the user's age is greater than 7 AND less than
# or equal to 11 (7 - 11), they get Quiz B

while valid_age == False:
    print("\n🚨❗ ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ 🚨  Please enter an age from 5 - 11 years. \
⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ❗🚨")
    age = age_check("°⋆.ೃ࿔*:･☁️. What's your age in years?: ")
# If their age is anything out of the age range,
# they get asked to re-enter it.

    if age <= 7 and age >= 5:
        quiz_a_age = True
        valid_age = True
    # If the user's age is less than or equal to 7
    # AND greater than or equal to 5 (5 - 7), they get Quiz A
    
    if age > 7 and age <= 11:
        quiz_b_age = True
        valid_age = True
    # If the user's age is greater than 7 AND less
    # than or equal to 11 (7 - 11), they get Quiz B

if valid_age == True:
    print(f"\nHey there, {name}. Welcome to the Kiwi Quiz!\n\tLet's begin...\
    \n")  # Welcome Message

if quiz_a_age == True:
    quiz_a()
        
elif quiz_b_age == True:
    quiz_b()
