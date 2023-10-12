# Creation of Shape class
class Shape:
    
    # class attribute
    dimension = ""
    volume = 0
    
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
    def the_SUBJECT(SUBJECT):
        print(f"In mathematics this is used in {Shape.SUBJECT}")
\
    # Using @classmethod decorator to create a class method 
    @classmethod
    def the_dimension(cls, newDimension,instance): # cls is used to refer to the class
        # cls.dimension = dimension # class attribute is set to the dimension parameter
        cls.dimension = newDimension
        if newDimension == "2D":
            print(f"The object is in {cls.dimension} ") # prints the class attribute 
        else:
            newDimension == "3D"
            area = float(instance.area)
            height = float(input("What is the height of the object?"))
            cls.volume = height * area # <<<===== issue with getting area! from initialization
            print(f"The object is in {cls.dimension} and it's volume is {cls.volume}")
            
        # Using @staticmethod decorator to create a static method 
        @staticmethod #<<==== have to figure out a unit conversion method
        def unitConversion():
            pass
        
# The Shape Class hard coded is instantiated
square = Shape("square", "red", 300)
square.details()
square.the_SUBJECT()
square.the_dimension("2D", square)
square.the_dimension("3D", square) # <<== issue with this line of code on module
