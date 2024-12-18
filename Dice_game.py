''' 
A simple game that rolls a dice and outputs the result 

random module used to set the the values of num1 and num2 
to random numbers in the list 

Time module used to wait for 3 seconds before showing the 
result

'''

import random
import time


dice_numbers=[1,2,3,4,5,6]
score=0
numberof_try=0

while True:
    user_input=int(input("Press 1 to roll dice (press 2 to quit):"))
    if user_input==2:
        print("Thanks for playing!")
        break
    
    dice1=random.choice(dice_numbers)
    dice2=random.choice(dice_numbers)
    print("dice is rolling....")
    time.sleep(3)
    print(f"Dice rolled, your result : ({dice1},{dice2})")

    if dice1==dice2:
        score+=1
        numberof_try+=1
        print("\n you won!\n")
    else:
     numberof_try+=1
     print("\n Try your luck again...\n")

print("\n Your total score :",score)
print("Number Of Tries  :",numberof_try)






    


      