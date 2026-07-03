# First interation of random number generator;
import random

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

# Main routine begins below

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

elif result == "incorrect":
    print("Wrong!")
