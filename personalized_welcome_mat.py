def create_welcome_message(name):
    line_lenght = 10
    centered_name = name.center(line_lenght, '*')
    return f"Welcome {centered_name} Welcome"

while True:
    user_name = input("Please enter your name for a personalized welcome message: ")
    if user_name.isalpha():
        welcome_message = create_welcome_message(user_name)
        print(welcome_message)
    else:
        print("Invalid name. Please enter alphabetic characters only.")

    continue_input = input("Would you like to create another welcome message? (yes/no): ").lower()
    if continue_input != 'yes':
        break