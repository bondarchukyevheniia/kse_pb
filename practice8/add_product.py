def add_product(inventory, name, price, quantity):
    product = input("який продукт?")
    if name in inventory:
        inventory[name][quantity]+=quantity
    else:
        price = int(input("яка ціна?"))
        inventory[product] = {"price":price, "quantity":quantity}
    return inventory 
