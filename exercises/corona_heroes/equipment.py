# Armor
HEAD = 'head'
CHEST = 'chest'
GLOVES = 'gloves'
LEGS = 'legs'
BOOTS = 'boots'
# Hands
MAIN_HAND = 'main_hand'
OFF_HAND = 'off_hand'

class Equipment():

    def __init__(self, name, slot, stats):
        self.name = name
        self.slot = slot
        self.stats = stats # HP and Power currently