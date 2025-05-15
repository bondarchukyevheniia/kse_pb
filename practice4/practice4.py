nums = [3, 7, 2, 9, 5]
total = 0
i = 0
for num in nums:
  total += num
  i += 1
total = total/i
print("середнє значення:",total)

nums = [4, 7, 2, 4, 8, 9, 2, 10, 3, 8]
unique_nums1 = set(nums)
unique_nums2 = list(unique_nums1)
num = unique_nums2.sort(reverse=True)
emp = []
for i in unique_nums2:
  if i%2==0:
    emp.append(i)
print(emp)

grades = [
    [90, 85, 88],
    [75, 80, 79],
    [95, 92, 96],
    [88, 85, 84]
]
average = []
for i in grades:
  value = (sum(i)/len(i))
  average.append(value)
val = max(average)
for u, grade in enumerate(average):
  if grade==val:
    break
print(u)
print(grade)
print(grades[2])

prices = {
    "apple": 12,
    "banana": 8,
    "milk": 25,
    "bread": 20
}
suma = sum(prices.values())
print(suma)

people = {
    "Anna": "Kyiv",
    "Bohdan": "Lviv",
    "Oksana": "Kyiv",
    "Dmytro": "Odesa"
}
new_dict = {}
unique_cities =list(set(people.values()))
for i in unique_cities:
  new_dict[i]=[]
name = people.keys()
for key,value in people.items():
  new_dict[value].append(key)
print(new_dict)