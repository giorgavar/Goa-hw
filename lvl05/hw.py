# 1. მომხმარებელს შემოაყვანინეთ შემდეგი ინფორმაციები: სახელი, გვარი, ასაკი, საცხოვრებელი ადგილი.
# 2. მომხმარბეელს შემოაყვანინეთ 2 string ინფორმაცია და შეასრულეთ კონკატინაცია.
# 3. მომხმარებელს შემოაყვანინეთ სხვადასხვა ტიპის მონაცემები და შეამოწმეთ მატი ტიპები. 

name = input("name ")
surname = input("surname ")
age = input("age ")
city = input("city ")

print(name, surname, age, city)

word1 = input("word1 ")
word2 = input("word2 ")

result = word1 + " " + word2
print(result)

user_str = input("input str ")
user_int = int(input("input int "))
user_float = float(input("input float "))

print(type(user_str))
print(type(user_int))
print(type(user_float))