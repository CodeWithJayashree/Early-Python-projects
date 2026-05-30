# DAY 4 OF LEARNING THE BASICS OF CODING

bot_name: str = 'Chatbot.Luna'
print(f'Hello! I\'m {bot_name}! How can I assist you today?')

print(f'{bot_name}:Please include apostrophe\'s in responses when grammatically appropriate.')

while True:
    user_input: str = input('You: ').lower()

    if user_input in ['hi', 'hello', 'hello there', 'hello there!', 'hi!', 'hello!', 'hey', 'hey!', 'what\'s up', 'sup',
                      'hey there', 'hey there!', 'hello how are you', 'hi how are you', 'how are you', 'how r u']:
        print(f'{bot_name}: Hi there! How can I help you?')


    elif user_input in ['how are you', 'how are you?', 'how\'s it going', 'how\'s it going?', 'how are u', 'how are u?',
                        'hru', 'hru?']:
        print(f'{bot_name}: I\'m doing great 😊! Now, what can I do for you today?')

    elif user_input in ['math', 'calculator', 'help me with math', 'math problem']:
        print(f'{bot_name}: Of course! What operation would you like to perform? 🧮')


    elif user_input in ['+', 'add', 'help me add', 'i need to add these 2 numbers', 'find the sum', 'add these numbers',
                        'add the following', 'can you help me add']:
        print(f'{bot_name}: Sure! Let\'s do some addition. Please enter two numbers.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The sum is {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: Oops! That\'s not a valid number. Try again!')


    elif user_input in ['-', 'subtract', 'help me subtract', 'i need to subtract these 2 numbers',
                        'find the difference', 'minus', 'subtract these numbers', 'subtract the following',
                        'can you help me subtract']:
        print(f'{bot_name}: Sure! Let\'s do some subtraction. Please enter two numbers.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The difference is {num1 - num2}')
        except ValueError:
            print(f'{bot_name}: Oops! That\'s not a valid number. Try again!')


    elif user_input in ['*', 'multiply', 'times', 'help me multiply', 'i need to multiply these 2 numbers',
                        'find the product', 'multiply these numbers', 'multiply the following',
                        'can you help me multiply']:
        print(f'{bot_name}: Sure! Let\'s do some multiplication. Please enter two numbers.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The product is {num1 * num2}')
        except ValueError:
            print(f'{bot_name}: Oops! That\'s not a valid number. Try again!')


    elif user_input in ['/', 'divide', 'help me divide', 'i need to divide these 2 numbers', 'find the quotient',
                        'divide these numbers', 'divide the following', 'can you help me divide']:
        print(f'{bot_name}: Sure! Let\'s do some division. Please enter two numbers.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            if num2 == 0:
                print(f'{bot_name}: Cannot divide by zero!')
            else:
                print(f'{bot_name}: The quotient is {num1 / num2}')
        except ValueError:
            print(f'{bot_name}: Oops! That\'s not a valid number. Try again!')


    elif user_input in ['exponent', 'power', 'square root', 'cube root', 'perfect square', 'perfect cube', 'geometry',
                        'sequence', 'series', 'function', 'graph', 'coordinate plane', 'diagram', 'tan', 'tangent',
                        'cos', 'cosine', 'sin', 'sine', 'circumference', 'diameter', 'chord', 'hypotenuse', 'angle']:
        print(f'{bot_name}: Sorry user! I can only perform the 4 basic operations.😅')


    elif user_input in ['i\'m feeling sad', 'i\'m sad', 'i\'m feeling down', 'i\'m upset', 'today was the worst',
                        'i hated today', 'today sucks', 'i\'m sick', 'i hate being sick', 'being sick is the worst!']:
        print(f'{bot_name}: I\'m so sorry to hear that. I hope you feel better soon!')


    elif user_input in ['i\'m bored', 'i\'m super bored', 'what to do when you\'re bored?',
                        'can you help me, i\'m so bored rn']:
        print(
            f'{bot_name}: Fair enough 😂! Here are some things you can do for entertainment: Go on a walk, go on a bike ride, watch TV, bake, crochet, knit, sew, paint, solve a jigsaw puzzle, clean your room, take a nap, or read a book!')


    elif user_input in ['i\'m angry', 'i\'m so mad rn', 'i\'m so mad right now', "ugh", 'what to do when i\'m angry']:
        print(
            f'{bot_name}: That\'s okay. Your feelings matter, and I\'m glad you told me. Here are some ways you can let off steam: Scream into or punch a pillow, talk to a friend, take a few deep breaths, meditate, go on a walk, listen to music, or you can even journal your thoughts!')


    elif user_input in ['thanks', 'thank you so much!', 'thanks!', 'thx', 'thx!', 'tsym!', 'tysm']:
        print(f'{bot_name}: You\'re very welcome!😊')


    elif user_input in ['you are amazing', 'you\'re amazing', 'you\'re incredible', 'you\'re awesome',
                        'you\'re amazing!']:
        print(f'{bot_name}: Thank you! I\'m glad I could help. 😊')


    elif user_input in ['i\'m sorry!', 'i\'m so sorry!', 'i\'m sorry', 'i\'m so sorry', 'sorry', 'sorry!']:
        print(f"{bot_name}: No worries 🙂. Now, what can I do for you?")

    elif user_input in ['bye', 'see you', 'goodbye']:
        print(f'{bot_name}: Goodbye! Have a great day! :)')
        break

    else:
        print(f'{bot_name}: I\'m sorry, I don\'t understand. Please try again!')