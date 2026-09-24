# def login():
#     ask_username = str(input('Username: '))
#     ask_password = str(input('Password: '))

# login()


def login():
    
    correct_username = "erekle"
    correct_password = "Python123"

    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    
    if username == correct_username and password == correct_password:
        print("✅ Login successful! Welcome,", username)
    else:
        print("❌ Invalid username or password.")



login()










