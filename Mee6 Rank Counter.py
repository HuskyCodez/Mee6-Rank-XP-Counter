import random
from datetime import timedelta

#1 msg = 15 to 25xp
#1 msg interval is 1 min

while True:
    x = int(input("How Many XP to desired level: "))
    xp = random.randrange(15, 25)
    time = x/xp
    mamount = round(time)
    c = str(timedelta(minutes=mamount))[:-3]
    print('_______________')
    print('\nXP chosen: ' + f'{xp}')
    print('Messages to level up: ' + f'{mamount}')
    print('Approximate time until desired level (Hours and Minutes): ' + f'{c}\n')
    print('It would take you ' + f'{mamount}'+ ' messages to get ' + f'{x}' + ' xp.')
    print('_______________\n')

#feel free to change the code to your liking!#