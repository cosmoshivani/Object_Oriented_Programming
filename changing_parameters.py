class Cat():
    
    species = "Abyssinian"
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        
lilly = Cat("Lilly", 3)
sona = Cat("Sona", 7)

#updating parameter values

Cat.species = "Ragdoll"
lilly.age = 7
        
print(lilly.age)
print(sona.name)
print(Cat.species)

# >> 7
# >> Sona
# >> Ragdoll
