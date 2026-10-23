# 1) ახსენით კომენტარის სახით რა არის input და output2) მომხმარებელს შემოატანინეთ შემდეგი მნიშვნელობები name, surname,     age, height და დაბეჭდეთ ისინი

# 3) მომხმარებელს შემოატანინეთ შემდეგი მნიშვნელობები favorite_car, favorite_color და დაბეჭდეთ მსგავსად:

#    Favorite car: {favorite_car}
#    Favorite color: {favorite_color}

# 4) მოიძიეთ ინფორმაცია data converter - ების შესახებ და თითოეულზე გააკეთეთ 2-2 მაგალითი

# 5) მოიძიეთ ინფორმაცია type() ფუნქციაზე, ახსენით რას აკეთებს ის და გააკეთეთ 2 მაგლითი

# 6) მომხმარებელს შემოატანინეთ 3 რიცხვი, გამოითვალეთ ამ რიცხვების საშუალო არითმეტიკული და დაბეჭდეთ საბოლოო შედეგი

name = input("name ")
surname = input("surname ")
age = input("age ")
height = input("height ")

print(name, surname, age, height)

favorite_car = input("favorite car  ")
favorite_color = input("favorite color ")

print(f"Favorite car: {favorite_car}")
print(f"Favorite color: {favorite_color}")

x = int("25")
y = int(3.14)

a = str(15)
b = str(49.99)

num = 100
print(type(num))

text = "Hello World"
print(type(text))

num1 = float(input("1"))
num2 = float(input("2"))
num3 = float(input("3"))

average = (num1 + num2 + num3) / 3
print(average)