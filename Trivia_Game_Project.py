#This is a beginner project. The goal is to have a set of questions that we ask the user,and keep track of the user's score.
#First step when making a project is to think about the steps. How would you make the project, and what should the code do?

#Step 1: create a set of questions to ask user
#Step 2: store answers to the questions
#Step 3: randomize order of questions
#Step 4: ask user to answer questions
#Step 5: calculate user score
#Step 6: display user score

# using a dictionary to create a set of questions to ask user and store correct answers
# a dictionary = a collection of {key:value} pairs. They are ordered and mutable, no duplicates allowed!
# to make a dictionary, you must give it a name, and inside curly brackets write the key and value separated by a colon.
#separate one key value pair form another using a comma
# Now I'm going to find some trivia questions and use a dictionary to pair the answers and the questions!

import random

trivia_questions = {'What is the largest mammal in the world?': 'Blue Whale',
                    'Who is the first President of the USA?': 'George Washington',
                    'Who painted the Mona Lisa?': 'Leonardo Da Vinci',
                    'Who is the king of the gods in Greek mythology?': 'Zeus',
                    'In what galaxy is our solar system located?': 'Milky Way',
                    'What is the name of the largest ocean on Earth?': "Pacific Ocean",
                    'In the story of Snow White, how many dwarfs are there?': '7',
                    'Which planet is known as the “Blue Planet”?': 'Earth',
                    'Who wrote the famous tragedy Romeo and Juliet?': 'William Shakespeare',
                    'How many elements are in the periodic table?': '118'}


#now I have completed steps 1 and 2! Yay! :)
#to randomize the questions, I will use import random. I have to it above the dictionary for it to work.
#now I made a function, and inside that function I took all of the keys (the actual questions) form my dictionary and put it in a list.
#then, I made a variable called question_list that stores the list of all of my keys
#now, since I want it to be random, I only want the user to be asked 5 questions each time so total_questions = 5
#made variable called score and set to 0 to keep track of score
#random.sample(question_list, total questions) will select 5 questions from the list. this new list will be stored as selected_questions
def trivia_game():
    while True:
        question_list = list(trivia_questions.keys())
        total_questions = 5
        selected_questions = random.sample(question_list, total_questions)
        score = 0
        selected_questions = random.sample(question_list, total_questions)

    #Hey! I'm back after a long break of working on other projects! 2/26/26
    #ok so now we want to loop through teh question a certain number of times, but we also need
    # know what question we are asking so we have to index them
    # I will use the .title method to capitalize the first letter in each word
    # I will also add the .strip method in order to make sure that if the user types their answer with a space, that ist not marked incorrect
        for idx, question in enumerate(selected_questions):
            print(f'{idx + 1}. {question}')
            user_answer = input('Your answer: ').title().strip()
            correct_answer = trivia_questions[question]

            if user_answer == correct_answer.title():
                print('Correct!\n')
                score = score + 1
            else:
                print('Incorrect!\n')
        print(f'Game over! Your score is: {score}/{total_questions}\n')
        play_again = input('Do you want to play again? Enter yes or no: ').lower().strip()
        if play_again == 'yes':
            continue
        else:
            print('Thanks for playing!')
            break
# finally compete on 2/26/26! I'm so proud! :)


trivia_game()
