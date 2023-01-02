# PetCat.py
class Pet:
    def __init__ (self, n=' ', c=' ', t=' ', a=0):
        self.name = n
        self.color = c
        self.type = t 
        self.age = a

    def setName (self, n ):
        self.name = n
    def getName (self):
        return self.name
    def setColor (self, c ):
        self.color = c
    def getColor (self):
        return self.age
    def setType (self, t ):
        self.type = t
    def getType (self):
        return self.type
    def setAge (self, a):
        self.age = a
    def getAge (self):
        return  "{0} years".format(self.age) 

    def __str__ (self):
        return "{0} is a {1} {2} aged {3} years.".format (self.name, self.color, self.type, self.age)


class Cat( Pet ):       # Cat is a child class, Pet is the parent class
    def __init__ (self, n=' ', c=' ', a=0):
        self.name = n
        self.color = c
        self.type = 'cat'
        self.age = a

    def setType (self, t):
        print ('{0} refuses to change type, it will always be a {1} in this life.'. format (self.name, self.type) )

    def setAge(self, a):
        if 1<= a <30:
            self.age = a

c = Cat('Sassy', 'white', 3)
print(c)        # Sassy is a white cat aged 3. (invokes the `__str__()` inherited from parent class `Pet`)

c.setAge(0.5)   # not in the range defined in the override `setAge()` method
c.getAge()      # 3 years. (age not changed means the override setter is working, also the inherited getAge() is working)

c.setType('dog')   # Sassy refuses to change type, it will always be a cat in this life. (the override setter is in action)

c.setName('Pussy')    # (inherited setter from Pet class)
print (c)            # Pussy is a white cat aged 3.