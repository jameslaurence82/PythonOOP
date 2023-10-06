# Creation of Animal class
class Animal():
    #__init__ is used to automatically instantiate the Animal class when called
    # Constructor method for Animal class
    def __init__(self, species, weight, locale): # instance attributes for Animal class  
        self.species = species # species attribute
        self.weight = weight # weight attribute
        self.locale = locale # locale attribute

    # print attributes method for Animal class
    def details(self):
        print(f"The Species is: {self.species} and it weighs {self.weight} and it is located in {self.locale}")

class Shape:
        #__init__ is used to automatically instantiate the Animal class when called
    # Constructor method for Animal class
    def __init__(self, structure, color, area): # instance attributes for Animal class  
        self.structure = structure # Shape type attribute
        self.color = color # Shape color attribute
        self.area = area # Shape area attribute
        
    # print attributes method for Shape class
    def details(self):
        print(f"The Shape type is: {self.structure} and it is {self.color} in color and it has an area of {self.area}cm squared")
_horse = Animal("Horse2", "1000lbs", "Canada")
_horse.details()