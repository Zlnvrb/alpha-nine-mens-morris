import random

from ninemensmorris.NineMensMorrisLogic import Board


def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


def input_to_valid_move_form(given_input):
    input_split = given_input.split(" ")
    return to_correct_type(
        input_split[0]), to_correct_type(input_split[1]), to_correct_type(input_split[2])


def to_correct_type(value):
    try:
        return int(value)
    except:
        return None


class RandomPlayer():
    """
    Chooses random moves from all possible moves from board state.
    """
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valid_moves_vector, moves, _ = self.game.getValidMovesAsTuple(board, 1)
        # print(f"Valid moves: {moves}")
        indices = find_indices(valid_moves_vector, 1)
        a = random.choice(indices)
        return a


class GreedyNineMensMorrisPlayer():
    """
    Chooses a move by the following criteria, in the specified order:
    1. if a move exists, such that a mill will be formed for this player - choose that.
    2. if a move exists, such that a mill will be formed for the opponent - choose that to block.
    3. if by the previous criteria a move was not chosen, choose at random.
    """
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valid_moves_vector, valid_moves, all_moves = self.game.getValidMovesAsTuple(board, 1)
        b = Board(board)
        mills = b.get_possible_mills(valid_moves, 1)
        mills_for_opponent = b.get_possible_mills(valid_moves, -1)

        if mills:
            move = mills[0]
        elif mills_for_opponent:
            move = mills_for_opponent[0]
        else:
            move = random.choice(valid_moves)
        return all_moves.index(move)

class HumanNineMensMorrisPlayer():
    """
    Takes input from the terminal.
    """
    def __init__(self, game, show_valid_moves):
        self.game = game
        self.show_valid_moves = show_valid_moves

    def play(self, board):

        while True:
            valid_moves_vector, valid_moves, all_moves = self.game.getValidMovesAsTuple(board, 1)
            if self.show_valid_moves:
                print(f"Valid moves: {valid_moves}")

            user_input = input()
            move = input_to_valid_move_form(user_input)

            if move in all_moves:
                break
            else:
                print('This input is invalid.')

        # Return index of move
        return all_moves.index(move)
