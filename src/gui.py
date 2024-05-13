from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"Point(x={self._x}, y={self._y})"


class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self._point_1 = point_1
        self._point_2 = point_2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self._point_1._x,
            self._point_1._y,
            self._point_2._x,
            self._point_2._y,
            fill=fill_color,
            width=2,
        )

    def __repr__(self):
        return f"Line({self._point_1}, {self._point_2})"


class Window:
    def __init__(self, width: int, height: int):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self._canvas, fill_color)
