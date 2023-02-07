import random

upper_limit = input('Pease enter the upper limit :')

if upper_limit.isdigit():
    upper_limit = int(upper_limit)
    if upper_limit <=0 :
        print('Please make sure to inter a positive number')
        quit()

else:
    print('Please make sure to inter a valid number')
    quit()

random_guess = random.randint(0,upper_limit)
print('--random guess :', random_guess)

number_of_guesses = 0

while True:
    user_guess = input('Make a guess : ')
    number_of_guesses += 1

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_guess :
            # print('You have got it !')
            print('You hvae got it after ', number_of_guesses, ' guesses !')
            break
        else:
            if user_guess > random_guess :
                print('You are above the number !')
            else:
                print('You are below the number !')
    else:
        print('Please make sure to enter a valid number')

