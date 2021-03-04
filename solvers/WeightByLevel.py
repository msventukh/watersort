from game.Container import Container
from solvers.AbstractBaseSolver import AbstractBaseSolver


class WeightByLevel(AbstractBaseSolver):
    def history_size(self):
        return 3

    def choose_move(self, possible_moves: list[tuple[int, int]], containers: list[Container]):
        move = possible_moves[0]
        size = containers[0].size
        max_weight = -size
        for i, j in possible_moves:
            weight = self.calculate_weight(containers[i], containers[j], size)
            if weight > max_weight:
                move = (i, j)
                max_weight = weight
        return move

    @staticmethod
    def calculate_weight(src: Container, dest: Container, size: int):
        m = 2 if src.contains_same() else 1
        return size + len(dest.blocks) - m * len(src.blocks)

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_string():
        return "Weight by level"
