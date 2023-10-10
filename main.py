from Animal import Animal # Imports the Animal class from Animal.py
from Shape import Shape # Imports the Shape class from Shape.py

if __name__ == "__main__": # If this file is being run directly
    # The Animal Class hard coded is instantiated
    horse = Animal("Horse", "1000lbs", "Canada")
    horse.details()
    horse.set_species("Mammal")
    horse.set_gender("Male")
    horse.get_DNA()
    # The Animal Class hard coded instantiated
    frog = Animal("Frog", "1lbs", "Mexico")
    frog.details()
    frog.set_species("Amphibian")
    frog.set_gender("Female")
    frog.get_DNA()
    
    # The Shape Class hard coded is instantiated
    square = Shape("square", "red", 300)
    square.details()
    
    # The Animal Class with user input is instantiated
    
    
    
    
    # The Shape Class with user input is instantiated