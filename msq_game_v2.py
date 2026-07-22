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
How to Play
────────────────────────────────────
Welcome to the Level 1 Mechanical Science Quiz! 
In this quiz, you are presented with a set number of questions to do with mechanical energy. 

At the start, you can select the number of questions you would like to answer. If you wish, you can also view a list of formulas (for revision, we recommend trying to use the formula from memory).

You will have to use a variety of scientific formulas to calculate the answers to the questions.

When the quiz is completed, you can view your overall results and (if you wish) play again.

Extra Tips
────────────────────────────────────
Round all answers up to one decimal place.
Don't include units in your answers!
────────────────────────────────────

    """)

# Prints the necessary for formulas
def formulas():
    print("""
Relevant Formulas
────────────────────────────────────
Energy: 
Gravitational Energy = Mass * Gravity * Height
Kinetic Energy = ½ Mass * Velocity²

Work and Power:
Force = Mass * Gravity
Work = Force * Distance
Power = Work / Time

Electricity: 
Voltage = Current * Resistance
Power (in a circuit) = Voltage * Current

Heat:
Heat Energy (during an increase in temperature) = Mass * Specific Heat Capacity * Change in Temperature
Heat Energy (during a change in state) = Mass * Latent Heat 

Values:
Gravity = 10
Specific Heat Capacity of Water = 4200J/kgºC
Latent Heat of Fusion (water) = 334000J/kg
Latent heat of Vapourisation (water) = 2260000J/kg
────────────────────────────────────

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
question_type = ["kinetic energy", "gravitational energy", "work", "power", "voltage", "circuit power", "heat increase", "heat change"]
rounds_played = 0

# Main routine begins below
# Game title (start of program)
print("⁀➴ Mechanical Science Quiz ⚡"
      "\n────────────────────────────────────")
print()

# Questions/Setting before game loop begins are below
# Asks the user if they want to see the instructions before playing
want_instructions = yes_no_checker("Would you like to view the instructions? ")
if want_instructions == "yes":
    instructions()

# Asks the user if they want to see the formulas before playing
want_formulas = yes_no_checker("Would you like to view the formulas? ")
if want_formulas == "yes":
    formulas()

# Asks the user for the number of questions in the quiz
num_rounds = questions_checker("Select a number of questions: ")

# Game loop starts here
print()

# Code below generates the questions and stops generating them once the user has been asked the correct number of questions
while rounds_played < num_rounds:

    # Generates a heading for each "round" (question)
    round_heading = f"Question {rounds_played + 1} / {num_rounds}"
    print(round_heading)
    print("────────────────────────────────────")

    # Generates three random numbers 1-50 for the question
    random_1 = random.randint(1,50)
    random_2 = random.randint(1,50)
    random_3 = random.randint(1,50)

    # Chooses a type of question
    set_question = random.choice(question_type)

    # Generates a different question based on the question type (I'll probably be putting this in a function
    # Kinetic Energy
    if set_question == "kinetic energy":
        print(f"A {random_1}kg object is moving at a rate of {random_2}m/s.")
        # Calculates the correct answer
        find_answer = f"{random_1 * (random_2 * random_2) * 0.5:.1f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(float(find_answer))
        # for testing
        print(correct_answer)
        user_answer = int_check("What is the kinetic energy of the object? ")

    # Gravitational Energy
    elif set_question == "gravitational energy":
        print(f"A {random_1}kg object sits {random_2}m off the ground.")
        # Calculates the correct answer
        find_answer = f"{random_1 * 10 * random_2:.1f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(float(find_answer))
        print(correct_answer)
        user_answer = int_check("What is the gravitational potential energy of the object? ")

    # Work
    elif set_question == "work":
        print(f"A {random_1}kg object is lifted {random_2}m off the ground.")
        # Calculates the correct answer
        find_answer = f"{random_1 * 10 * random_2:.1f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(float(find_answer))
        print(correct_answer)
        user_answer = int_check("How much work was done to move the object? ")

    # Power
    elif set_question == "power":
        print(f"A crane lifts a {random_1}kg object {random_2}m off the ground in {random_3}s.")
        # Calculates the correct answer
        find_answer = f"{(random_1 * 10 * random_2) / random_3:.1f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(float(find_answer))
        print(correct_answer)
        user_answer = int_check("What is the power of the crane? ")

    # Voltage
    elif set_question == "voltage":
        print(f"A circuit has {random_1}Ω of resistance and a current of {random_2}A.")
        # Calculates the correct answer
        find_answer = f"{random_1 * random_2:.1f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(float(find_answer))
        print(correct_answer)
        user_answer = int_check("What is the voltage supplied to the circuit? ")

    # Power (in a circuit)
    elif set_question == "circuit power":
        print(f"A circuit is being powered by a {random_1}V battery and has a current of {random_2}A.")
        # Calculates the correct answer
        find_answer = f"{random_1 * random_2:.1f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(float(find_answer))
        print(correct_answer)
        user_answer = int_check("What is the power of the circuit? ")

    # Heat energy (temperature increase)
    elif set_question == "heat increase":
        print(f"{random_1}L of water undergoes a change in temperature from an initial temperature of {random_2}ºC to {random_3}ºC.")
        # Calculates the correct answer
        find_answer = f"{random_1 * 4200 * (random_2 - random_3):.1f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(float(find_answer))
        print(correct_answer)
        user_answer = int_check("How much heat energy is used/lost to change the temperature? If heat is lost, write the answer as a negative number.  ")

    # Heat energy (state change)
    elif set_question == "heat change":
        # Used to decide if the liquid in the question is being frozen (meaning the user will have to use the latent heat of fusion) or vapourised (meaning the user will have to use the latent heat of vapourisation)
        state_changes = ["cooled down until it freezes into ice", "heated up until it vapourises into steam"]
        change_type = random.choice(state_changes)
        print(f"{random_1}L of water is {change_type}.")
        # Calculates the correct answer (two different formulas)
        if change_type == "cooled down until it freezes into ice":
            find_answer = f"{random_1 * 334000:.1f}"
        else:
            find_answer = f"{random_1 * 2260000:.1f}"
        # Converts the correct answer into an integer so it can be compared to the user's answer
        correct_answer = int(float(find_answer))
        print(correct_answer)
        user_answer = int_check("How much heat energy is used to change the state of the water?  ")

    # Temporary fix for unresolved variable issue
    else:
        print("Program error")
        find_answer = "Error"
        correct_answer = int(find_answer)
        user_answer = "error"

    # Finds whether the user's answer is right or wrong
    result = answer_compare(user_answer, correct_answer)

    if result == "correct":
        print("Correct!")
        rounds_played += 1

    elif result == "incorrect":
        print("Wrong!")
        rounds_played += 1

    print()

# End of loop
# Statistics Area
# Optional play again
# Game end
