import os  # OS module for the 'clear' command

''' Interaction decorator '''


def interation(interaction):
    def wrapper(*args, **kwargs):
        # Clear screen
        os.system('clear')

        # Current interaction
        interaction(*args, **kwargs)

        choice = input('\n>>  ')
        return ACTIONS[interaction.__name__].get(choice)

    return wrapper


''' Game Interactions '''


@interation
def enemy_encounter(enemy):
    print(f'A {enemy.name} ({enemy.level}) appears')
    print('1. Fight')
    print('2. Run')


# Actions definition


ACTIONS = {
    'enemy_encounter': {
        '1': 'fight',
        '2': 'run'
    }
}
