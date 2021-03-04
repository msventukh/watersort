import random
from enum import Enum
from game.Container import Container

Status = Enum('GameEnding', 'victory defeat exit next impossible')


class Game:
    def __init__(self, colors: int, layers: int = 4, rnd_init_value=None):
        while True:
            blocks = list(str(x) for x in range(10))[:colors] * layers
            if rnd_init_value is None:
                rnd_init_value = random.random()
                print(f"Initial random value is {rnd_init_value}")

            def randomizer(): return rnd_init_value
            random.shuffle(blocks, random=randomizer)
            self.containers = [Container(layers, blocks[x:x + layers]) for x in range(0, len(blocks), layers)] + \
                              [Container.create_empty(layers), Container.create_empty(layers)]
            if not self.is_defeat() and not self.is_victory():
                break

    def is_defeat(self):
        if any(c.is_empty() for c in self.containers):
            return False
        tails_with_space = [c.show_tail() for c in self.containers if c.has_space()]
        if len(tails_with_space) != len(set(tails_with_space)):
            return False
        tails_without_space = [c.show_tail() for c in self.containers if not c.has_space()]
        return len(set(tails_with_space) & set(tails_without_space)) == 0

    def is_victory(self):
        return all((c.contains_same() or c.is_empty()) for c in self.containers)

    def next_turn(self, source: int, dest: int):
        if self.is_possible_move(source, dest):
            self.containers[dest].put(self.containers[source].take())
            if self.is_victory():
                return Status.victory
            if self.is_defeat():
                return Status.defeat
            return Status.next
        else:
            return Status.impossible

    def is_possible_move(self, source: int, dest: int):
        try:
            s = self.containers[source]
            d = self.containers[dest]
        except IndexError:
            return False
        return d.has_space() and not s.is_empty() and (d.is_empty() or s.show_tail() == d.show_tail())
