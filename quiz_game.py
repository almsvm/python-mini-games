print('Welcome to my computer quiz!')

playing = input('Do you want to play? (y/n): ').lower()

if playing != 'y':
    quit()
    
print("Ok. Let's play!")
score = 0

answer = input('What does CPU stand for? ').lower()
if answer == 'central processing unit':
    print('That is correct!')
    score+=1
else:
    print('That is incorrect!')

answer = input('What does GPU stand for? ').lower()    
if answer == 'graphics processing unit':
    print('That is correct!')
    score+=1
else:
    print('That is incorrect!')

answer = input('What does RAM stand for? ').lower()    
if answer == 'random acces memory':
    print('That is correct!')
    score+=1
else:
    print('That is incorrect!')

answer = input('What does PSU stand for? ').lower()    
if answer == 'power supply':
    print('That is correct!')
    score+=1
else:
    print('That is incorrect!')
    
print(f'You scored {score} questions correct!')
print(f'You got {score/4*100}%!')
print('Thanks for playing!')
    
