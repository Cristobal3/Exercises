
class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print('You do {} damage to the goblin.'.format(self.power))
        if enemy.health <= 0:
            print('The goblin is dead')
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def print_status(self):
        




class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print('The goblin does {} damage to you.'.format(self.power))
        if enemy.health <= 0:
            print('You are dead...scrub')

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

hero = Hero(10, 5)
goblin = Goblin(6, 2)

while goblin.alive() and hero.alive():
    hero.attack(goblin)
    goblin.attack(hero)


