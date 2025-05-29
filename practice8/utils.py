def is_valid_price(value):
    if value<0:
        pric= False
    else:
        pric= True
    return pric
def is_valid_quantity(value):
    if value>0:
        quant= True
    else:
        quant= False
    return quant
def format_currency(amount):
    form ="%.2f" %amount
    return form + "грн"
