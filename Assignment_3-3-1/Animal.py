# Creation of Animal class
# The following will be included in the code below
# __init__ function, class attribute, class method, instance attribute, 
# instance method, static attribute
class Animal():
    
    # class attribute
    species = "" 
    # static attribute (CAPITALIZED to indicate it is static)
    DNA = "composed of the same Elements\n"
    #__init__ is used to automatically instantiate the Animal class when called
    # Constructor method for Animal class
    def __init__(self, name, weight, locale): # instance attributes for Animal class  
        self.name = name # species name instance attribute
        self.weight = weight # weight instance attribute
        self.locale = locale # locale instance attribute

    # instance method
    # print attributes method for Animal class
    # def details(self):
    #     print(f"The animal is: {self.name} and it weighs {self.weight} and it is located in {self.locale}")

    def details(self):
        return f"The animal is: {self.name} and it weighs {self.weight} and it is located in {self.locale}"

    # class method to call the static class attribute
    def get_DNA(DNA):
        return f"The DNA of the animal is {Animal.DNA}"
    
    # Using @classmethod decorator to create a class method 
    @classmethod
    def set_species(cls, species): # cls is used to refer to the class
        cls.species = species # class attribute is set to the species parameter
        return f"The animal species is {cls.species}" # prints the class attribute
    """
    Test to change to instance method
    @classmethod
    def set_species(cls, species): # cls is used to refer to the class
        cls.species = species # class attribute is set to the species parameter
        return f"The animal species is {cls.species}" # prints the class attribute
    """
    
    
        
    # Using @staticmethod decorator to create a static method    
    @staticmethod
    def set_gender(gender):
        return f"The animal is a {gender}"
# # The Animal Class hard coded instantiated
print("\nCreates Hardcoded Animal Class Instance for Horse")
horse = Animal("Horse", "1000lbs", "Canada")
print(horse.details())
print(horse.set_species("Mammal"))
print(horse.set_gender("Male"))
print(horse.get_DNA())
# The Animal Class with user input instantiated
print("Creates User Defined Animal Class Instance")
animal1 = Animal("", "", "")
animal1.name = input("What is the name of the animal? ")
animal1.weight = input("How much does the animal weigh? ")
animal1.locale = input("What country is the animal located in? ")
animal1.set_gender = input("What sex is the animal? ")
print("\nPrints User Defined Animal Class Instance")
print(animal1.details())
print(animal1.set_species())
print(animal1.set_gender())
print(animal1.get_DNA())