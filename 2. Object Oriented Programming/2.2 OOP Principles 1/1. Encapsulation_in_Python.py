class warrior:
    
    def __init__(self,name):
        #instance attributes
        self.name = name
        self._age = 0                #Private by convention  (attribute with an underscore means its private variable,
                                    # mean it can be accessed only inside of its class)
        
    # Using property decorator - getter function
    @property
    def age(self):
        return self._age                 # getter
    
    @age.setter 
    def age(self,age):
        if age > 0:
            self._age = age             
        else:
            print("Age should be greater than Zero")        # setter
            

    
# creating an instance
warrior = warrior("warrior1")
print(warrior.name)

warrior.age = -5
# Age should be greater than Zero
print(warrior.age)
# 0

warrior.age = 15
print(warrior.age)
# 15