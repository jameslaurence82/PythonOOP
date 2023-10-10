# Creation of Animal class
# The following will be included in the code below
# __init__ function, class attribute, class method, instance attribute, 
# instance method, static attribute
class Animal():
    
    species = "" # class attribute
    DNA = "Composed of the same Elements" # static attribute
    #__init__ is used to automatically instantiate the Animal class when called
    # Constructor method for Animal class
    def __init__(self, name, weight, locale): # instance attributes for Animal class  
        self.name = name # species name instance attribute
        self.weight = weight # weight instance attribute
        self.locale = locale # locale instance attribute

    # instance method
    # print attributes method for Animal class
    def details(self):
        print(f"The animal is: {self.name} and it weighs {self.weight} and it is located in {self.locale}")

    # Using @classmethod decorator to create a class method
    @classmethod
    def set_species(cls, species):
        cls.species = species
        print(f"The animal species is {cls.species}")
        
    @staticmethod
    def gender(gender):
        print(f"The animal is a {gender}")

