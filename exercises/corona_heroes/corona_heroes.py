#!/usr/bin/env python3

import menu
import game

# Temp
import enemies
import equipment

if __name__ == '__main__':
    game = game.Game()

    menu.menu_main(game)

    character = game.character

    # New item
    sword = equipment.Equipment(
        'Sword of Destiny', equipment.MAIN_HAND, {'damage': 100})
    character.equip(sword)

    game.play()
