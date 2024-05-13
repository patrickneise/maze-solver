import unittest

from maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_create_cells_10_12_square(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_create_cells_12_10_rectangle(self):
        num_rows = 12
        num_cols = 10
        m1 = Maze(0, 0, num_rows, num_cols, 20, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_create_cells_10_12_square_offset(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)


if __name__ == "__main__":
    unittest.main()
