numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

for i in numbers:
    if i % 2 != 0:
        numbers.remove(i)
print(numbers)

numbers.insert(0, 20)
print(numbers)
numbers.sort()
print(numbers)

