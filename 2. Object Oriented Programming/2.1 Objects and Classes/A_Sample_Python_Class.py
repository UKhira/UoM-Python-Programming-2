#   Objects/Classes are Things that have interaction with each other. to identify a class,
# Class is a noun, and it has interaction with other objects

class Monster:
    #class attributes,  attribute means state,characteristics of objects such as color,size,...
    color = "black"         #'color' attribute, 'black' value
    
    #constructor
    def __init__(self, age, name):
        #instance attributes,  means each objects in monster class has different values for age, name attributes
        self.age = age          # 'self' is a method that use to refer current object
        self.name = name
        
        #private attribute by convention
        self._is_innocent = None            #private attributes are defined using a leading underscore "_"
        
    # instance method,  methods means behavior of an object
    def steal(self, warrior):
        warrior.lose_stick()
        
  
      
# creating an instance
monster1 = Monster(15, "Ork")

# accessing attributes
print(monster1.age,"\n",monster1.name)

# changing values
monster1.age = 10
print(monster1.age)

# creating another instance
monster2 = Monster(20, "Goblin")
print(monster2.name)

        