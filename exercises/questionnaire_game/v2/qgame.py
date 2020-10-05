import sys
import json

''' Main function '''


def main():
    # First of all, welcome the player
    print('Welcome to Python Questionnaire!')

    # Ask for the player's name
    name = input('What is your name?\n')
    print()  # Add a new line after the input, just so it looks nice.

    # Load the questions from the database
    questions = load_questions()

    # Define score
    score = 0

    # Start asking the questions
    for number, question in enumerate(questions, 1):
        print(f'Question #{number}:')
        ask_question(score, question)

    win_game(name, score)


''' Helper functions '''


def load_questions():
    with open('questions.json') as f:
        return json.load(f)


def ask_question(score, question_data):
    # Extract data for comfort
    question = question_data['question']
    answers = question_data['answers']
    correct_answer = question_data['correct_answer']
    # Print the question
    print(question)
    # Print available answers
    for number, answer in enumerate(answers, 1):
        # Print new line for each 2nd question
        if number % 2 != 0:
            end = '\t|\t'
        else:
            end = '\n'
        print(f'{number}: {answer}', end=end)

    # Receive the player's guess
    player_guess = receive_input()

    # Check whether the guess is correct
    if player_guess == correct_answer:
        print('Correct!\n')
        # Increase score
        score += 1
    else:
        lose_game(score)


def receive_input():
    player_guess = ''
    try:
        player_guess = int(input())
        if validate_input(player_guess):
            return player_guess
        else:
            raise ValueError
    except ValueError:
        print('Please enter a number (1-4)')
        return receive_input()


def validate_input(player_guess):
    # At this point we know that the input is an integer,
    # because otherwise it would get caught by the exception.
    if player_guess < 1 or player_guess > 4:
        return False
    return True


def win_game(name, score):
    print(f'Congratulations {name}! You won the game!')
    print(f'Your score is {score}!')


def lose_game(score):
    print('Wrong answer :(')
    # Stop the game
    print(f'Your score is {score}')
    sys.exit()


if __name__ == '__main__':
    # Start the game
    main()
