# Checks that the user has entered a valid option based on a list
def yes_no_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

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

# Main routine begins below

testing_question = yes_no_checker("Input yes or no: ")
print(f"You entered: {testing_question}")