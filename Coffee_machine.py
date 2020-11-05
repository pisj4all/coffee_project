ingredients={
    "water":400,
    "milk":540,
    "coffee beans":120,
    "disposible cups":9,
    "money":550
}

def buy():
    choice= int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if choice==1:
        ingredients['water']-=250
        ingredients['coffee beans']-=16
        ingredients['money']+=4
    elif choice==2:
        ingredients['water']-=350
        ingredients['milk']-=75
        ingredients['coffee beans']-=20
        ingredients['money']+=7
    elif choice==3:
        ingredients['water']-=200
        ingredients['milk']-=100
        ingredients['coffee beans']-=12
        ingredients['money']+=6

def fill():
    print("Write how many ml of water do you want to add:")
    ingredients['water']+=int(input())
    print("Write how many ml of milk do you want to add:")
    ingredients['milk']+=int(input())
    print("Write how many grams of coffee beans do you want to add:")
    ingredients['coffee beans']+=int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    ingredients['disposible cups']+=int(input())
    
def take():
    initial_money=ingredients['money']
    ingredients['money']-=initial_money
    print(f"I gave you {initial_money}$")

def ingredients_status():
    print(f'\nThe coffee machine has:')
    for k,v in ingredients.items():
        print(f'{v} of {k}')

    print('')


while True:
    ingredients_status()
    order = input("Write action (buy, fill, take, stop):")
    if order=="buy":
        buy()
    elif order=="fill":
        fill()
    elif order=="take":
        take()
    elif order=="stop":
        break
