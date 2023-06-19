import random

top_of_range = input('Enter a number ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please enter a number greater than 0')
        quit()
        
else:
    print('Please enter a number')
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses+=1
    user_guess = input('Guess a number between 0 and ' + str(top_of_range) + ': ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number')
        continue
    
    if user_guess == random_number:
        print('You guessed it right!')
        break
    elif user_guess > random_number:
        print('Too high!')
    else:
        print('Too low!')    
        
print('You guessed it in ' + str(guesses) + ' tries!')                                                                                                                                      