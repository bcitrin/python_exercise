import random

from colorama import Fore, Style

#Todo: documentation

class Plant:
    def __init__(self, name, species, age, water_level, water_requirement, light_requirement, height):
        self.name = name
        self.species = species
        self.age = age
        self.water_level = water_level
        self.light_exposure = random.uniform(0, 1)
        self.water_requirement = water_requirement
        self.light_requirement = light_requirement
        self.height = height

    def water(self, amount):
        self.water_level += amount
        if self.water_level > self.water_requirement:
            print(Fore.YELLOW + f"Warning: {self.name}'s water level is currently at {self.water_level:.2f} mm while it should not cross {self.water_requirement} mm. "\
                "Save him from drowning!" + Style.RESET_ALL)

    def provide_light(self, intensity):
        self.light_exposure = intensity
        if self.light_exposure > self.light_requirement:
            print(Fore.YELLOW + f"Warning: {self.name}'s light intensity is currently at {self.light_exposure:.2f} lux where it should not cross {self.light_requirement} lux. "\
                "Consider reducing the light level or moving your plan to the shade!" + Style.RESET_ALL)
        
    def grow(self):
        if self.light_exposure < self.light_requirement:
            growth = 0
        else:
            growth = random.uniform(0, 1) * min(self.water_level - self.water_requirement, 1)
        self.height += growth
        self.water_level = 0

class IrrigationSystem:
    def __init__(self, water_level):
        self.water_level = water_level

    def add_water(self, amount):
        self.water_level += amount

    def irrigate_plants(self, plant_list):
        water_per_plant = self.water_level / len(plant_list)
        for plant in plant_list:
            plant.water(water_per_plant) #Todo: consider only watering as required and keeping spares. Could at the end water whoever needs with the spares.
        self.water_level = 0

class GreenhouseController:
    def __init__(self, irrigation_system):
        self.plants = []
        self.irrigation_system = irrigation_system

    def add_plant(self, plant):
        self.plants.append(plant)

    def water_plants(self):
        self.irrigation_system.irrigate_plants(self.plants)

    def run_simulation(self, days):
        for _ in range(days):
            self.water_plants()
            for plant in self.plants:
                plant.provide_light(random.uniform(0, 1))
                plant.grow()
            self.irrigation_system.add_water(random.uniform(0, 1))

# Testing
if __name__ == "__main__":
    # Create sample plants
    plant1 = Plant("Rose", "Rosa", 10, 0.5, 1.5, 0.7, 10)
    plant2 = Plant("Tulip", "Tulipa", 5, 0.4, 2.0, 0.6, 8)

    # Create an irrigation system with 2 liters of water
    irrigation_system = IrrigationSystem(1)

    # Create a greenhouse controller
    greenhouse = GreenhouseController(irrigation_system)

    # Add plants to the greenhouse
    greenhouse.add_plant(plant1)
    greenhouse.add_plant(plant2)

    # Run the simulation for 5 days
    greenhouse.run_simulation(5)

    # Display the results
    print("Plans state after simulation:")
    for plant in greenhouse.plants:
        print(f"Plant: {plant.name}, Height: {plant.height:.2f} cm")

