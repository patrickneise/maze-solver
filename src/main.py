from gui import Window
from maze import Maze


def main():
    # size of the application window
    WINDOW_X = 800
    WINDOW_Y = 600
    # size of the maze
    NUM_ROWS = 10
    NUM_COLS = 10
    # location of maze in window
    ORIGIN_X = 0
    ORIGN_Y = 0
    # size of cells
    CELL_WIDTH = 50
    CELL_HEIGHT = 50

    win = Window(WINDOW_X, WINDOW_Y)
    maze = Maze(ORIGIN_X, ORIGN_Y, NUM_ROWS, NUM_COLS, CELL_WIDTH, CELL_HEIGHT, win)
    maze.solve()
    win.wait_for_close()


main()
