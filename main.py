MENU = {
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
profit = 0
def is_suffificent_resources(drink_ingredients):
    for item in drink_ingredients:
        if resources[item] > drink_ingredients[item]:
            return True
        else:
            print(f"Sorry not enough {item}")
            return False
        
def process_coins():
    qTotal = int(input("How many quarters?: ")) * .25
    dTotal = int(input("How many dimes?: ")) * .10
    nTotal = int(input("How many nickels?: ")) * .05
    pTotal = int(input("How many pennies?: ")) * .01
    total = qTotal + dTotal + nTotal + pTotal
    return total

def transaction_successful(coffee):
    total = process_coins()
    
    if total >= coffee["cost"]:
        difference = total - coffee["cost"]
        difference = round(difference, 2)
        print(f"{difference} in change has been refunded.")
        global profit
        profit += coffee["cost"]
        return True
    else: 
        print("Sorry not enough money. Money refunded")
        return False
    
def makeCoffee():
    for item in drinkIngredients:
        resources[item] -= drinkIngredients[item]
    print(f"Enjoy your {userInput}")

vending = True

while vending:
    userInput = input("What would you like? (espresso/latte/cappuccino):")
    if userInput == "off":
        vending = False
    elif userInput == "report":
        print(f"Milk: { resources['milk'] } ml")
        print(f"Water: { resources['water'] } ml")
        print(f"Coffee: { resources['coffee'] } g")
        print(f"Money: ${profit}")
    else:
        coffee = MENU[userInput]
        drinkIngredients = coffee["ingredients"]
        if is_suffificent_resources(drinkIngredients):
            if transaction_successful(coffee):
                makeCoffee()


    

