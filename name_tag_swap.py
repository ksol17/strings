def swap_characters(username):
    if len(username) > 1:
        return username[-1] + username[1:-1] + username[0]
    return username

while True:
    username_input = input("Enter your username to see the magic swap: ")
    swapped_username = swap_characters(username_input)

    print(f"✨ Ta-da! Your magical username is: {swapped_username} ✨")

    continue_input = input("Want to try another username? (yes/no): ").lower()
    if continue_input != 'yes':
        break 