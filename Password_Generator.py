# I'm gonna make a random password generator! I'm planning on starting this today and maybe finishing sometime next week
#Ok so just like the trivia game project I wanna plan this project out.
# ask user what length password should be
# ask user about uppercase letters,
# ask user about special characters
# ask user about digits

# create all available characters based on user preferences
# randomly pick character up to user preferred length
# ensure we have at least 1 of each character type based on user preferences
# ensure length is valid according to preferences

import random
import string


def generate_password():
    print('Hello user 🙂, and welcome to random password generator! Please enter your preferences below.\n')
    while True:
        try:
            length = int(input('Enter the length of the password\n  '))
            if length<4:
                print('Please enter a valid length of 4 or more characters')
                continue
            break
        except ValueError:
            print('Invalid input! Please enter a whole number')
    include_special = str(input('Do you want to include special characters? Enter yes or no.\n   ')).strip().lower()
    include_digit = str(input('Do you want to include digits? Enter yes or no.\n   ')).strip().lower()
    include_uppercase = str(input('Do you want to include uppercase characters? Enter yes or no.\n  ')).strip().lower()

# now I'm going to use something i've never used before. I'm going to get the ascii lowercase letters
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == 'yes' else ""
    digits = string.digits if include_digit == "yes" else ""
    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digit == "yes":
        required_characters.append(random.choice(digits))
    remaining_length = length - len(required_characters)
    password = required_characters
    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)
    random.shuffle(password)
    final_password = ''.join(password)
    print(f'Your final password is {final_password}!')







generate_password()
