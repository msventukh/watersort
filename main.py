from game.Container import Container
from game.ForceQuit import ForceQuit
from game.Game import Status, Game

OUTPUT = {
    Status.victory: 'Congratulations! You won!',
    Status.defeat: 'No possible moves. You lost.',
    Status.exit: 'Bye-bye!'
}


def start_game(colors: int, layers: int = 4):
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


if __name__ == '__main__':
    start_game(10, 4)
