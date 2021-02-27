import argparse

from game.Container import Container
from game.ForceQuit import ForceQuit
from game.Game import Status, Game

OUTPUT = {
    Status.victory: 'Congratulations! You won!',
    Status.defeat: 'No possible moves. You lost.',
    Status.exit: 'Bye-bye!'
}


def start_game(colors: int, layers: int):
    game = Game(colors, layers)
    turn = 1
    print("Let's get it started!")
    while True:
        print(f"Turn {turn}")
        show_current_state(game.containers)
        while True:
            try:
                source = check_input("Where to take from?") - 1
                dest = check_input("Where to put to?") - 1
            except ForceQuit:
                result = Status.exit
                break
            result = game.next_turn(source, dest)
            if result != Status.impossible:
                break
            print("Impossible move")
        if result != Status.next:
            break
        turn = turn + 1
        print("")
    show_current_state(game.containers)
    end_game(result, turn)


def end_game(result: Status, turns: int):
    print("")
    print(OUTPUT[result])
    print(f"The game has finished after {turns} turn(s)")


def show_current_state(containers: list[Container]):
    pos = 0
    for c in containers:
        pos = pos + 1
        print(f"{pos}\t{c.to_string()}")


def check_input(prompt: str):
    while True:
        s = input(f"{prompt}\t")
        if s == 'exit':
            raise ForceQuit
        try:
            return int(s)
        except ValueError:
            print("Please enter a number")


def check_colors(value):
    return check_int_range(value, 2, 10, "colors")


def check_layers(value):
    return check_int_range(value, 2, 100, "layers")


def check_int_range(v: int, min_value: int, max_value: int, name: str):
    value = int(v)
    if value < min_value or value > max_value:
        raise argparse.ArgumentTypeError(f"{value} is an invalid number of {name} (must be between {min_value} "
                                         f"and {max_value})")
    return value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--colors", help="Number of different colors [2..10]", type=check_colors, default=6)
    parser.add_argument("-l", "--layers", help="Number of layers in a single container [2..100]", type=check_layers,
                        default=4)
    args = parser.parse_args()
    start_game(args.colors, args.layers)
