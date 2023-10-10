# Creation of Shape class
class Shape:
    
    # class attribute
    dimension = ""
    volume = ""
    # static attribute (CAPITALIZED to indicate it is static)
    SUBJECT = "Geometry"
    
    #__init__ is used to automatically instantiate the Shape class when called
    # Constructor method for Shape class
    def __init__(self, type, color, area): # instance attributes for Animal class  
        self.type = type # Shape type instance attribute
        self.color = color # Shape color instance attribute
        self.area = area # Shape area instance attribute
        
    # print attributes method for Shape class
    def details(self):
        print(f"The Shape type is: {self.type} and it is {self.color} in color and it has an area of {self.area}cm squared")
        
        # class method to call the static class attribute
    def get_SUBJECT(SUBJECT):
        print(f"In methematics this is in {Shape.SUBJECT}")
    
    # Using @classmethod decorator to create a class method 
    @classmethod
    def set_dimension(cls, dimension): # cls is used to refer to the class
        cls.dimension = dimension # class attribute is set to the dimension parameter
        if dimension == "3D":
            
        else:
            dimension == "2D"
            print(f"The object is in the {cls.dimension} ") # prints the class attribute
        
        
    # Using @staticmethod decorator to create a static method    
    @staticmethod
    def set_():
        print(f"The animal is a {}")