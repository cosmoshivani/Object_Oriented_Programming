class Cat():
    
    species = "Abyssinian"
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age

    #new instances
    def description(self):
        return f"{self.name} is very cute"
        
    def speak(self, sound):
        return f"{self.name} says {sound}"
        
lilly = Cat("Lilly", 3)
sona = Cat("Sona", 7)

print(lilly.description())
print(sona.speak("meow meow"))


# >> Lilly is very cute
# >> Sona says meow meow
