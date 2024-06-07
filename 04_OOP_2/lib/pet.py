#!/usr/bin/env python3
# Class Attributes and Methods


class Pet:

    total_pets = 0
    all = []

    @classmethod
    def increase_pets(cls, increment=1):
        cls.total_pets += increment

    def __init__(self, name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        # Pet.total_pets += 1
        # Pet.increase_pets()
        self.__class__.increase_pets()
        self.__class__.all.append(self)

    # 6✅. Create a class method increase_pets that will increment total_pets
    # replace Pet.total_pets += 1 in __init__ with increase_pets()

    def print_pet_details(self):
        print(
            f"""
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
        """
        )
