import random
wordbank = ['apple', 'cookie','pizza','burger','pasta','ramen','sushi','orange','banana','cake','popsicle','strawberry']
def word_guessing_game():
    print('Welcome to word guessing game! You have a maximum of 10 guesses.')
    word = random.choice(wordbank).lower().strip()
    chosen_word = ['_'] * len(word)
    attempts = 10
    while attempts > 0:
        print('\nMake sure to only guess one letter at a time per attempt!')
        print('\nCurrent word:' + " ".join(chosen_word))
        user_guess = input('Enter your guess: ').lower().strip()
        if user_guess in word:
            for i in range(len(chosen_word)):
                if word [i] == user_guess:
                    chosen_word[i] = user_guess
            print('Good guess!')
        else:
            # The longer way to write this (aka what I'm used to, is attempts =attempts-1)
            attempts -=1
            print(f'Try again! Attempts left: {attempts}')
        if '_' not in chosen_word:
            print(f'\nWell done! You\'ve guessed the word: {word}')
            break
        if attempts == 0 and '_' in chosen_word:
            print(f'\nYou\'ve run out of attempts. The word was {word}')






word_guessing_game()