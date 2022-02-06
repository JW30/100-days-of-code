from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine:

    def __init__(self):
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def run(self):
        while True:
            choice = input(f"What would you like? ({self.menu.get_items()}): ")
            if choice == "off":
                break
            elif choice == "report":
                self.coffee_maker.report()
                self.money_machine.report()
            else:
                drink = self.menu.find_drink(choice)
                if drink:
                    if self.coffee_maker.is_resource_sufficient(drink):
                        if self.money_machine.make_payment(drink.cost):
                            self.coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    cm = CoffeeMachine()
    cm.run()
