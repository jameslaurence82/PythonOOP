# Creation of Shape class
class Shape:
    #__init__ is used to automatically instantiate the Shape class when called
    # Constructor method for Shape class
    def __init__(self, type, color, area): # instance attributes for Animal class  
        self.type = type # Shape type attribute
        self.color = color # Shape color attribute
        self.area = area # Shape area attribute
        
    # print attributes method for Shape class
    def details(self):
        print(f"The Shape type is: {self.structure} and it is {self.color} in color and it has an area of {self.area}cm squared")