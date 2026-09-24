#1
numbers = [2, 4, 6, 8, 10]

total_sum = 0

for num in numbers:
    total_sum += num

average = total_sum / len(numbers)

print("total:", total_sum)
print("answer:", average)


#2
secret_number = 7

while True:
    user_input = int(input("num: "))

    if user_input == secret_number:
        print("right num")
        break
    else:
        print("wrong num")

#3
while True:
    number = int(input("input num: "))

    if number % 2 != 0:
        print("its odd retry")
        continue
    else:
        print("its even")
        break
