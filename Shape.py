# Creation of Shape class
class Shape:
    
    # class attribute
    dimension = "" 
    # static attribute (CAPITALIZED to indicate it is static)
    SUBJECT = "Geometry"
    
    #__init__ is used to automatically instantiate the Shape class when called
    # Constructor method for Shape class
    def __init__(self, type, color, area): # instance attributes for Animal class  
        self.type = type # Shape type attribute
        self.color = color # Shape color attribute
        self.area = area # Shape area attribute
        
    # print attributes method for Shape class
    def details(self):
        print(f"The Shape type is: {self.structure} and it is {self.color} in color and it has an area of {self.area}cm squared")
        
        # class method to call the static class attribute
    def get_SUBJECT(SUBJECT):
        print(f"This shape is used in the {Shape.SUBJECT} area of Mathematics")
    
    # Using @classmethod decorator to create a class method 
    @classmethod
    def set_species(cls, species): # cls is used to refer to the class
        cls.species = species # class attribute is set to the species parameter
        print(f"The animal species is {cls.species}") # prints the class attribute
        
    # Using @staticmethod decorator to create a static method    
    @staticmethod
    def set_gender(gender):
        print(f"The animal is a {gender}")