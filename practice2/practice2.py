age = 18
temperature = 36.6
name = "name"
is_it_dog = False
empty = None
day = "Wednesday"
page = 15

a = 30
b = 31
c = a
a = b
b = c
print(a)
print(b)

x = 3
y = 9
print(2*x+3*y)
print(x**2+2*x*y+y**2)
print(2/8*x-13/7*y)
print(y**(4*x-2*y)**1/2)
print(x%y)
print(y/x**2)
print(x>y)
print(x**2!=y)

name = "borscht"
price = 111
ng = f"{name} дорівнює {price} гривень"
print(ng)

x1 = 1
x2 = 2
x3 = 3
x4 = 4
c = ((x1>x3)or (x2>x4)and not(x2!=x3)or (x1==x4))
print(c)

height = int(input("Напишіть тут Ваш зріст в метрах"))
weight = int(input("Напишіть тут Вашу вагу в кг"))
bmi = weight/(height**2)
print(f"При вазі {weight} кг і рості {height} метрів Ваш BMI складає {bmi}")

r1 = 30
p1 = 3.14*r1**2
print(p1)
r2 = 36.3
p2 = 3.14*r2**2
print(p2)
p11 = 100
print(p11)
p22 = p2*p11/p1
print(p22)
diff = p22-p11
print(diff)
