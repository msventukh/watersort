import random

from game.Container import Container
from solvers.AbstractBaseSolver import AbstractBaseSolver


class RandomMove(AbstractBaseSolver):
    def history_size(self):
        return 5

    def choose_move(self, possible_moves: list[tuple[int, int]], containers: list[Container]):
        number_of_options = len(possible_moves)
        return possible_moves[random.randint(0, number_of_options - 1)]

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_string():
        return "Random move"
