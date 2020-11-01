from game_objects import Creature
from items import Item

WARRIOR = 'Warrior'
MAGE = 'Mage'

class_stats = {
    WARRIOR: {
        'hp': 100,
        'power': 30
    },
    MAGE: {
        'hp': 100,
        'power': 10
    }
}


class Character(Creature):

    def __init__(self, name, char_class, level=1):
        super().__init__(name, level)
        self.exp = 0
        self.char_class = char_class
        self.base_hp = class_stats[char_class]['hp']
        self.hp = self.base_hp
        self.base_power = class_stats[char_class]['power']
        self.power = self.base_power
        self.equipment = CharacterEquipment()
        self.inventory = CharacterInventory()

    def __str__(self):
        return f'{self.name}, {self.char_class} is {"alive" if self.alive else "dead"}'

    def equip(self, item):
        prev_item = getattr(self.equipment, item.slot)
        if prev_item:
            self.inventory.add(prev_item)
        setattr(self.equipment, item.slot, item)
        print(f'{self.name} equipped {item.name}')

    def attack(self, target):
        # Calculate damage
        damage = self.power
        if self.equipment.main_hand:
            damage += self.equipment.main_hand.stats['damage']
        if self.equipment.off_hand:
            damage += self.equipment.off_hand.stats['damage']
        # Send damage to the parent `attack` method
        super().attack(target, damage)

    def add_exp(self, exp):
        print(f'{self.name} received {exp} experience')
        self.exp += exp
        # Player levels up every 100 exp, increasing by the scaling formula.
        to_next_level = self._scaling_formula(100)
        if self.exp > to_next_level:
            self.level_up()
            self.exp -= to_next_level

    def level_up(self):
        self.level += 1
        print(f'{self.name} leveled up! ({self.level})')


class CharacterEquipment():

    def __init__(self):
        # Armor
        self.head = None
        self.chest = None
        self.gloves = None
        self.legs = None
        self.boots = None
        # Hands
        self.main_hand = None
        self.off_hand = None

    def __str__(self):
        result = ''
        for slot, item in self.__dict__.items():
            pretty_slot = slot.title().replace('_', ' ')
            result += f'{pretty_slot}: {getattr(item, "name", "Empty")}\n'
        return result


class CharacterInventory():

    def __init__(self):
        self.items = []
        self.max_items = 20

    def add(self, item):
        if isinstance(item, Item):
            if len(self.items) < self.max_items:
                self.items.append(item)
            else:
                print('Inventory is full')
        else:
            raise ValueError(f'{item} is not of Item type')

    def remove(self, item):
        self.items.remove(item)

    def __str__(self):
        items = [item.name for item in self.items]
        return 'Inventory:\n' + (', '.join(items) if items else 'Empty')
