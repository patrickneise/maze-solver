from gui import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 12, 15, 50, 50, win, 10)
    maze.solve()
    print("SOLVED!!!")
    win.wait_for_close()


main()
