from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
menu = Menu()
item = menu.get_items()
while is_on:
    choice = input(f"What type drinks do you want to drink?({item}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



