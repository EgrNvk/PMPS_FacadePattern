class Barista:
    def grind_coffee(self):
        print("\tМелемо кавові зерна")

    def heat_water(self):
        print("\tНагріваємо воду")

    def brew_coffee(self):
        print("\tЗаварюємо каву")

    def add_sugar(self):
        print("\tДодаємо цукор")

    def make_coffee(self):
        print("Бариста починає готувати каву:")
        self.grind_coffee()
        self.heat_water()
        self.brew_coffee()
        self.add_sugar()
        print("Кава готова")


class Kitchen:
    def prepare_ingredients(self):
        print("\tПідготовлюємо інгредієнти")

    def bake_dessert(self):
        print("\tВипікаємо десерт")

    def decorate_dessert(self):
        print("\tПрикрашаємо десерт")

    def make_dessert(self):
        print("Кухня починає готувати десерт:")
        self.prepare_ingredients()
        self.bake_dessert()
        self.decorate_dessert()
        print("Десерт готовий")


class Cashier:
    def calculate_price(self):
        print("\tРозраховуємо суму замовлення")

    def print_receipt(self):
        print("\tДрукуємо чек")

    def accept_payment(self):
        print("\tПриймаємо оплату")

    def make_bill(self):
        print("Каса оформлює рахунок:")
        self.calculate_price()
        self.print_receipt()
        self.accept_payment()
        print("Оплату завершено")


class CoffeeShopFacade:
    def __init__(self):
        self.barista = Barista()
        self.kitchen = Kitchen()
        self.cashier = Cashier()

    def order_combo(self):
        print("Клієнт робить замовлення:")
        self.barista.make_coffee()
        self.kitchen.make_dessert()
        self.cashier.make_bill()
        print("Замовлення готове")


shop = CoffeeShopFacade()
shop.order_combo()