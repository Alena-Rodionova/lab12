class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название Ресторана {self.restaurant_name},  кухня:  {self.cuisine_type} итальянская.")

    def open_restaurant(self):
        print("Ресторан сейчас открыт.")

class IceCreamStand(Restaurant):
    def __init__(self, IceCreamStand_name, flavors):
        self.IceCreamStand_name = IceCreamStand_name
        self.flavors = flavors

    def describe_IceCreamStand(self):
        print(f"Название ларька с мороженным: {self.IceCreamStand_name}")

    def IceCream(self):
        A=['Шоколадное ','Клубничное','Банановое','Пломбир','Баблгам','Крем Брюле']
        print(f"Вкусы:{self.flavors} {A}")


newIceCreamStand = IceCreamStand("Маленький Единорог"," ")
print(newIceCreamStand.IceCreamStand_name)
print(newIceCreamStand.flavors)

newIceCreamStand.describe_IceCreamStand()
newIceCreamStand.IceCream()
