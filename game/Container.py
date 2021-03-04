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

    @staticmethod
    def create_empty(layers: int):
        return Container(layers, [])

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
        if self.is_empty():
            return None
        return self.blocks[len(self.blocks) - 1]

    def is_empty(self):
        return len(self.blocks) == 0

    def is_filled_with_same_blocks(self):
        return not self.has_space() and self.contains_same()

    def contains_same(self):
        return all(x == self.show_tail() for x in self.blocks)

    def to_string(self):
        return self.head + ''.join(map(lambda n: COLORS[n], self.blocks))
