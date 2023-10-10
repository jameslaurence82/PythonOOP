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


