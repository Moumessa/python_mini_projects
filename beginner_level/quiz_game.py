print('--------- A SIMPLE QUIZ GAME -----------')

playing = input('Do you want to play ?')

if playing != 'yes':
    quit()

print("Okey ! Let's play !")

score = 0
answer = input('What does CPU stand for ?')
if answer == 'Central Unit Processing':
    print('Correct')
    score+=1
else:
    print('Incorrect !')

answer = input('What does GPU stand for ?')
if answer == 'Graphical Unit Processing':
    print('Correct')
    score+=1
else:
    print('Incorrect !')

answer = input('What does RAM stand for ?')
if answer == 'Random Access Memory':
    print('Correct')
    score+=1
else:
    print('Incorrect !')


print('You got', score, 'correct answers !')