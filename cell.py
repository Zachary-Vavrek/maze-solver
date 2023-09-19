from graphics import Line, Point

# I don't like the idea of a cell just sort of existing without location.
# The project example cell doesn't have a location until it's drawn.  That's
# weird, right?  I'm not sure how to run tests ... I mean, at all, really.

# So I guess I'll just follow the example here?

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    # Just such a strong feeling of "I don't like how this is being done here,
    # but I don't think it matters that much."  I'd rather be napping.
    # So I'm just copying over the example code for the parts of the Cell
    # class which I'd already made.

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    # But the example's draw_move is ... what?  Why're you doing that, dude?
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        start_pt = Point(
            (self._x1 + self._x2) / 2,
            (self._y1 + self._y2) / 2
            )
        end_pt = Point(
            (to_cell._x1 + to_cell._x2) / 2,
            (to_cell._y1 + to_cell._y2) / 2
            )
        fill_color = "red"
        if undo:
            fill_color = "gray"
        linemove = Line(start_pt, end_pt)
        self._win.draw_line(linemove, fill_color)
        