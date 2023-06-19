import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper','scissors']

while True:
    user_input = input('Type Rock, Paper, or Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break
        
    if user_input not in options:
        print('Invalid input. Please try again.')
        continue
    
    random_number = random.randint(0, 2)
    # rock = 0 , paper = 1 , scissors = 2
    computer_pick = options[random_number]
    print('Computer picked: ' + computer_pick)
    
    
    if user_input == 'rock' and computer_pick == 'scissors':
        user_wins += 1
        print('You won!')
        
    
    elif user_input == 'paper' and computer_pick == 'rock':
        user_wins += 1
        print('You won!')
        
    
    elif user_input =='scissors' and computer_pick == 'paper':
        user_wins += 1
        print('You won!')
        
    elif user_input == computer_pick:
        print('Tie!')
        
    else:
        computer_wins += 1
        print('You lost!')    
    
          
print('You won ' + str(user_wins) + ' times.' )
print('The Computer won '+ str(computer_wins) +' times.')
print('Goodbye!')    