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


print(Volvo)  # This just gives us information about where the object is located to make it usefull for non-programmer we use dunder methods 


# Fixing Goes from here new Class and object
class Gaadi:
    def __init__(self,name:str,horsepower:str) -> None:
        self.name=name,
        self.horsepower=horsepower
    
    # Dunder method  string output
    def __str__(self) :
        return f'{self.name} {self.horsepower} hp'

    
    
    
Tavera:Gaadi=Gaadi("Cheverolet",600)
bmw:Gaadi=Gaadi("BMW",606)

print(Tavera)
