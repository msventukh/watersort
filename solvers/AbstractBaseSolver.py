import copy
from abc import ABC, abstractmethod

from game.Container import Container
from solvers.exceptions import SolverStuck


class AbstractBaseSolver(ABC):
    def __init__(self):
        self.history = list()

    @staticmethod
    def hash_containers(containers: list[Container]):
        return '|'.join(map(lambda x: ''.join(x.blocks), containers))

    @abstractmethod
    def choose_move(self, possible_moves: list[tuple[int, int]], containers: list[Container]):
        pass

    @abstractmethod
    def history_size(self):
        pass

    def make_snapshot(self, containers: list[Container]):
        self.history.append(self.hash_containers(containers))
        self.history = self.history[-self.history_size():]

    def is_new_state(self, containers: list[Container]):
        new_hash = self.hash_containers(containers)
        return new_hash not in self.history

    def next_move(self, containers: list[Container]):
        self.make_snapshot(containers)
        size = len(containers)
        possible_moves = list()
        for i in range(size):
            s = containers[i]
            bs = s.show_tail()
            for j in range(size):
                d = containers[j]
                if s != d:
                    bd = d.show_tail()
                    if not (s.is_empty() or s.is_filled_with_same_blocks()) and ((d.has_space() and bs == bd) or d.is_empty()):
                        containers_copy = copy.deepcopy(containers)
                        containers_copy[j].put(containers_copy[i].take())
                        if self.is_new_state(containers_copy):
                            possible_moves.append((i, j))
        if len(possible_moves) == 0:
            raise SolverStuck
        return self.choose_move(possible_moves, containers)
