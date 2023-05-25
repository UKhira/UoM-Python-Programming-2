class Warrior:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.is_mobile = True
       
        
    # def walk(self):
    #     while self.is_mobile:
    #         print("Walking")

class SuperWarrior(Warrior):
    
    def walk(self):
        print("Can walk without a rest")
        
class NormalWarrior(Warrior):
    
    def walk(self):
        print('Need a rest while walking')
        
def check_walking_style(obj):
    obj.walk()
    
sup_warrior = SuperWarrior("warrior1", 20)
warrior = NormalWarrior("warrior2", 18)

check_walking_style(sup_warrior)
# Can walk without a rest
check_walking_style(warrior)
# Meed rest while walking
        

    
