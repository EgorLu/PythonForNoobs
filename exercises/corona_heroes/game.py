import random
import sys


from character import Character
from enemies import Enemy, ENEMIES_LIST
import items
import interaction

''' Handles game state '''


class Game():

    def __init__(self):
        self.character = None
        self.possible_events = ['battle']  # TODO: Add loot and others

    def play(self, scenario=None):
        ''' Plays a set or a randomly generated scenario '''
        if scenario:
            pass
        else:  # Random scenario
            while self.character.alive:
                event = random.choice(self.possible_events)
                if event == 'battle':
                    enemy = Enemy(random.choice(ENEMIES_LIST))
                    choice = None
                    while not choice:
                        choice = interaction.enemy_encounter(enemy)
                    if choice == 'fight':
                        self.battle(self.character, enemy)
                    elif choice == 'run':
                        # TODO: Add chance and maybe add enemies that you can't run away from.
                        print('You manage to run away from the enemy')
                    input('Enter to continue')

    def battle(self, oponent1, oponent2):
        '''
        oponent1 is the attacker, thus hits first
        '''

        # Don't battle if any of the oponents is dead
        if not (oponent1.alive and oponent2.alive):
            return

        # Combat
        print(
            f'Battle: {oponent1.name} ({oponent1.level}) vs {oponent2.name} ({oponent2.level})')
        turn = True
        while oponent1.alive and oponent2.alive:
            if turn == 0:
                oponent1.attack(oponent2)
            else:
                oponent2.attack(oponent1)
            turn = not turn

        # Determine who won and grant exp and loot if it's the player
        winner = oponent1 if oponent1.alive else oponent2
        loser = oponent2 if oponent1.alive else oponent1
        if isinstance(winner, Character) and isinstance(loser, Enemy):
            # Exp
            winner.add_exp(loser.grant_exp())
            # Loot
            for item_id, drop_chance in loser.loot:
                if drop_chance - random.random() >= 0:
                    item = items.Item(item_id, items.ITEMS[item_id]['name'])
                    winner.inventory.add(item)
            # Magically heal the winner (remove this later)
            winner.hp = winner._scaling_formula(winner.base_hp)
        else:
            self.game_over()

    def game_over(self):
        print(f'\nGame over\n{self.character}')
        sys.exit()
