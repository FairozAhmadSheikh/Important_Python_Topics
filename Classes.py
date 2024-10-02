# Classes Simplify the process of creating Objects  For code that has to be duplicated a lot
# Method is a function inside a class for example start is a method in Car Object
# Self Refers to the Instance e.g in Volvo is an instance ,using self means reffering to Volvo

class Car:
    def __init__(self,name:str,color:str,horsepower:int) -> None:
        self.name=name
        self.color=color
        self.horsepower=horsepower
        
    def start(self):
       return f"{self.name} Engine is Starting "
    
    def get_info(self):
        return(f"{self.name} with {self.horsepower} horsepower") 
    

Volvo:Car=Car("Volvo","Blue",600) # Instance
print(Volvo.color)
print(Volvo.horsepower)


BMW=Car("BMW","Green",40) # New Instance
print(BMW.name)
print(BMW.color)
print(BMW.horsepower)

# Calling Methods
print(BMW.start())
print(Volvo.start())
print(Volvo.get_info())


print(Volvo)