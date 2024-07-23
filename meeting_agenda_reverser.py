def reverse_agenda(agenda_string):
    # 'gym, breakfast, work'
    agenda_items = agenda_string.split(', ')
    reversed_agenda = agenda_items[::-1]
    return ', '.join(reverse_agenda)

while True:
    user_agenda = input("Enter your meeting agenda items separated by commans: ")
    reversed_order = reverse_agenda(user_agenda)

    print(f"Reversed agenda order: {reversed_order}")

    continue_input = input("Would you like to reverse another agenda? (yes/no): ").lower()
    if continue_input != 'yes':
        break