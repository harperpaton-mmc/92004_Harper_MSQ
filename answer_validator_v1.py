# First interation of random number generator;
import random

# Checks to see if the user's answer was correct
def answer_checker(question):
    while True:
        # Compares user answer to correct answer
        error = "[Please enter an integer!]"
        try:

            response = int(input(question))

            if response == answer:
                return "correct"

            else:
                return "incorrect"

        except ValueError:
            print(error)


# Initialising variables
question_type = ["kinetic energy", "gravitational energy"]

# Main routine begins below

# Generates three random numbers 1-50 for the question
random_1 = random.randint(1,50)
random_2 = random.randint(1,50)
random_3 = random.randint(1,50)

# Chooses a type of question
question = random.choice(question_type)

# Generates a different question based on the question type
if question == "kinetic energy":
    print(f"A {random_1}kg object is moving at a rate of {random_2}m/s")
    result = random_1 * (random_2 * random_2) * 0.5
    answer = f"{result:.0f}"
    # for testing
    print(answer)
    user_answer = answer_checker("What is the kinetic energy of the object? ")
    if user_answer == "correct":
        print("Right!")

    elif user_answer == "incorrect":
        print("Wrong!")


elif question == "gravitational energy":
    print(f"A {random_1}kg object sits {random_2}m off the ground")
    result = random_1 * random_2 * 10
    answer = f"{result:.0f}"
    # for testing
    print(answer)
    user_answer = answer_checker("What is the gravitational potential energy of the object? ")
    if user_answer == "correct":
        print("Right!")

    elif user_answer == "incorrect":
        print("Wrong!")