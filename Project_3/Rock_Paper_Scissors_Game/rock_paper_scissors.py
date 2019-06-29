import random
import time

moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class Rock_Player(Player):
    # always returns rock
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    # player chooses a move at random
    def move(self):
        return (random.choice(moves))


class ReflectPlayer(Player):
    # remembers what move the opponent played last round, and plays that move
    def move(self, my_move, their_move):
        if their_move == 'rock':
            return 'rock'
        elif their_move == 'paper':
            return 'paper'
        else:
            return 'rock'


class CyclePlayer(Player):
    # remembers what move it played last round, and cycles through the moves
    def move(self, my_move, their_move):
        if my_move == 'rock':
            return 'paper'
        elif my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


class HumanPlayer(Player):
    def move(self):
        # ask the human what move to make
        while True:
            hp_choice = input('Rock, Paper or Scissors? ')
            # If entry error, let them try again
            if hp_choice in moves:
                return hp_choice
            else:
                print('That is not a valid move. Please try again.')


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p1.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f'Player 1: {move1}  Player 2: {move2}')
        time.sleep(1)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print('Player 1 wins!')
            self.p1.score += 1
        elif beats(move2, move1):
            print('Player 2 wins!')
            self.p2.score += 1
        else:
            print("It's a draw!")

    def play_game(self):
        print('Game start!')
        time.sleep(1)
        # choose number of rounds, 1 is an option
        rounds = int(input('How many rounds would you like to play? '))
        time.sleep(1)
        for round in range(rounds):
            print(f'Round: {round}')
            self.play_round()
            # display score after each round
            print('And the scores at the end of that round are...')
            time.sleep(1)
            print(f'Player 1: {self.p1.score}, Player 2: {self.p2.score}')
            time.sleep(1)
            if self.p1.score > self.p2.score:
                print('Player 1 wins!')
            elif self.p2.score > self.p1.score:
                print('Player 2 wins!')
            else:
                print("It's a draw!")
        time.sleep(1)
        # display final scores
        print('The final score is...')
        time.sleep(1)
        print(f'Player 1: {self.p1.score}, Player 2: {self.p2.score}')
        time.sleep(1)
        print('That means, the winner is...drumroll...')
        if self.p1.score > self.p2.score:
            print('Player 1!')
        elif self.p2.score > self.p1.score:
            print('Player 2!')
        time.sleep(1)
        print('Game over!')


if __name__ == '__main__':
    # set the program to play between HumanPlayer and RandomPlayer
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
