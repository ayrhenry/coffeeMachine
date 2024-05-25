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

MONEY = 10
vending = True

def InsertedCoins():
    q = int(input("How many quarters?"))
    d = int(input("How many dimes?"))
    n = int(input("How many nickels?"))
    p = int(input("How many pennies?"))

    return [q, d, n, p]

def makeCoffee(drink):
    drinkName = drink
    iHateEspressosWTF = drink != "espresso"
    drink = MENU[drink]
    drinkResources = drink["ingredients"]
    
    resources["water"] = resources["water"] - drinkResources["water"]
    resources["coffee"] = resources["coffee"] - drinkResources["coffee"]
    
    #this doesnt make sense to me. my guess is that the id of "espresso is not equal to the id of drink="espresso" but that also doesn't make sense because why wouldn't it?
    if iHateEspressosWTF == True:
        resources["milk"] = resources["milk"] - drinkResources["milk"]

    return print(f"Here's your {drinkName}. Enjoy!")


def transaction(total, drink):
    drinkCost = drink
    global MONEY
    print(total)
    if total >= drinkCost:
        #makeCoffee(drink)
        difference = total - drinkCost
        MONEY += drinkCost

        print(f"Here's your change: {round(difference, 2)}")
        return True
    else:
        print("Insufficent funds, money refunded")
        return False
    

def coinProcessor(coins):
    quarter = .25
    nickel = .05
    dime = .10
    penny = .01

    qAmount = quarter * coins[0]
    dAmount = dime * coins[1]
    nAmount = nickel * coins[2]
    pAmount = penny * coins[3]

    total = qAmount + nAmount + dAmount + pAmount

    return total


def sufficientResources(drink):
        

    def resourceCalc(ingredients):
    #print(f"Water: {ingredients[0]}ml \n Milk: {ingredients[1]}ml \n Coffee: {ingredients[2]}g \n Money: ${MONEY}\n")
    #mlk = str(resources["milk"])
    #print(resources["milk"])
    #print(ingredients["milk"])
    #print("Resrx:" + mlk ) 
    
    #Need to skip oner milk condition for espresso only. I'm not sure how x.x
        if drink != "espresso":
            if ingredients["milk"] <= resources["milk"]:

                if  ingredients["water"] <= resources["water"]:
                    if ingredients["coffee"] <= resources["coffee"]:
                            return True
                    else:
                        print("Sorry not enough coffee")
                        return False
                else:
                    print("Sorry not enough water")
                    return False
            else:
                print("Sorry not enough milk")
                return False

    if drink == "cappuccino":
        cappuccino = MENU["cappuccino"]
        ingredients = cappuccino["ingredients"]
        return resourceCalc(ingredients)
        
        
    elif drink == "espresso":
        espresso = MENU["espresso"]
        ingredients = espresso["ingredients"]
        return resourceCalc(ingredients)
        

    elif drink == "latte":
        latte = MENU["latte"]
        ingredients = latte["ingredients"]
        return resourceCalc(ingredients)
        
        








while vending:
    coffee = input("What would you like?")
    if coffee == "report":
        print(f"Water: {resources['water']}ml \n Milk: {resources['milk']}ml \n Coffee: {resources['coffee']}g \n Money: ${MONEY}\n")
        coffee = input("What would you like?")
              
    if coffee == "off":
        vending = False
        break

    #Making dictionary values accessible via declaration
    drinkDict = MENU[coffee]
    
    #Checking for sufficient resources
    suffRes = sufficientResources(coffee)
    if suffRes == True:

        #Inserting Coins
        userMoney = InsertedCoins()

        #Calculating coin total with coinProcessor
        total = coinProcessor(userMoney)

        #Process transaction
        complete = transaction(total, drinkDict["cost"])

        #if statement to determine if the drink should be made and dispensed by makeCoffee()
        if complete is True:
            makeCoffee(coffee)
    


    

