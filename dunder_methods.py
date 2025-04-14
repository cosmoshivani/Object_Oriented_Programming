#dunder - double underscore

class Cat():
  
  def __init__(self, color, sound):
    self.color = color
    self.sound = sound

  def __str__(self):
    return f"{self.color} cat says {self.sound}"

lilly = Cat("brown", "mew")
simone = Cat("cream", "meow")

print(lilly)
print(simone)

# >> brown cat says mew
# >> cream cat says meow
