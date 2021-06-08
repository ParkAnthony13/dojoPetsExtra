class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 10
        self.energy = 100
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.sound)
        return self
    def status(self):
        print(self.health)
        print(self.energy)
        return self

class Demon(Pet):
    def __init__(self,name,type,tricks, sound="growl"):
        super().__init__(name,type,tricks, sound)
        self.health = 10000
        self.energy = 10000