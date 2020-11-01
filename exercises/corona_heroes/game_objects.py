class Creature():

    def __init__(self, name, level=1):
        self.name = name
        self.alive = True
        self.level = level
        self.hp = 1
        self.power = 1

    def __str__(self):
        return f'{self.name} is {"alive" if self.alive else "dead"}'

    def attack(self, target, damage=None):
        damage = damage or self.power
        if issubclass(target.__class__, Creature):
            print(f'{self.name} attacks {target.name} for {damage} damage!')
            target.receive_damage(damage)
        else:
            print(f'{self.name} cannot attack that')

    def receive_damage(self, damage):
        # print(f'{self.name} receives {damage} points of damage')
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            print(f'{self.name} has died')
        else:
            print(f'{self.name} has {self.hp} HP left')

    def _scaling_formula(self, stat):
        ''' Add 10% to the base stat for each level '''
        return int(stat * (10 + self.level - 1) / 10)

