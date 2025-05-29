from data import inventory, transacticccons 
while True:
    action = int(input("Дія"))
    if action == 1:
        product = input("який продукт?")
        quant = input("яка кількість")
        inventory = add_product(inventory,product,quant)
    elif action == 2:
        pass
    elif action == 3:
        pass
    elif action == 0:
        break