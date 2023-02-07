import random

user_score = 0
computer_score = 0

choices = ['rock', 'paper', 'scissors']

while True:
    user_response = input('Type Rock/Paper/Scissors or Q to quit :').lower()

    if user_response not in choices :
        continue

    if user_response == 'q':
        break

    random_number = random.randint(0,2)

    random_choice = random.choice(choices)
