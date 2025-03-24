# monster.py
import random
from character import Character

class Monster(Character):
    def __init__(self, name):
        """Initialize the Monster with rolled combat strength and health points."""
        combat_strength = random.randint(1, 12)  # Random dice roll for combat strength
        health_points = random.randint(10, 30)   # Random dice roll for health points
        super().__init__(name, combat_strength, health_points)

    def monster_attacks(self, hero):
        """Monster attacks the hero."""
        print(f"{self.name} attacks {hero.name} with strength {self.combat_strength}!")
        hero.take_damage(self.combat_strength)

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector.")
