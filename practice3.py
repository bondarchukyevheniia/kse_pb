number = int(input("Число"))
if number%2==0:
  print("Парне")
else:
    print("не парне")

average = int(input(" Середній Бал"))
if average >= 90:
  print("Відмінник")
elif average >= 75:
  print("Молодець")
else:
  print("Старайся більше")

  for price in range(10,101,5):
  price2 = price*1.2
  print(f"ціна без пдв:{price}, з пдв:{price2}")

  i1 = int(input("число1"))
i2 = int(input("число2"))
i3 = int(input("число3"))
if i1>i2 and i1>i3:
  print(i1)
elif i2>i3 and i2>i1:
  print(i2)
elif i3>i2 and i3>i1:
  print(i3)

  money = 1000
month = 0
while money<=5000:
  money += 300
  month += 1
  print(money, month)

  year = int(input("високосний"))
if year%4==0 and not year%100 or year%400==0:
  print("високосний")
else:
  print("звичайний рік")

  for i in range(1, 21):
  if i%4==0:
    continue
  print(i)

  credit = 10000
payment = 1200
month = 0
while credit>0:
  credit = credit-payment
  credit = credit*1.02
  month +=1
  if credit>0:
    print(credit)

    total=0
while True:
   sum = float(input("введіть ваш місячний дохід або '0' для виходу"))
   if sum==0:
    break
   elif sum<0:
    print("дохід не може бути від'ємним")
    continue
   else:
    total = total+sum
    print("ваш дохід збережено", total)
    