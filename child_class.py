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

class Abyssimian(Cat):
  pass

class Ragdoll(Cat):
  pass

class Birman(Cat):
  pass
        
lilly = Ragdoll("Lilly", 3)
sona = Abyssimian("Sona", 7)
butter = Birman("butter", 5)

print(lilly.description())
print(sona.speak("meow meow"))
print(butter.description())
print(butter.name)
print(type(butter))

# Lilly is very cute
# Sona says meow meow
# butter is very cute
# butter
# <class '__main__.Birman'>
