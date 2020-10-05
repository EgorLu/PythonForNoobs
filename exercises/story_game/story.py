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
        lines.append(
            input(f'Round #{game_round + 1}, {player_names[game_round % players_num]}:\n'))

    # Print lines
    print('\n'.join(lines))
