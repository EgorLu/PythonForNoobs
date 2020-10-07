import os


def clear_screen():
    ''' Clears the terminal screen (could be improved to store the clear value)'''
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Posix
        os.system('clear')


if __name__ == '__main__':
    # Get players
    players_num = int(input('How many players will be playing?\n'))
    player_names = []
    for i in range(1, players_num + 1):
        player_names.append(input(f'Player #{i} name: '))

    # Get lines
    lines = []
    rounds = players_num * 3
    for game_round in range(rounds):
        print(
            f'Round #{game_round + 1}, {player_names[game_round % players_num]}:')
        lines.append(input('First sentece:\n'))
        clear_screen()
        lines.append(input('Second sentece:\n'))
        # But this can be done cleaner, we could print the last sentence in the list instead.

    # Print lines
    print('\n'.join(lines))
