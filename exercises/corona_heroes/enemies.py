from game_objects import Creature

TROLL = 'Troll'
ORC = 'Orc'
GOBLIN = 'Goblin'
FIVEG = '5G Radiation'
SCIENTIST = 'Evil Scientist'
GMO = 'GMO'
COVID = 'COVID-19'
ENEMIES_LIST = [TROLL, ORC, GOBLIN, FIVEG, SCIENTIST, GMO, COVID]
BILL = 'Bill Gates'
PHARMA = 'Big Pharma'
STATE = 'The Deep State'
BOSSES_LIST = [BILL, PHARMA, STATE]

ENEMIES = {
    TROLL: {
        'hp': 200,
        'power': 15,
        'exp_reward': 20,
        'loot': [
            (1, 0.5),  # Item ID, drop chance
            (2, 0.3)
        ]
    },
    ORC: {
        'hp': 120,
        'power': 15,
        'exp_reward': 12,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    },
    GOBLIN: {
        'hp': 80,
        'power': 10,
        'exp_reward': 10,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    },
    FIVEG: {
        'hp': 50,
        'power': 50,
        'exp_reward': 10,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    },
    SCIENTIST: {
        'hp': 80,
        'power': 30,
        'exp_reward': 10,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    },
    GMO: {
        'hp': 80,
        'power': 30,
        'exp_reward': 10,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    },
    COVID: {
        'hp': 80,
        'power': 30,
        'exp_reward': 10,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    },
    BILL: {
        'hp': 2000,
        'power': 300,
        'exp_reward': 10,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    },
    PHARMA: {
        'hp': 2000,
        'power': 300,
        'exp_reward': 10,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    },
    STATE: {
        'hp': 2000,
        'power': 300,
        'exp_reward': 10,
        'loot': [
            (1, 0.5),
            (2, 0.3)
        ]
    }
}


class Enemy(Creature):

    def __init__(self, enemy_type, level=1):
        super().__init__(enemy_type, level)
        self.base_hp = ENEMIES[enemy_type]['hp']
        self.base_power = ENEMIES[enemy_type]['power']
        self.base_exp_reward = ENEMIES[enemy_type]['exp_reward']
        self.loot = ENEMIES[enemy_type]['loot']
        self.hp = self._scaling_formula(self.base_hp)
        self.power = self._scaling_formula(self.base_power)

    def grant_exp(self):
        return self._scaling_formula(self.base_exp_reward)
