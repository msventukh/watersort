from game.Container import Container
from solvers.AbstractBaseSolver import AbstractBaseSolver


class FirstPossibleMove(AbstractBaseSolver):
    def history_size(self):
        return 100

    def choose_move(self, possible_moves: list[tuple[int, int]], containers: list[Container]):
        return possible_moves[0]

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_string():
        return "First possible move"
