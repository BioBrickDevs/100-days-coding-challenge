from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mm = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()
while True:
    choice = input(f"What would you like {menu.get_items()}?").lower()
    if choice in menu.get_items().split("/"):
        if(maker.is_resource_sufficient(menu.find_drink(choice))):
            if mm.make_payment(20):
                maker.make_coffee(menu.find_drink(choice))


    if choice == "off":
        break

    if choice == "report":
        maker.report()
        mm.report()

item = menu.find_drink("latte")

