import random
# Exploring dictonaries
# Testing saving user scores/statistics to a dictionary
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

# Intialising variables
snack_list = ["coffee", "tea", "cookies"]
offer_history = []
answer_history = []
total_coffee = 0
total_tea = 0
total_cookies = 0
yes_coffee = 0
yes_tea = 0
yes_cookies = 0
loops_run = 0

# Loop for testing begins below

while loops_run < 10:
    snack_offer = random.choice(snack_list)
    want_snack = yes_no_checker(f"Do you want some {snack_offer}? ")

    # Stores what the type of snack was offered + user answer
    offer_item = snack_offer
    answer_item = f"{snack_offer} = {want_snack}"

    # Adding items to the list
    offer_history.append(offer_item)
    answer_history.append(answer_item)

    # Adds one to the toal loops
    loops_run += 1

# End of question loop

# Counting statistics
# Amount the snack was offered
total_coffee = offer_history.count("coffee")
total_tea = offer_history.count("tea")
total_cookies = offer_history.count("cookies")

# Amount player accepted
yes_coffee = answer_history.count("coffee = yes")
yes_tea = answer_history.count("tea = yes")
yes_cookies = answer_history.count("cookies = yes")

# Dictionary
testdict = dict(coffee = f"{yes_coffee}/{total_coffee}", tea = f"{yes_tea}/{total_tea}", cookies = f"{yes_cookies}/{total_cookies}")
print(testdict)
