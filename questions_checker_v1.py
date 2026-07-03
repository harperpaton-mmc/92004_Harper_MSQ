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

# Main routine begins below

questions_number = questions_checker("How many questions would you like to answer? ")
print(f"You selected: {questions_number} question(s)!")