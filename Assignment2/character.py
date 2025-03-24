# character.py
class Character:
    def __init__(self, name, combat_strength, health_points):
        self.name = name
        self._combat_strength = combat_strength
        self._health_points = health_points

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value > 0:
            self._combat_strength = value
        else:
            print("Combat strength must be positive.")

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value >= 0:
            self._health_points = value
        else:
            print("Health points must not be negative.")

    def attack(self, target):
        """Attack another character."""
        print(f"{self.name} attacks {target.name} with strength {self.combat_strength}!")
        target.take_damage(self.combat_strength)

    def take_damage(self, damage):
        """Take damage from an attack."""
        self._health_points -= damage
        if self._health_points <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} now has {self._health_points} health left.")

    def is_alive(self):
        """Check if character is still alive."""
        return self._health_points > 0
