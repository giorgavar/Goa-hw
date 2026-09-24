numbers = [3, 7, 2, 9, 4]

for n in numbers:
    print(n)

total = 0
for n in numbers:
    total += n
print(total)


numbers = [3, 6, 8, 1, 4, 9]

count_even = 0
for n in numbers:
    if n % 2 == 0:
        count_even += 1
print(count_even)


numbers = [5, 2, 9, 1, 7]

min_val = numbers[0]
max_val = numbers[0]

for n in numbers:
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n

print(min_val)
print(max_val)


numbers = [1, 4, 7, 8, 9, 12]

for n in numbers:
    if n % 2 != 0:
        print(n)


total = 0
while True:
    num = int(input())
    if num == 0:
        break
    total += num
print(total)


while True:
    num = int(input())
    if num < 0:
        break


while True:
    num = int(input())
    if num % 5 == 0:
        break


attempts = 0
while True:
    num = int(input())
    attempts += 1
    if num % 2 == 0:
        break
print(attempts)


while True:
    num = int(input())
    if num % 2 != 0:
        break


while True:
    num = int(input())
    if num < 0:
        continue
    if num == 0:
        break
    print(num)


while True:
    num = int(input())
    if num < 0:
        continue
    if num == 100:
        break
    print(num)
