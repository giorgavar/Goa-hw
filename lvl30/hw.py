# 2) კომენტარებით ახსენით თუ რას აკეთებს .upper(); .lower(); .capitalize(); .find() ფუნქციები.

# 3) მომხმარებელს შემოატანინეთ წინადადება და დაბეჭდეთ იგი პატარა ასოებით.

# 4) მომხმარებელს შემოატანინეთ ელფოსტის მისამართი და გადაამოწმეთ შეიცავს თუ არა '@' სიმბოლოს, შედეგი კი დაბეჭდეთ დიდი ასოებით.

# 5) მომხმარებელს შემოატანინეთ წიგნის დასახელება და შედეგი დაბეჭდეთ სათაურის სტილში.

# 6) მომხმარებელს შემოატანინეთ წინადადება და სიმბოლო. თქვენი დავალებაა დაითვალოთ რამდენჯერ გვხვდება ეს სიმბოლო წინადადებაში.

# 7) მომხმარებელს შემოატანინეთ სიტყვა და შეამოწმეთ, არის თუ არა იგი დიდი ასოებით, თუ კი — დაბეჭდე "სიტყვა უკვე დიდია!", თუ არა — გადააქციე და დაბეჭდე.

#.upper() ყველა ასოს აქცევს დიდად





text = "Hello World"


print(text.upper())

#.lower() ყველა ასოს აქცევს პატარად
print(text.lower())

#.capitalize() პირველ ასოს აქცევს დიდად, დანარჩენს პატარად
print(text.capitalize())

#.find() ეძებს სიმბოლოს ან სიტყვას და აბრუნებს მის ინდექსს თუ ვერ იპოვა აბრუნებ-1-ს
print(text.find("W"))



sentence = input("any sentance: ")
print(sentence.lower())




email = input("email: ")

if "@" in email:
    print("EMAIL CONTAINS @")
else:
    print("EMAIL DOES NOT CONTAIN @")



book_title = input("book cover: ")
print(book_title.title())



sentence = input("any sentance: ")
symbol = input("any symbol: ")

count = sentence.count(symbol)
print(f"symbol '{symbol}'  {count} times in the sentance")



word = input("any word: ")

if word.isupper():
    print("the word is already uppercase")
else:
    print(word.upper())