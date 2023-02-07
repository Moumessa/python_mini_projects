print('--------- A SIMPLE QUIZ GAME -----------')

playing = input('Do you want to play ?')

if playing != 'yes':
    quit()

print("Okey ! Let's play !")

answer = input('What does CPU stand for ?')
if answer == 'Central Unit Processing':
    print('Correct')
else:
    print('Incorrect !')

answer = input('What does GPU stand for ?')
if answer == 'Graphical Unit Processing':
    print('Correct')
else:
    print('Incorrect !')

answer = input('What does RAM stand for ?')
if answer == 'Random Access Memory':
    print('Correct')
else:
    print('Incorrect !')