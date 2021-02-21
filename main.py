import random

COLORS = {
    '0': '\x1b[0;31;41m  \x1b[0m',
    '1': '\x1b[0;32;42m  \x1b[0m',
    '2': '\x1b[0;33;43m  \x1b[0m',
    '3': '\x1b[0;34;44m  \x1b[0m',
    '4': '\x1b[0;35;45m  \x1b[0m',
    '5': '\x1b[0;36;46m  \x1b[0m',
    '6': '\x1b[0;37;47m  \x1b[0m',
    '7': '\x1b[1;31;40m[]\x1b[0m',
    '8': '\x1b[1;34;40m[]\x1b[0m',
    '9': '\x1b[1;33;40m[]\x1b[0m'
}


class Container:
    def __init__(self, size: int, blocks: list[str]):
        self.head = '|'
        self.blocks = blocks
        self.size = size

    def take(self):
        return self.blocks.pop()

    def put(self, value: str):
        self.blocks.append(value)

    def has_space(self):
        return len(self.blocks) < self.size

    def show_tail(self):
        return self.blocks[len(self.blocks) - 1]

    def is_empty(self):
        return len(self.blocks) == 0

    def contains_same(self):
        return not self.has_space() and all(x == self.show_tail() for x in self.blocks)

    def to_string(self):
        return self.head + ''.join(map(lambda n: COLORS[n], self.blocks))


class ForceQuit(Exception):
    pass


def init(colors: int, layers: int = 4):
    blocks = list(str(x) for x in range(10))[:colors] * layers
    random.shuffle(blocks)
    containers = [Container(layers, blocks[x:x + layers]) for x in range(0, len(blocks), layers)] +\
                 [empty_container(layers), empty_container(layers)]
    turn = 0
    print("Let's get it started!")
    while True:
        if is_victory(containers):
            show_current_state(containers)
            print(f"Congratulations! You won in {turn} moves!")
            break
        if is_defeat(containers):
            show_current_state(containers)
            print("No possible moves. You lost.")
            break
        turn = turn + 1
        try:
            next_turn(containers, turn)
        except ForceQuit:
            print("Bye-bye!")
            break


def next_turn(c: list[Container], n: int):
    print(f"Turn {n}")
    show_current_state(c)
    while True:
        source = check_input("Where to take from?", len(c)) - 1
        dest = check_input("Where to put to?", len(c)) - 1
        if is_possible_move(c[source], c[dest]):
            c[dest].put(c[source].take())
            break
        else:
            print("Impossible move")
    print('')


def is_defeat(containers: list[Container]):
    if any(c.is_empty() for c in containers):
        return False
    tails_with_space = [c.show_tail() for c in containers if c.has_space()]
    if len(tails_with_space) != len(set(tails_with_space)):
        return False
    tails_without_space = [c.show_tail() for c in containers if not c.has_space()]
    return len(set(tails_with_space) & set(tails_without_space)) == 0


def is_victory(containers: list[Container]):
    return all((c.contains_same() or c.is_empty()) for c in containers)


def is_possible_move(source: Container, dest: Container):
    return dest.has_space() and not source.is_empty() and (dest.is_empty() or source.show_tail() == dest.show_tail())


def show_current_state(containers: list[Container]):
    pos = 0
    for c in containers:
        pos = pos + 1
        print(f"{pos}\t{c.to_string()}")


def empty_container(layers: int):
    return Container(layers, [])


def check_input(prompt: str, m: int):
    while True:
        s = input(f"{prompt}\t")
        if s == 'exit':
            raise ForceQuit
        try:
            n = int(s)
            if n <= m:
                return n
            print(f"Please enter a number not bigger then {m}")
        except ValueError:
            print("Please enter a number")


if __name__ == '__main__':
    init(10, 4)
