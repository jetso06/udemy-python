from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menuItem = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#while is_on = True:

def coffedrinks():
    global drink
    resource_sufficient = coffee_maker.is_resource_sufficient(drink)
    print(resource_sufficient)
    if resource_sufficient == True:
        payment_done = money_machine.make_payment(drink.cost)
        coffee_maker.make_coffee(drink)


is_on = True
while is_on == True:
    choice = input(f"What would you like? ({menu.get_items()}):")
    drink = menu.find_drink(choice)

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink == None:
        continue
    else:
        coffedrinks()
