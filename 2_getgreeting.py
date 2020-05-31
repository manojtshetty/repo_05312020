class Animal:
        def __init__(self, isMammal,isCarniverous):
            self.isMammal = isMammal
            self.isCarniverous = isCarniverous
        def getIsMammal(self):
            return self.isMammal
        def getIsCarniverous(self):
            return self.isCarniverous
        def getGreeting(self): 
            pass

class Dog(Animal):
    def getGreeting(self):
        if self.getIsMammal():
            Mam_check = 'is a mammal'
        else:
            Mam_check = 'is not a mammal'
        if self.getIsCarniverous():
            Carn_check = 'is carniverous'
        else:
            Carn_check = 'is not carniverous'
        
        return 'A dog says \'ruff\', '+Carn_check+', and '+Mam_check+'.'
		
class Cow(Animal):
    def getGreeting(self):
        if self.getIsMammal():
            Mam_check = 'is a mammal'
        else:
            Mam_check = 'is not a mammal'
        if self.getIsCarniverous():
            Carn_check = 'is carniverous'
        else:
            Carn_check = 'is not carniverous'
        
        return 'A Cow says \'moo\', '+Carn_check+', and '+Mam_check+'.'
		
class Duck(Animal):
    def getGreeting(self):
        if self.getIsMammal():
            Mam_check = 'is a mammal'
        else:
            Mam_check = 'is not a mammal'
        if self.getIsCarniverous():
            Carn_check = 'is carniverous'
        else:
            Carn_check = 'is not carniverous'
        
        return 'A Duck says  \'quack\', '+Carn_check+', and '+Mam_check+'.'
		
dog1 = Dog(True,True)
cow1 = Cow(True,False)
duck1 = Duck(False,False)

print (dog1.getGreeting())
print (cow1.getGreeting())
print (duck1.getGreeting())