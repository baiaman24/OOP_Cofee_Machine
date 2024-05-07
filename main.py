from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
drink_menu = Menu()
money = MoneyMachine()
should_work = True
while should_work:
    options = drink_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "report":
        coffee.report()
        money.report()
    elif choice == "off":
        should_work =False
    else:
        chosen_drink = drink_menu.find_drink(choice)
        if coffee.is_resource_sufficient(chosen_drink):
            if money.make_payment(chosen_drink.cost):
                coffee.make_coffee(chosen_drink)

