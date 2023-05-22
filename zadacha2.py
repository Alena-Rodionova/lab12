class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название Ресторана {self.restaurant_name},  кухня:  {self.cuisine_type} итальянская.")

    def open_restaurant(self):
        print("Ресторан сейчас открыт.")

class IceCreamStand(Restaurant):
    def __init__(self, IceCreamStand_name, flavors, mesto, raspisanie):
        self.IceCreamStand_name = IceCreamStand_name
        self.flavors = flavors
        self.mesto = mesto
        self.raspisanie = raspisanie

    def describe_IceCreamStand(self):
        print(f"Название ларька с мороженным: {self.IceCreamStand_name}")

    def location_IceCreamStand(self):
        print(f"Место расположения: {self.mesto}улица Стремянная дом 11")

    def raspisanie_IceCreamStand(self):
        print(f"Время работы: {self.raspisanie} 10:00-19:00")

    def IceCream(self):
        A=['Клубничное','Банановое','Пломбир','Баблгам','Крем Брюле']
        print(f"Вкусы:{self.flavors} {A}")
        t=int(input('1)Удалить вкус 2)Добавить вкус  Выберите действие: '))
        if t==1:
            u=input('Введите вкус: ')
            A.remove(u)
        elif t==2:
            u = input('Введите вкус: ')
            A.append(u)
        print(f"Обновленные вкусы:{self.flavors} {A}")
    def By_IceCream(self):
        A=['Клубничное','Банановое','Пломбир','Баблгам','Крем Брюле']
        v = input('Какой вкус вы хотите: ')
        if v in A:
            print('Да, такой вкус есть')
        else: print('Такого вкуса нет, приходите в другой раз')
newIceCreamStand = IceCreamStand("Маленький Единорог"," "," "," ")
print(newIceCreamStand.IceCreamStand_name)
print(newIceCreamStand.flavors)
print(newIceCreamStand.location_IceCreamStand)
print(newIceCreamStand.raspisanie_IceCreamStand)

newIceCreamStand.describe_IceCreamStand()
newIceCreamStand.IceCream()
newIceCreamStand.By_IceCream()
newIceCreamStand.location_IceCreamStand()
newIceCreamStand.raspisanie_IceCreamStand()