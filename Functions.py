from datetime import datetime


# # Manual Approach
print(datetime.now())
print(datetime.now())
print(datetime.now())


# Define function and call it 
def show_time():
    print("This is the Current Date and Time: ")
    return datetime.now()

print(show_time())

def greet(name:str):
    return "Hello "+name
    
print(greet("Alice"))
print(greet("Ali"))


# Other way of mentioning Return types in functions Arrow means what we are Returning
# Its completely optional to define Return Type

def add(num1:float,num2:float)->float:
    return num1+num2

print(add(10.2,60.24))