import sys

# First of all, welcome the player
print('Welcome to Python Questionnaire!')

# Ask for the player's name
name = input('What is your name?\n')
print()  # Add a new line after the input, just so it looks nice.

# Keep the score
score = 0

''' Game start '''

# Ask the first question
print('Question #1: What is the first letter of the English alphabet?')
print('1: A', end='\t|\t')
print('2: B')
print('3: C', end='\t|\t')
print('4: D')
# Receive the player's guess
# At this point, we do not validate input and assume that it's a number between 1 and 4.
player_guess = int(input())
# Check whether the answer is correct
if player_guess == 1:
    print('Correct!\n')
    # Increase score
    score += 1
else:
    print('Wrong answer :(')
    # Stop the game
    print(f'Your score is {score}')
    sys.exit()

# Ask the second question
print('Question #2: What is COVID-19?')
print('1: A new Avengers movie', end='\t|\t')
print('2: A global virus')
print('3: A new brand of the Corona beer', end='\t|\t')
print('4: Government\'s plan to infuse the population with electronic chips')
# Receive the player's guess
# At this point, we do not validate input and assume that it's a number between 1 and 4.
player_guess = int(input())
# Check whether the answer is correct
if player_guess == 4:
    print('Correct!\n')
    # Increase score
    score += 1
else:
    print('Wrong answer :(')
    # Stop the game
    print(f'Your score is {score}')
    sys.exit()

# Ask the third question
print('Question #3: Did dinosaurs exist?')
print('1: Yes, this is proven by a plethora of evidence', end='\t|\t')
print('2: No, Native Americans carve the fossils from bear bones and bury them across the world')
print('3: Yes, in the Jurassic World', end='\t|\t')
print('4: Yes and they live amongst us nowadays')
# Receive the player's guess
# At this point, we do not validate input and assume that it's a number between 1 and 4.
player_guess = int(input())
# Check whether the answer is correct
if player_guess == 2:
    print('Correct!\n')
    # Increase score
    score += 1
else:
    print('Wrong answer :(')
    # Stop the game
    print(f'Your score is {score}')
    sys.exit()

# Ask the fourth question
print('Question #4: Can you use Google Drive if you don\'t have a driver\'s license?')
print('1: No, unless using a self-driving computer', end='\t|\t')
print('2: Yes, only if you install the relevant drivers')
print('3: The government is ran by Lizardmen', end='\t|\t')
print('4: Google Drive and driving a vehicle are unrelated')
# Receive the player's guess
# At this point, we do not validate input and assume that it's a number between 1 and 4.
player_guess = int(input())
# Check whether the answer is correct
if player_guess == 3:
    print('Correct!\n')
    # Increase score
    score += 1
else:
    print('Wrong answer :(')
    # Stop the game
    print(f'Your score is {score}')
    sys.exit()

''' End of questions, the game is won '''
print(f'Congratulations {name}! You won the game!')
print(f'Your score is {score}!')
