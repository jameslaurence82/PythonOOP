# Creation of Animal class
class Animal():
    #__init__ is used to automatically instantiate the Animal class when called
    def __init__(self, species, weight, locale): # instance attributes for Animal class  
        self.species = species # species attribute
        self.weight = weight # weight attribute
        self.locale = locale # locale attribute
        