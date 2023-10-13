"""
=====Task for code review=============

1. Implement inheritance. Make two instances of parent class and one of child classes unless you already have
2. Count the number of instances of Parent class and Child class. (the number of Parent 
class instances can either include or exclude the number of Child instances)
3. In your Child class, create a new attribute which your Parent class doesn't have. 
"""
# Creation of Shape Parent class
class Shape:
    
    #class counter as per code review
    counter = 0
    
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
        Shape.counter += 1 # to add the number of instances created
        
    # print attributes method for Shape class
    def details(self):
        return f"The Shape is a {self.model} and it is {self.color} in color and it has an area of {self.area} cm squared"
    
    # Using @classmethod decorator to create a class method 
    @classmethod
    def the_dimension(cls, newDimension,instance): # cls is used to refer to the class
        # cls.dimension = dimension # class attribute is set to the dimension parameter
        cls.dimension = newDimension
        if newDimension == "2D":
            return f"The object is in {cls.dimension} " # returns the class attribute 
        else:
            newDimension == "3D"
            area = float(instance.area)
            height = float(input("What is the height of the object? "))
            cls.volume = height * area # <<<===== issue with getting area! from initialization
            return f"The object is in {cls.dimension} and it's volume is {cls.volume} cm cubed." # returns the class attribute and volume calc
        
    # class method to call the static class attribute
    def the_SUBJECT(SUBJECT):
        return f"In mathematics this is used in {Shape.SUBJECT}."    
    
    # Using @staticmethod decorator to create a static method 
    @staticmethod #<<==== Still have to figure out a how to implement a static method
    def unitConversion():
        pass

# Creation of Child Class    
class Square(Shape):
    
    def __init__(self,sides):
        super().__init__(sides)self.side = sides
    


# Creation of the parent class
print("\nFirst Instantiation of Parent Class")
print("-------------------------------")
rectangle = Shape("rectangle", "red", 300)
print(rectangle.details())
print(rectangle.the_SUBJECT())
print("This hardcodes 2D option of if statement")
print(rectangle.the_dimension("2D", rectangle))
print("This is the hardcodes 3D option of if statement")
print(rectangle.the_dimension("3D", rectangle)) 
print(f"This is instiantation # {Shape.counter}")
# Creation of the parent class
print("\nSecond Instantiation of Parent Class")
print("-------------------------------")
parallelogram = Shape("Parallelogram", "purple", 150)
print(parallelogram.details())
print(parallelogram.the_SUBJECT())
print("This hardcodes 2D option of if statement")
print(parallelogram.the_dimension("2D", parallelogram))
print("This is the hardcodes 3D option of if statement")
print(parallelogram.the_dimension("3D", parallelogram)) 
print(f"This is instiantation # {Shape.counter}")
# Creation of the child class
print("\nInstantiation of Child Class")
print("-----------------------------")
square1 = Square("square", "blue", 400)
print(square1.details())
print(square1.the_SUBJECT())
print("This hardcodes 2D option of if statement")
print(square1.the_dimension("2D", square1))
print("This hardcodes 3D option of if statement")
print(square1.the_dimension("3D", square1)) 
print(f"This is instantiation # {Shape.counter}")