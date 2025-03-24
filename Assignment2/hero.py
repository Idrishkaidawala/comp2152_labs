# hero.py
import random
from character import Character

class Hero(Character):
    def __init__(self, name):
        """Initialize the Hero with rolled combat strength and health points."""
        combat_strength = random.randint(1, 10)  # Random dice roll for combat strength
        health_points = random.randint(5, 20)    # Random dice roll for health points
        super().__init__(name, combat_strength, health_points)

    def hero_attacks(self, monster):
        """Hero attacks the monster."""
        print(f"{self.name} attacks {monster.name} with strength {self.combat_strength}!")
        monster.take_damage(self.combat_strength)

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector.")
