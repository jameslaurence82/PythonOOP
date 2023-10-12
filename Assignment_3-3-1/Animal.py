class Animal:
    # class attribute
    species = ""
    # static attribute (CAPITALIZED to indicate it is static)
    DNA = "composed of the same Elements\n"

    # Constructor method for Animal class
    def __init__(self, name, weight, locale):
        # instance attributes for Animal class
        self.name = name  # species name instance attribute
        self.weight = weight  # weight instance attribute
        self.locale = locale  # locale instance attribute

    def details(self):
        return f"The animal is: {self.name} and it weighs {self.weight} and it is located in {self.locale}"

    # class method to get the class attribute
    @classmethod
    def get_DNA(cls):
        return f"The DNA of the animal is {cls.DNA}"

    # class method to set the class attribute
    @classmethod
    def set_species(cls, species):
        cls.species = species

    # static method
    @staticmethod
    def set_gender(gender):
        return f"The animal is a {gender}"

# The Animal Class hard-coded instantiated
print("\nCreates and Prints Hardcoded Animal Class Instance for Horse\n")
horse = Animal("Horse", "1000lbs", "Canada")
print(horse.details())
horse.set_species("Mammal")  # Set the species directly
print(horse.set_gender("Male"))
print(horse.get_DNA())

# The Animal Class with user input instantiated
print("Creates User Defined Animal Class Instance")
animal1 = Animal("", "", "")
animal1.name = input("What is the name of the animal? ")
animal1.weight = input("How much does the animal weigh? ")
animal1.locale = input("What country is the animal located in? ")
species = input("What species is it? ")  # Get the species input
animal1.set_species(species)  # Set the class attribute 'species' using the method
animal1.gender = input("What sex is the animal? ")

# User-generated Animal data prints
print("\nPrints User Defined Animal Class Instance")
print(animal1.details())
print(animal1.species)  # Access the modified class attribute directly
print(animal1.set_gender("Female"))  # Call the set_gender static method
print(animal1.get_DNA())