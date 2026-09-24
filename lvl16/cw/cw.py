# for loop ეს არის განმეორებადი ციკლი რომელიც აკეთებს მოქმედებას რამდენჯერმე.
# indentation არის შეწევა (tab ან 4 space) რომელიც Python-ში გამოიყენება კოდის ბლოკების გამოსაყოფად.

for number in range(0, 67):
    print(number)

for number in range(4, 98, 2):
    print(number)

for number in range(12, 87):
    print(number)

name = 'gio'

for i in range(0, 10, 1):
    for letter in name:
        print(letter)

word = input("any word: ")
for letter in word:
    print(letter)

num = int(input("any number: "))
for i in range(num):
    print(i)





