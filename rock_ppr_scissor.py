'''
A simple game of rock paper scissor 

using random module for computer to make a choice

using if else statement to check user input and computer choice
and displaying the result.

'''

import random


options=("Rock","Paper","Scissors")
score=0
print("Choose from --->",options)
while True:

    user_input=input("Enter your move (press q to quit):").capitalize()
    comp_input=random.choice(options)

    if(user_input=='Q'):
        print("Your score =",score)
        break
    if(user_input==comp_input):
        print(f'Oponent : {comp_input} You : {user_input}')
        print("Its a Draw")

    elif(user_input=='Rock' and comp_input=='Scissors'):
        print(f'Oponent : {comp_input} You : {user_input}')
        print("You Win!")
        score+=1

    elif(user_input=='Rock' and comp_input=='Paper'):
        print(f'Oponent : {comp_input} You : {user_input}')
        print("You loose!")
        score-=1

    elif(user_input=='Paper' and comp_input=='Rock'):
        print(f'Oponent : {comp_input} You : {user_input}')
        print("You Win!")
        score+=1

    elif(user_input=='Paper' and comp_input=='Scissors'):
        print(f'Oponent : {comp_input} You : {user_input}')
        print("Loose!")
        score-=1

    elif(user_input=='Scissors' and comp_input=='Paper'):
        print(f'Oponent : {comp_input} You : {user_input}')
        print("You Win!")
        score+=1
    
    elif(user_input=='Scissors' and comp_input=='Rock'):
        print(f'Oponent : {comp_input} You : {user_input}')
        print("You loose!")
        score-=1

    


