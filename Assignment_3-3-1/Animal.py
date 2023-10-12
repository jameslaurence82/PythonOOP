class Animal:
    # class attribute
    species = ""
    # static attribute (CAPITALIZED to indicate it is static)
    DNA = "composed of the same Elements.\n"

    # Constructor method for Animal class
    def __init__(self, name, weight, locale):
        # instance attributes for Animal class
        self.name = name  # species name instance attribute
        self.weight = weight  # weight instance attribute
        self.locale = locale  # locale instance attribute

    def details(self):
        return f"The animal is a {self.name} that weighs {self.weight} and resides in {self.locale}."

    # class method to get the class attribute
    @classmethod
    def the_DNA(cls):
        return f"The DNA of the animal is {cls.DNA}."

    # class method to set the class attribute
    @classmethod
    def the_species(cls, species):
        cls.species = species
        return f"The species of the animal is {cls.species}."

    # static method
    @staticmethod
    def the_gender(gender):
        return f"The animal is a {gender}."

# The Animal Class hard-coded instantiated
print("\nCreates and Prints Hardcoded Animal Class Instance for Horse\n")
horse = Animal("Horse", "1000lbs", "Canada")
print(horse.details())
print(horse.the_species("mammal"))  # Set the species directly
print(horse.the_gender("Male"))
print(horse.the_DNA())

# The Animal Class with user input instantiated
print("Creates User Defined Animal Class Instance")

name = input("What is the name of the animal? ")
weight = input("How much does the animal weigh? ")
locale = input("What country is the animal located in? ")
animal1 = Animal(name, weight, locale)
species = input("What species is it? ")  # Get the species input
gender = input("What sex is the animal? ")


# User-generated Animal data prints
print("\nPrints User Defined Animal Class Instance")
print(animal1.details())
print(animal1.the_species(species))  # Access the modified class attribute directly
print(animal1.the_gender(gender))  # Call the set_gender static method
print(animal1.the_DNA())