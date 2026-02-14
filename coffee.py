menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def resources_enough(option):            
    if option == 'cappuccino' or option == "latte":
        if resources["water"] >= menu[option]['ingredients']['water'] and resources["milk"] >= menu[option]['ingredients']['milk'] and resources["coffee"] >= menu[option]['ingredients']['coffee']:
            return True
        
        else:
            return False
    
    elif option == "espresso":
        if resources["water"] >= menu[option]['ingredients']['water'] and resources["coffee"] >= menu[option]['ingredients']['coffee']:
            return True
        
        else:
            return False
        
def tell_what_lacks(option2):
        if option2 == "espresso":
            if resources["water"] < menu[option2]['ingredients']['water']:
                if resources["coffee"] < menu[option2]['ingredients']['coffee']:
                    print("Sorry, there isn't enough water and coffee")
            else:
                print("Sorry, there isn't enough water. ")
        else:
            if resources["water"] < menu[option2]['ingredients']['water']:
                if resources["coffee"] < menu[option2]['ingredients']['coffee']:
                    if resources["milk"] < menu[option2]['ingredients']['milk']:
                        print("Sorry, there isn't enough water and milk and coffee... ")
                    else:
                        print("Sorry, there isn't enough water and coffee")
                else:
                    print("Sorry, there isn't enough water. ")
               

while(True):
    choice = input("What would you like to order? A cappuccino, latte, or espresso? ").lower()

    if choice == 'report':
        print(f"Currently:\nWater = {resources['water']}")
        print(f"Milk = {resources['milk']}")
        print(f"Coffee = {resources['coffee']}")
        print(f"Money = ${money}")

    elif choice == 'cappuccino' or choice == 'latte' or choice == 'espresso':
        if not resources_enough(choice):
            tell_what_lacks(choice)
            break
        print(f"A {choice} costs ${menu[choice]['cost']}")
        q = int(input("Enter number of quarters: "))
        d = int(input("Enter number of dimes: "))
        n = int(input("Enter number of nickels: "))
        p = int(input("Enter number of pennies: "))

        given_money = (q*0.25) + (d*0.10) + (n*0.05) + (p*0.01)

        if given_money < menu[choice]['cost']:
            print("Sorry, the money is not enough. ")
            break

        else:
            change = given_money - menu[choice]['cost']
    
            print(f"Here is your {choice}, and your change of ${change:.2f}. Enjoy!")

            if choice == 'espresso':
                resources["coffee"] -= menu[choice]["ingredients"]["coffee"]
                resources["water"] -= menu[choice]["ingredients"]["water"]
            else:
                resources["coffee"] -= menu[choice]["ingredients"]["coffee"]
                resources["milk"] -= menu[choice]["ingredients"]["milk"]
                resources["water"] -= menu[choice]["ingredients"]["water"]

            money = money + menu[choice]['cost'] 
           

    else:
        print("Please enter valid option. ")