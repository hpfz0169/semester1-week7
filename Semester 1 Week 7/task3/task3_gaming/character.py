# define a parent class called Character with the following fields:
# (1) name - the name of the character
# (2) health - the character's health points
# (3) level - the current level of the character, default to 1
# (4) attack_power - the character base attack power

class Character:

    def __init__(self, name, health, attack_power, level=1):
        self.name = name
        self.health = health
        self.level = level
        self.attack_power = attack_power

    # this class has the following methods:
    # (1) attack() - print a message that the character attacks with their attack power.
    # (2) take_damage(amount) - reduces health by the specific damage amount and prints the updated health.
    #     If health reaches 0 or below, print a message that the character has been defeated
    # (3) level_up() - increases the character's level by 1, boosts the health by 20, attack_power by 5,
    #     and prints a message indicating the character leveled up
    # (4) __str__ - returns a summary of the character's name, level, health, and attack power

    def attack(self):
        print(f"{self.name} attacks with power {self.attack_power}.")

    def take_damage(self, amount):
        self.health -= amount
        if self.health > 0:
            print(f"{self.name}'s current health: {self.health}.")
        else:
            self.health = 0
            print(f"{self.name} has been defeated.")

    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack_power += 5
        print(f"{self.name} leveled up to {self.level}.")

    def __str__(self):
        return f"Character '{self.name}' - Level: {self.level}, Health: {self.health}, Attack Power: {self.attack_power}."


# Warrior subclass
class Warrior(Character):

    def __init__(self, name, health, attack_power, armor, level=1):
        super().__init__(name, health, attack_power, level)
        self.armor = armor

    def power_strike(self):
        print(f"{self.name} performs a Power Strike with 2x power!")

    def take_damage(self, amount):
        reduced_damage = max(0, amount - self.armor)
        self.health -= reduced_damage
        if self.health > 0:
            print(f"{self.name}'s current health: {self.health}.")
        else:
            self.health = 0
            print(f"{self.name} has been defeated.")

    def __str__(self):
        return f"Warrior '{self.name}' - Level: {self.level}, Health: {self.health}, Attack Power: {self.attack_power}, Armor: {self.armor}."


# Mage subclass
class Mage(Character):

    def __init__(self, name, health, attack_power, mana, level=1):
        super().__init__(name, health, attack_power, level)
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.name} casts a powerful spell with 1.5x power!")
        else:
            print(f"{self.name} does not have enough mana to cast the spell.")

    def attack(self):
        print(f"{self.name} casts a spell with power {self.attack_power}.")

    def __str__(self):
        return f"Mage '{self.name}' - Level: {self.level}, Health: {self.health}, Attack Power: {self.attack_power}, Mana: {self.mana}."


# Archer subclass
class Archer(Character):

    def __init__(self, name, health, attack_power, arrows, level=1):
        super().__init__(name, health, attack_power, level)
        self.arrows = arrows

    def shoot_arrow(self):
        if self.arrows > 0:
            self.arrows -= 1
            print(f"{self.name} performs a ranged attack with power {self.attack_power}.")
        else:
            print(f"{self.name} is out of arrows.")

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            print(f"{self.name} shoots an arrow with power {self.attack_power}.")
        else:
            print(f"{self.name} is out of arrows.")

    def __str__(self):
        return f"Archer '{self.name}' - Level: {self.level}, Health: {self.health}, Attack Power: {self.attack_power}, Arrows: {self.arrows}."


# -------------------------
# Creating characters to test
# -------------------------

character1 = Character("Naruto", 100, 20)
warrior1 = Warrior("Guts", 150, 30, 10)
mage1 = Mage("Merlin", 90, 40, 100)
archer1 = Archer("Hawkeye", 80, 25, 5)

character2 = Character("Sasuke", 95, 22)
warrior2 = Warrior("Thor", 180, 35, 15)
mage2 = Mage("Gandalf", 110, 45, 60)
archer2 = Archer("Legolas", 85, 28, 8)

# -------------------------
# Testing Character
# -------------------------
print(character1)
character1.attack()
character1.take_damage(30)
character1.level_up()
print(character1)

print()

# -------------------------
# Testing Warrior
# -------------------------
print(warrior1)
warrior1.attack()
warrior1.power_strike()
warrior1.take_damage(25)   # armor reduces damage
warrior1.level_up()
print(warrior1)

print()

# -------------------------
# Testing Mage
# -------------------------
print(mage1)
mage1.attack()
mage1.cast_spell()
mage1.cast_spell()
mage1.take_damage(50)
mage1.level_up()
print(mage1)

print()

# -------------------------
# Testing Archer
# -------------------------
print(archer1)
archer1.attack()
archer1.shoot_arrow()
archer1.shoot_arrow()
archer1.take_damage(20)
archer1.level_up()
print(archer1)

print()

# -------------------------
# Testing extra characters
# -------------------------
print(character2)
print(warrior2)
print(mage2)
print(archer2)

character2.attack()
warrior2.power_strike()
mage2.cast_spell()
archer2.attack()