import random
import time
from typing import List, Self, Tuple

from gui import Line, Point, Window


class Cell:
    def __init__(
        self,
        has_left_wall: bool,
        has_right_wall: bool,
        has_top_wall: bool,
        has_bottom_wall: bool,
        top_left: Point,
        bottom_right: Point,
        window: Window = None,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.visited = False
        self._x1 = top_left._x
        self._x2 = bottom_right._x
        self._y1 = top_left._y
        self._y2 = bottom_right._y
        self._win = window

    def __repr__(self):
        return f"Cell(left={self.has_left_wall}, right={self.has_right_wall}, top={self.has_top_wall}, bottom={self.has_bottom_wall}, x1={self._x1}, y1={self._y1}, x2={self._x2}, y2={self._y2})"

    def draw(self):
        walls = [
            (
                self.has_left_wall,
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
            ),
            (
                self.has_right_wall,
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
            ),
            (
                self.has_top_wall,
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
            ),
            (
                self.has_bottom_wall,
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
            ),
        ]

        for wall in walls:
            wall_color = "black" if wall[0] else "white"
            self._win.draw_line(wall[1], wall_color)

    def draw_move(self, to_cell: Self, undo: bool = False):
        start_x = (self._x1 + self._x2) / 2
        start_y = (self._y1 + self._y2) / 2
        end_x = (to_cell._x1 + to_cell._x2) / 2
        end_y = (to_cell._y1 + to_cell._y2) / 2
        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        color = "red" if undo else "green"
        line.draw(self._win._canvas, color)


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        if self._seed:
            random.seed(seed)
        self._cells = self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self) -> List[List[Cell]]:
        cells = []
        for row_index in range(self._num_rows):
            row = []
            for col_index in range(self._num_cols):
                x1 = self._x1 + self._cell_size_x * col_index
                x2 = x1 + self._cell_size_x
                y1 = self._y1 + self._cell_size_y * row_index
                y2 = y1 + self._cell_size_y
                cell = Cell(
                    True, True, True, True, Point(x1, y1), Point(x2, y2), self._win
                )
                row.append(cell)
                if self._win:
                    self._draw_cell(cell)
            cells.append(row)

        return cells

    def _draw_cell(self, cell: Cell):
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]

        entrance.has_top_wall = False
        exit.has_bottom_wall = False

        self._draw_cell(entrance)
        self._draw_cell(exit)

    def _break_walls_r(self, row_index: int, col_index: int):
        current_cell = self._cells[row_index][col_index]
        current_cell.visited = True

        while True:
            valid_moves = self._get_valid_moves(row_index, col_index, break_wall=True)

            if not valid_moves:
                self._draw_cell(current_cell)
                return

            move = random.choice(valid_moves)
            move_cell = self._cells[move[0]][move[1]]
            # move left
            if move == (row_index, col_index - 1):
                current_cell.has_left_wall = False
                move_cell.has_right_wall = False
            # move right
            elif move == (row_index, col_index + 1):
                current_cell.has_right_wall = False
                move_cell.has_left_wall = False
            # move down
            elif move == (row_index + 1, col_index):
                current_cell.has_bottom_wall = False
                move_cell.has_top_wall = False
            # move up
            elif move == (row_index - 1, col_index):
                current_cell.has_top_wall = False
                move_cell.has_bottom_wall = False

            self._draw_cell(current_cell)
            self._draw_cell(move_cell)
            self._break_walls_r(move[0], move[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self) -> bool:
        solved = False
        while not solved:
            solved = self._solve_r(0, 0)
        return solved

    def _solve_r(self, row_index: int, col_index: int):
        self._animate()
        current_cell = self._cells[row_index][col_index]
        current_cell.visited = True

        if current_cell == self._cells[-1][-1]:
            return True

        valid_moves = self._get_valid_moves(row_index, col_index)
        random.shuffle(valid_moves)
        for move in valid_moves:
            move_cell = self._cells[move[0]][move[1]]
            current_cell.draw_move(move_cell)
            if self._solve_r(move[0], move[1]):
                return True
            else:
                current_cell.draw_move(move_cell, undo=True)
        return False

    def _get_valid_moves(
        self, row_index: int, col_index: int, break_wall: bool = False
    ) -> List[Tuple[int, int]]:

        up = (
            {
                "row_index": row_index - 1,
                "col_index": col_index,
                "move_cell": self._cells[row_index - 1][col_index],
                "open_from": not self._cells[row_index][col_index].has_top_wall,
                "open_to": not self._cells[row_index - 1][col_index].has_bottom_wall,
            }
            if row_index >= 1
            else None
        )

        down = (
            {
                "row_index": row_index + 1,
                "col_index": col_index,
                "move_cell": self._cells[row_index + 1][col_index],
                "open_from": not self._cells[row_index][col_index].has_bottom_wall,
                "open_to": not self._cells[row_index + 1][col_index].has_top_wall,
            }
            if row_index <= self._num_rows - 2
            else None
        )

        left = (
            {
                "row_index": row_index,
                "col_index": col_index - 1,
                "move_cell": self._cells[row_index][col_index - 1],
                "open_from": not self._cells[row_index][col_index].has_left_wall,
                "open_to": not self._cells[row_index][col_index - 1].has_right_wall,
            }
            if col_index >= 1
            else None
        )

        right = (
            {
                "row_index": row_index,
                "col_index": col_index + 1,
                "move_cell": self._cells[row_index][col_index + 1],
                "open_from": not self._cells[row_index][col_index].has_right_wall,
                "open_to": not self._cells[row_index][col_index + 1].has_left_wall,
            }
            if col_index <= self._num_cols - 2
            else None
        )

        potential_moves = [move for move in [up, down, left, right] if move]
        valid_moves = []
        for move in potential_moves:
            if ((move["open_from"] and move["open_to"]) or break_wall) and (
                not move["move_cell"].visited
            ):
                valid_moves.append((move["row_index"], move["col_index"]))

        return valid_moves
