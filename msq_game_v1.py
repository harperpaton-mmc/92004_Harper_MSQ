# First interation of random number generator;
import random

# Checks that the user has entered a valid option based on a list
def yes_no_checker(question, valid_ans=('yes', 'no')):
    error = f"[Please enter a valid option from the following list: {valid_ans}!]"

    while True:

        # Gets user response and makes sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Checks to see if the user response is a word in the list
            if item == user_response:
                return item

            # Checks if the user response is the same as the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # prints error if user does not enter something that is valid
        print(error)
        print()


# Prints the instructions for the game
def instructions():
    print("""
    •••How to Play•••

    Welcome to the Level 1 Mechanical Science Quiz! 
    In this quiz, you are presented with a set number of questions to do with mechanical energy. 

    At the start, you can select the number of questions you would like to answer. If you wish, you can also view a list of formulas (for revision, we recommend trying to use the formula from memory).

    You will have to use a variety of scientific formulas to calculate the answers to the questions.

    When the quiz is completed, you can view your overall results and (if you wish) play again.

    •••Extra Tips•••

    Round all answers up to one decimal place.
    Don't include units in your answers!

    """)

# Checks for an integer above 0 or <enter>
def questions_checker(question):
   while True:
       # Checks that the user inputs an integer above or equal to 1 for the number of questions. If not, returns error.
       error = "[Please enter an integer above or equal to 1!]"

       try:
            response = int(input(question))

            # Checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

       except ValueError:
           print(error)

# Collects user answer (integer)
def int_check(question):
    while True:
        # Returns error message if user enters something other than an integer
        error = "[Please enter an integer!]"

        try:
            # Prompts user for the question's answer
            response = int(input(question))

            # Returns user answer so it can be stored
            return response

        except ValueError:
            print(error)

# Compares the user's answer to the correct answer and returns "correct" if they match or "incorrect" if they don't
def answer_compare(user, expected):

    if user == expected:
        answer_status = "correct"

    else:
        answer_status = "incorrect"

    return answer_status


# Initialising variables
question_type = ["kinetic energy", "gravitational energy"]
rounds_played = 0

# Main routine begins below

# Game title (start of program)
print("•••⁀➴ Mechanical Science Quiz ⚡•••"
      "\n────────────────────────────────────")
print()

# Asks the user if they want to see the instructions before playing
want_instructions = yes_no_checker("Would you like to view the instructions? ")
if want_instructions == "yes":
    instructions()

# Asks the user for the number of questions in the quiz
num_rounds = questions_checker("How many questions long do you want the quiz to be? ")

# Game loop starts here
# Code below generates the questions and stops generating them once the user has been asked the correct number of questions
while rounds_played < num_rounds:

    # Generates three random numbers 1-50 for the question
    random_1 = random.randint(1,50)
    random_2 = random.randint(1,50)
    random_3 = random.randint(1,50)

    # Chooses a type of question
    set_question = random.choice(question_type)

    # Generates a different question based on the question type
    if set_question == "kinetic energy":
        print(f"A {random_1}kg object is moving at a rate of {random_2}m/s")
        # Calculates the correct answer
        find_answer = f"{random_1 * (random_2 * random_2) * 0.5:.0f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(find_answer)
        # for testing
        print(find_answer)
        user_answer = int_check("What is the kinetic energy of the object? ")

    elif set_question == "gravitational energy":
        print(f"A {random_1}kg object sits {random_2}m off the ground")
        # Calculates the correct answer
        find_answer = f"{random_1 * random_2 * 10:.0f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(find_answer)
        print(find_answer)
        user_answer = int_check("What is the gravitational potential energy of the object? ")

    # Temporary fix for unresolved variables
    else:
        print("Program error")
        find_answer = "Error"
        correct_answer = int(find_answer)
        user_answer = "error"

    result = answer_compare(user_answer, correct_answer)

    if result == "correct":
        print("Correct!")
        rounds_played += 1

    elif result == "incorrect":
        print("Wrong!")
        rounds_played += 1
