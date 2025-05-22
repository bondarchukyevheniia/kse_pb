import geometry
print(geometry.rectangle_area(4,6))
import converter
print(converter.uah_to_usd(1000,39.5))
import taxes
print(taxes.calculate_income_tax(15000)+taxes.calculate_vat(15000))
import math

print(math.sqrt(121),math.sin(3.14/2),math.floor(7.8),math.ceil(7.8))
import random
kub1 = random.randint(1, 6)
kub2 = random.randint(1, 6)
sum = kub1+kub2
print(kub1,kub2,sum)
import datetime
birthday = input("рррр-мм-дд")
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
today = datetime.date.today()
days_lived  = (today-birthday_date.date()).days
print(f"Ви прожили вже {days_lived} днів")