from animals import Penguin
from habitat import Habitat


# Create a penguin
bob = Penguin("Bob")

# Create a habitat
seaworld = Habitat("Sea World")
seaworld.add_animal(bob)

for animal in seaworld.animals:
    print(animal)
