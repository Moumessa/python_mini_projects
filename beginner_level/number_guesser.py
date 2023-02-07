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

while True:
    user_guess = input('Make a guess : ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_guess :
            print('You have got it !')
        else:
            print('You have got it wrong')
        break
    else:
        print('Please make sure to inter a valid number')
        continue

