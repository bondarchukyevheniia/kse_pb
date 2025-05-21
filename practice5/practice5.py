def calculave_vat(price):
  pdv = 0.2
  result = price * pdv
  return result
calculave_vat(555)

def usd_to_uah(amount):
  dollar = 39.5
  grivna = dollar * amount
  return grivna
usd_to_uah(90)

def monthly_salary(hours,rate):
  salary = hours * rate
  return salary
monthly_salary(10,0.6)

def apply_discount(price,discount):
  sale = price * (100-discount)/100
  return sale
apply_discount(22,0.3)

def profit(revenue,cost,tax):
  profit = (revenue - cost) * (1-tax)
  return profit
profit(10000,5000,0.18)

def weighted_average_price(prices, quantities):
  prices = [1,2,3,4]
  quantities = [4,3,2,1]
  total = 0
  for index,num in enumerate(prices):
    total+= prices[index]*quantities[index]
    znam = sum(quantities)
    average = total/znam
  return average
weighted_average_price([1,2,3,4],[4,3,2,1])

def calculate_wacc(equity, debt, cost_of_equity, cost_of_debt, tax_rate):
  wacc = (equity/(equity+debt))*cost_of_equity+(debt/(equity+debt))*cost_of_debt*(1-tax_rate)
  return wacc
calculate_wacc(5,5,5,5,5)

def monthly_payment(present_value, rate, months):
  anuit = (present_value*rate)/(1-1/(1+rate)**months)
  return anuit
monthly_payment(4,6,8)

def adjust_for_inflation(price):
  dot = {}
  min_price = min(price)
  max_price = max(price)
  average_price = sum(price)/len(price)
  total = 0
  for num in price:
    if num<average_price:
      total+=1
  dot["мінімальне"] = min_price
  dot["максимальне"] = max_price
  dot["середнє"] = average_price
  dot["кількість"] = total
  return dot
adjust_for_inflation([3,6,9,5])