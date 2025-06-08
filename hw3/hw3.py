#1.1
numbers = [1,2,3,4,5,6,7,8,9]
total = sum(numbers)
print(total)

#1.2
numbers = [35,98,12,108,56,1]
minimum = min(numbers)
print(minimum)

#1.3
numbers = [1,2,3,4,5,6,7,8,9]
numbers[::-1]

#1.4
numbers = [0,1,2,3,4,5,6,7,8,9,10]
neparni = []
for i in numbers:
  if i%2!=0:
    neparni.append(i)
print(neparni)

#1.5
numbers = [1,2,3,4,5,6,7,8,9]
num = int(input("Number:"))
empty = []
for i in numbers:
  mnoz = i*num
  empty.append(mnoz)
print(empty)

#2.1
numbers = [44,55,29,98,2,34,7,99,27,18]
num = int(input("Number:"))
empty = []
for i in numbers:
  if i>num:
    empty.append(i)
print(empty)

#2.2
numbers = [-22,33,-10,20,40,-8,-18,19]
empty = []
for i in numbers:
  if i>0:
    empty.append(i)
for num in empty:
  average = sum(empty)/len(empty)
print(average)

#2.3
numbers = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Number:"))
empty = []
for i in numbers:
  if i>num:
    empty.append(i)
max = len(empty)
print(max)

#2.4
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
num = int(input("Number:"))
empty = []
for i in numbers:
  if i%2==0:
    empty.append(i)
suma = sum(empty)
print(suma)

#2.5
numbers = [1,2,3,4,5,6,7,8,9,10]
empty = []
for i in numbers:
  square = i**2
  empty.append(square)
print(empty)

#2.6
numbers = [-1,1,-2,2,-3,3,-4,4,-5,5]
dodatni = []
for i in numbers:
  if i>0:
    dodatni.append(i)
print(dodatni)

#2.7
words = ["unable", "able", "unhelpful", "helpful"]
empty = []
for i in words:
  if "un" in i:
    empty.append(i)
print(empty)

#2.8
numbers = [1,2,3,4,5,6,7,8,9,10]
n = int(input("Number:"))
empty = []
for i in numbers[0:n]:
  empty.append(i)
suma = sum(empty)
print(suma)

#2.9
numbers = ["level","book","refer","pen"]
polindrom = []
for i in numbers:
  if i[::1]==i[::-1]:
    polindrom.append(i)
print(polindrom)

#2.10
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
empty = []
num = int(input("Number:"))
for i in numbers:
  if i%num == 0:
    empty.append(i)
print(empty)

#3.1
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
x = int(input("x:"))
y = int(input("y:"))
empty = []
for i in numbers:
  if i%x==0 and i%y!=0:
    empty.append(i)
print(empty)

#3.2
numbers =[[1,2,3],[4,5,6],[7,8,9]]
empty = []
for i in numbers:
  for item in i:
    empty.append(item)
print(empty)

#3.3
# isupper() - цей метод знайшла за допомогою пошуку в Гуглі
word = ["H","o","M","e"]
big_letter = []
for i in word:
  if i.isupper():
    big_letter.append(i)
print(big_letter)

#3.4
numbers = [18,44,44,15,17,98,56,56,2,4,4]
empty = []
nums = list(numbers)
spadannya = nums.sort(reverse=True)
for i in nums:
  empty.append(i)
print(empty)

#3.5
numbers = [1,2,3,4,5,6,7,8,9]
nums = [10,11,12,13,14,15,16,17,18]
empty = []
for i in numbers:
  if i%2==0:
    empty.append(i)
for j in nums:
  if j%2==0:
    empty.append(j)
print(empty)

#3.6
numbers = {"student":12, "student2":10, "student3":11, "student":9}
suma = []
for i in numbers:
  if "student" in numbers.keys():
    summa = sum(numbers.values())
print(summa)

#3.7
numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
  numbers[i%2==0] = "parne"
print(numbers)

#3.8
words = ["cat", "dog", "hello", "good", "start"]
empty = []
x = int(input("x:"))
for i in words:
  if len(i)>x:
    empty.append(i)
print(len(empty))

#3.9
numbers = [1,3,5,7,9]
nums = [2,4,6,8]
empty = []
for i in numbers:

#3.10
numbers = [1,2,3,4,5,6,7,8,9]
empty = []
x = int(input("x:"))
y = int(input("y:"))
for i in numbers:
  if i>x:
    mnoz = i*y
    empty.append(mnoz)
print(empty)