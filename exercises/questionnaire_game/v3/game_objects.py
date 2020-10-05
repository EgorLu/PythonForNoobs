import json
import sys


class Game():
    def __init__(self):
        self.score = 0
        self.name = ''
        self.questions = []

    def start(self):
        self.name = input('What is your name?\n')
        self.load_questions()

        for number, question in enumerate(self.questions, 1):
            print(f'Question #{number}:')
            self.ask_question(question)

        self.win_game()

    def load_questions(self):
        with open('questions.json') as f:
            questions_json = json.load(f)
        for question in questions_json:
            self.questions.append(Question(question))

    def ask_question(self, question_data):
        # Print the question
        print(question_data.question)
        # Print available answers
        for number, answer in enumerate(question_data.answers, 1):
            # Print new line for each 2nd question
            if number % 2 != 0:
                end = '\t|\t'
            else:
                end = '\n'
            print(f'{number}: {answer}', end=end)

        # Receive the player's guess
        player_guess = self.receive_input()

        # Check whether the guess is correct
        if player_guess == question_data.correct_answer:
            print('Correct!\n')
            # Increase score
            self.score += 1
        else:
            self.lose_game()

    def receive_input(self):
        player_guess = ''
        try:
            player_guess = int(input())
            if self.validate_input(player_guess):
                return player_guess
            else:
                raise ValueError
        except ValueError:
            print('Please enter a number (1-4)')
            return self.receive_input()

    def validate_input(self, player_guess):
        # At this point we know that the input is an integer,
        # because otherwise it would get caught by the exception.
        if player_guess < 1 or player_guess > 4:
            return False
        return True

    def win_game(self):
        print(f'Congratulations {self.name}! You won the game!')
        print(f'Your score is {self.score}!')

    def lose_game(self):
        print('Wrong answer :(')
        # Stop the game
        print(f'Your score is {self.score}')
        sys.exit()


class Question():
    def __init__(self, question_data):
        self.question = question_data['question']
        self.answers = question_data['answers']
        self.correct_answer = question_data['correct_answer']