# Creation of Shape class
class Shape:
    
    # class attribute
    dimension = ""
    volume = ""
    # static attribute (CAPITALIZED to indicate it is static)
    SUBJECT = "Geometry"
    
    #__init__ is used to automatically instantiate the Shape class when called
    # Constructor method for Shape class
    def __init__(self, model, color, area): # instance attributes for Animal class  
        self.model = model # Shape type instance attribute
        self.color = color # Shape color instance attribute
        self.area = area # Shape area instance attribute
        
    # print attributes method for Shape class
    def details(self):
        print(f"The Shape is a {self.model} and it is {self.color} in color and it has an area of {self.area} cm squared")
        
    # class method to call the static class attribute
    def get_SUBJECT(SUBJECT):
        print(f"In mathematics this is used in {Shape.SUBJECT}")
    
    def get_height():
        return print(input("What is the height of the object?"))
    
    # Using @classmethod decorator to create a class method 
    @classmethod
    def set_dimension(cls, dimension): # cls is used to refer to the class
        cls.dimension = dimension # class attribute is set to the dimension parameter
        if dimension == "2D":
            print(f"The object is in {cls.dimension} ") # prints the class attribute 
        else:
            dimension == "3D"
            cls.volume = (Shape.get_height()*cls.area) # <<<===== issue with getting area! from initialization
            print(f"The object is in {cls.dimension} and it's volume is {cls.volume()}")
            
        # Using @staticmethod decorator to create a static method 
        # @staticmethod <<==== have to figure out a staticmethod to use