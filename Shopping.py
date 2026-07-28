class Item:
    def __init__(self, name, brand, price):
        self.__name = name
        self.__brand = brand
        self.__price = price

    def show_traits(self):
        print("The item is a {} which is branded as {} and it costs {}.".format(self.__name, self.__brand, self.__price))
    
    def change_price(self,new_price):
        self.__price = new_price

i = Item("TV","Samsung",9000)
i.show_traits()

print("Trying to change the price from outside.")
i.__price=800
print("Testing...")
i.show_traits()
print("It didn't work")

print("Now trying setter method.")
i.change_price(800)
print("Testing...")
i.show_traits()
print("It worked")