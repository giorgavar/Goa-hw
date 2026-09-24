def greet(name):
    return f"Hello, {name}!"
    print(greet("World"))
  
print(greet("World"))

def double(x):
    return x * 5

print(double(5))

def checkodd(num):
    if num % 2 != 0:
        return True
    else:
        return False
    
print(checkodd(7))
print(checkodd(4))

def BMI(weight, height):
    bmi = weight / (height * height)
    return bmi

print(BMI(70, 1.75))
print(BMI(85, 1.8))