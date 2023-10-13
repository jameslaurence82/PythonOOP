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
    
    # method to call the class counter
    @classmethod
    def classCounter(cls):
        return f"This is instantiation # {cls.counter} of the Parent Class"

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
    Shape.counter = 0
    def __init__(self, model, color, area, sides):
        super().__init__(model, color, area)
        self.sides = sides
        Shape.counter =+ 1
    
    def details(self):
        return f"The Shape is a {self.model} and it is {self.color} in color and it has an area of {self.area} cm squared and it has {self.sides} sides."
    # method to call the class counter
    @classmethod
    def classCounter(cls):
        # this goal of using the same name (classCounter() from the parent is to override it when counting 
        # the child instances as the values should be different.
        return f"This is instantiation # {cls.counter} of the Child Class"



# Creation of the parent class
print("\nFirst Instantiation of Parent Class")
print("--------------------------------------")
rectangle = Shape("rectangle", "red", 300) # Parent instantiation
print(rectangle.details()) # calls details method from Parent Class
print(rectangle.the_SUBJECT()) # calls the static method to print the subject name
print("This hardcodes 2D option of if statement")
print(rectangle.the_dimension("2D", rectangle))
print("This is the hardcodes 3D option of if statement")
print(rectangle.the_dimension("3D", rectangle)) 
print(Shape.classCounter())

# Creation of the child class
print("\nFirst Instantiation of Child Class")
print("-------------------------------------")
square1 = Square("square", "blue", 400, 4)
print(square1.details()) # calls parent details method from Parent Class
print(square1.the_SUBJECT()) # calls the parent static method from Parent Class to print the subject name 
print("This hardcodes 2D option of if statement")
print(square1.the_dimension("2D", square1)) # uses if statement from Parent Class to say if object is 2d or 3d
print("This hardcodes 3D option of if statement")
print(square1.the_dimension("3D", square1)) # else part of if from Parent Class statement for 3d asks for height and gives volume
print(Square.details(square1)) # calls the details method from the child class which overrides the parent details method
print(f"This child class of Shape has {square1.sides} sides") 
print(Square.classCounter()) # calls the class counter from the child class which is different from the parent class counter

# Creation of the parent class
print("\nSecond Instantiation of Parent Class")
print("--------------------------------------")
parallelogram = Shape("Parallelogram", "purple", 150)
print(parallelogram.details())
print(parallelogram.the_SUBJECT())
print("This hardcodes 2D option of if statement")
print(parallelogram.the_dimension("2D", parallelogram))
print("This is the hardcodes 3D option of if statement")
print(parallelogram.the_dimension("3D", parallelogram))
print(Shape.classCounter()) # calls the parent class counter which will be 2 as this is the second parent class instance

print("4 parent class instantiations and 3 child class instantiations are now created")
shape1 = Shape("Parallelogram", "purple", 150)
print(f"parent class {shape1.details()}")
square2 = Square("square", "blue", 400, 4)
print(f"child class {square2.details()}")
shape2 = Shape("Parallelogram", "purple", 150)
print(f"parent class {shape2.details()}")
square3 = Square("square", "blue", 400, 4)
print(f"child class {square3.details()}")
shape3 = Shape("Parallelogram", "purple", 150)
print(f"parent class {shape3.details()}")
square4 = Square("square", "blue", 400, 4)
print(f"child class {square4.details()}")
shape4 = Shape("Parallelogram", "purple", 150)
print(f"parent class {shape4.details()}")
# after these 4 parent instances there should be 6 instances of the parent class
# after these 3 child instances there should be 5 instances of the child class
print("Prints total number of parent class instantiations - should be 6")
print(Shape.classCounter())
print("Prints total number of child class instantiations - should be 5")
print(Square.classCounter())


