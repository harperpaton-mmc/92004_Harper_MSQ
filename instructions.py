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

# Main routine begins below

want_instructions = yes_no_checker("Would you like to view the instructions? ")
if want_instructions == "yes":
    instructions()