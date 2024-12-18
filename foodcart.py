foodstall={"pizza"     :10.50,
           "popcorn"   :14.00,
           "popsticle" :13.33,
           "drink"     :9.23
           }

def displayMenue(foodstall):
    print("\n-------Welcome to My FoodCart------")
    for key,value in foodstall.items():
        print(f'{key:<10} : ${value:.2f}')

    print("-------------------------------------\n")


displayMenue(foodstall)


bill=0.00
while True:
    user_input=input("Please select from menue (press q to quit) :").lower()

    if user_input=="q":
        print("Thank you for coming...")
        break

    elif user_input=="pizza":
        bill +=foodstall.get("pizza")
        print(f'Total : ${bill}')

    elif user_input=="popcorn":
        bill +=foodstall.get("popcorn")
        print(f'Total : ${bill}')

    elif user_input=="popsticle":
        bill +=foodstall.get("popsticle")
        print(f'Total : ${bill}')

    elif user_input=="drink":
        bill +=foodstall.get("drink")
        print(f'Total : ${bill}')

print("******** BILL *********\n")
print(f'Total : ${bill}\n')
print("***********************")
