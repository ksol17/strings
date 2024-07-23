def repeat_message(message, times):
    return '-'.join([message] * times)

while True:
    user_message = input("Enter the message you want to repeat: ")
    repeat_count = int(input("How many times would you like to repeat it? "))

    repeated_message = repeat_message(user_message, repeat_count)

    print(f"Repeated message: {repeated_message}")

    continue_input = input("Would you like to create another repeated message? (yes/no): ").lower()
    if continue_input != 'yes':
        break