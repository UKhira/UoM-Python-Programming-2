import WalkingStick
import Binoculers

class warrior :
    
    def __init__(self, age, name) :
        self.age = age
        self.name = name
        self.is_mobie = True
        self.stick = WalkingStick()
    
    
    def walk(self):
        while self.is_mobie:
            print('Walking')
            
    
    def lose_stick(self):
        self.stick = None
        self.is_mobie = False 
        
        
class SuperWarrior(warrior):            # in () this access the superclass(base class,parent class) "warrior" and inherit its values
    
    def __init__(self, age, name):
        super().__init__(age, name)
        self.binoculers = Binoculers
        
                                        # SuperWarrior and NormalWarrior are Sub Classes AKA Child Classes
    def fight(self):
        pass
    
    def walk(self):
        while self.is_mobie:                # in here the value "walk" method. is_mobile attribute (which inherits from superclass) has overridden
            print("Walk with no rest")
        
class NormalWarrior(warrior):
    
    def rest(self, rest_time = None):
        if rest_time is not None:
            print("Rest only for {}".format(rest_time))
        else:
            print("Rest a lot")
    

# creating an instance
sup_warrior1 = SuperWarrior(15,"warrior1")
sup_warrior1.walk()

Warrior = NormalWarrior(13, "warrior2")
Warrior.rest()
Warrior.rest(10)        

# Override - Same name, same parameters, different implementations