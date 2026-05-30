#I want this calculator to explain what the pythagorean theorem is, ask for user input, and calculate
# made on 1/28/26
import math
def pythagorean_theorem_calculator():
  print ('Welcome user! This calculator will help you calculate the pythagorean theorem')
  print('What is your name? ')
  bot_name = 'Chatbot'
  username = input('Enter your name: ')
  print (f"Hello {username}! My name is {bot_name}")
  print('Let\'s calculate the pythagorean theorem!')
  print('Please enter numbers only.')
  while True:
    try:
      side_a = float(input(f'Enter side a value'))
      side_b = float(input(f'Enter side b value'))
      hypotenuse = math.sqrt(side_a**2 + side_b**2)
      print (f'The hypotenuse is {hypotenuse}')
    except ValueError:
      print("That's not a valid number. Please try again!")
    print('Do you want to calculate again?')
    user_choice = input('Enter yes or no: ').lower()
    if user_choice == 'yes':
        continue
    elif user_choice == 'no':
        print('Do you want to learn about the pythagorean theorem?')
        learn_choice = input('Enter yes or no: ').lower()
        if learn_choice == 'yes':
            print('a Pythagorean theorem is the relationship between the three sides of a right triangle. ')
            print('It was named after the Greek philosopher Pythagoras, born around 570 BC.')
            print(f'Good bye {username}!')
            break
        else:
            print('Ok!')
            print(f'Good bye {username}!')
            break
    else:
        print(f'Good bye {username}!')
        break


pythagorean_theorem_calculator()