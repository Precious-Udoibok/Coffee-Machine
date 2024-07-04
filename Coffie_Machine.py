from resources import resources,MENU,profit
#TODO Process the Coins
#Ask the user to insert coins

coffee_milk = resources['milk']
coffee_water = resources['water']
coffee_available = resources['coffee']
orders = True
while orders:
    try:
        #Ask the user what type of coffe the will like.
        user_coffee = input('\nWhat would you like? (espresso/latte/cappuccino): ').lower()
        # TODO Print Report of the resources in the coffee machine
        if user_coffee == 'report':
            print(f'Water: {coffee_water}ml\nMilk: {coffee_milk}ml\nCoffee: {coffee_available}g\nMoney: ${round(profit,2)}')

        # TODO Check if the resources are sufficient for the coffee
        # if user enters any coffee check if the resources are sufficient to make the coffee
        elif user_coffee == 'latte' or user_coffee == 'cappuccino' or user_coffee == 'espresso':
            if coffee_water < MENU[user_coffee]['ingredients']['water']:
                print('Sorry the is not enough water')
            elif coffee_milk < MENU[user_coffee]['ingredients']['milk']:
                print('Sorry the is not enough milk')
            elif coffee_available < MENU[user_coffee]['ingredients']['coffee']:
                print('Sorry the is not enough coffee')
            else:
                print('Please Insert Coins')
                quarter = int(input('How many quarters?: '))
                penny = int(input('How many pennies?: '))
                Dime = int(input('How many dimes?: '))
                Nickel = int(input('How many nickels?: '))
                total = (quarter * 0.25) + (penny * 0.01) + (Dime * 0.10) + (Nickel * 0.05)
                print(total)
                change = total - MENU[user_coffee]['cost']
                if total < MENU[user_coffee]['cost']:
                    print('Not Enough Money, Money Refunded')
                else:
                    print(f'Here is your ${change}\nHere is your {user_coffee} coffee ☕️ Enjoy.')
                    coffee_milk -= MENU[user_coffee]['ingredients']['milk']
                    coffee_water -= MENU[user_coffee]['ingredients']['water']
                    coffee_available -= MENU[user_coffee]['ingredients']['coffee']
                    profit += MENU[user_coffee]['cost']

        elif user_coffee == 'off':
            orders = False
    except Exception:
        print('invalid Input')