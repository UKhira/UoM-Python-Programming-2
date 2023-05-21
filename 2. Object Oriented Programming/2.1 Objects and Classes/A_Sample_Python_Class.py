#   Objects/Classes are Things that have interaction with each other. to identify a class,
# Class is a noun, and it has interaction with other objects

class Monster:
    #class attributes,  attribute means state,characteristics of objects such as color,size,...
    color = "black"         #'color' attribute, 'black' value
    
    #constructor
    def __init__(self, age, name):
        #instance attributes
        self.age = age
        self.name = name
        
        #private attribute by convention
        self._is_innocent = None
        
    # instance method,  methods means behavior of an object
    def steal(self, warrior):
        warrior.lose_stick()
        