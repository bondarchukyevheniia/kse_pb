b = "Hello, Python World!"
print(b)

a = int(input(""))
b = int(input(""))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

line1 = "домашнє"
line2 = "завдання2"
line12 = line1+line2
count = len(line12)
print(f"{line1} {line2}")
print(count)

number = int(input(""))
if number%2==0:
  print("парне")
else:
  print("не парне")

for i in range(1,11):
  print(i)

number = int(input(""))
if number>0:
  print("позитивний")
elif number<0:
  print("негативний")
else: 
  number==0
  print("нуль")

for i in range(0,11,2):
  print(i)

n = int(input(""))
total=0
for n in range(1,n+1):
  total+=n
print(total)

for i in range(10,0,-1):
  print(i)

for i in range(1,11):
  if i==5:
    continue
  elif i==7:
    break
  print(i)

