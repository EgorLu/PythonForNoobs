import os  # OS module for the 'clear' command
from functools import partial  # Partial function for character creation

import character  # In order to create a character


game_object = None


''' Menu decorator '''


def menu_decorator(menu):
    def wrapper(*args, **kwargs):
        # Clear screen
        os.system('clear')

        # Current menu
        menu(*args, **kwargs)

        choice = input('\n>>  ')
        exec_menu(choice, menu.__name__)

    return wrapper


''' Menu functions '''


@menu_decorator
def menu_main(game):
    global game_object
    if not game_object:
        game_object = game
    print('Corona heroes')
    print('1. New game')
    print('2. Load game')


@menu_decorator
def menu_create_char():
    print('Choose class')
    print('1. Warrior')
    print('2. Mage')


def create_character(char_class):
    global game_object
    name = input('Name: ')
    game_object.character = character.Character(name, char_class)
    os.system('clear')
    print(f'{name} the {char_class} is born!')


''' Execute Menu '''


def exec_menu(choice, current_menu):
    # If the 'choice' action exists in the current menu's options, use it.
    # Otherwise remain the in the current menu.
    menu_actions[current_menu].get(choice, globals()[current_menu])()


# Menu definition
menu_actions = {
    'menu_main': {
        '1': menu_create_char,
        # "2": None,
    },
    'menu_create_char': {
        '1': partial(create_character, character.WARRIOR),
        '2': partial(create_character, character.MAGE)
    }
}
