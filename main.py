# Does Python have block comments or just line comments?  I forget.
# There's some triple-quote thing that stuff I'm reading indicates I shouldn't
# use.  Oh well.  Anyone doing code archaeology will just get to see this.
# Hi code archaeologists.

# from tkinter import Tk, BOTH, Canvas
from graphics import Window
from maze import Maze


# class Window:
# # Renaming these to better match convention (as I see it from Boot.dev) now
# # that I understand better what they are.  I'm not sure the root widget title
# # means or does anything yet.
#     def __init__(self, width, height):
#         self._root = Tk()
#         self._root.title = ("Widget Title 37")
#         self._canvas = Canvas(self._root, height=height, width=width)
#         self._canvas.pack()
#         self.window_running = False
#         self._root.protocol("WM_DELETE_WINDOW", self.close)

# # The rest of the stuff in Window looks fine.  draw_x() functions take an x
# # and draw to the relevant window (canvas), default to black if no color
# # given in second argument.
#     def redraw(self):
#         self._root.update_idletasks()
#         self._root.update()

#     def wait_for_close(self):
#         self.window_running = True
#         while self.window_running:
#             self.redraw()
    
#     def close(self):
#         self.window_running = False

#     def draw_line(self, line, fill_color="black"):
#         line.draw(self._canvas, fill_color)

#     def draw_cell(self, cell, fill_color="black"):
#         cell.draw(fill_color)

# # Renaming self.x to self._x because it seems like that's probably the habit
# # I should be building?  Leads to adding a lot of underscores later.
# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y

# class Line:
#     def __init__(self, point_a, point_b):
#         self._point_a = point_a
#         self._point_b = point_b

# # Brief moment as I wondered where my 'create_line' function was before
# # realizing it was something built-in.
#     def draw(self, canvas, fill_color):
#         canvas.create_line(
#             self._point_a._x,
#             self._point_a._y,
#             self._point_b._x,
#             self._point_b._y,
#             fill=fill_color,
#             width=2)
#             # This list of arguments looks a lot better indented like this.
#         canvas.pack()


# class Cell:
#     # Having win come after x & y was a confusing pain, so now it's first.
#     # On this window, at these points, with these walls ...
#     # That makes sense, right?
#     def __init__(
#         self,
#         win,
#         x1, x2, y1, y2,
#         lw=True, rw=True, tw=True, bw=True
#     ):
#     # Still getting the hang of proper stylistic indendation for trailing
#     # parens in function definitions.  It seems like it doesn't matter where
#     # it actually lands (end of last parameter, indent to match def, indent to
#     # match the variables just below ...).  Also, VS Code automatically made
#     # the next line a comment when it was inside the (), but not just now when
#     # text is outside.  Hrm.
#         self._win = win
#         # Look, I barely care about x and y coords.  I care about points.
#         # Right?  So these are points now.  Top Left, Top Right, Bottom Left,
#         # Bottom Right, Center.  I had to make a little diagram to keep x1, x2,
#         # y1, y2 straight last time.  This way I only need to do that once.
#         self._tl = Point(x1, y1)
#         self._tr = Point(x2, y1)
#         self._bl = Point(x1, y2)
#         self._br = Point(x2, y2)
#         self._c = Point((x1+x2)/2,(y1+y2)/2)
#         # Names from the example are a bit verbose for me.  But only a bit.
#         self.has_left_wall = lw
#         self.has_right_wall = rw
#         self.has_top_wall = tw
#         self.has_bottom_wall = bw

#     # Redoing it as points rather than coords made this cleaner.  Point names
#     # are a bit terse.  self._top_right_corner just seems long.  Also, I hate
#     # underscore-reliant variable naming.
#     def draw(self, fill_color="black"):
#         if self.has_top_wall:
#             topline = Line(self._tl, self._tr)
#             topline.draw(self._win._canvas, fill_color)
#         if self.has_right_wall:
#             rightline = Line(self._tr, self._br)
#             rightline.draw(self._win._canvas, fill_color)
#         if self.has_left_wall:
#             leftline = Line(self._tl, self._bl)
#             leftline.draw(self._win._canvas, fill_color)    
#         if self.has_bottom_wall:
#             bottomline = Line(self._bl, self._br)
#             bottomline.draw(self._win._canvas, fill_color)

#     def draw_move(self, to_cell, undo=False):
#         if undo:
#             color = "gray"
#         else:
#             color = "red"
#         path = Line(self._c, to_cell._c)
#         path.draw(self._win._canvas, color)

# class Maze:
#     def __init__(
#         self,
#         win,
#         x1,
#         y1,
#         num_rows,
#         num_cols,
#         cell_size_x,
#         cell_size_y,
#     ):
#         self._win = win                 # What window are we on
#         self._x1 = x1                   # Horizontal buffer with left edge
#         self._y1 = y1                   # Vertical buffer with top edge
#         self._num_rows = num_rows       # Number of rows of cells
#         self._num_cols = num_cols       # Number of columns of cells
#         self._cell_size_x = cell_size_x # Horizontal size of cells
#         self._cell_size_y = cell_size_y # Vertical size of cells
#         self._create_cells()            # Lastly a call to create these cells.
    
#     # Start with an empty list.  At each spot, append a new empty list and then
#     # go into that new list, start filling it with cells.
#     def _create_cells(self):
#         self._cells = []
#         for i in range(self._num_cols):
#             self._cells.append([])
#             for j in range(self._num_rows):
#                 # This now requires calculating the right cell x & y coords.
#                 # Do corners overlap?  I'm going to let corners overlap.
#                 # So there's horizontal buffer (x1), plus the product of 
#                 # number of cells so far (i) and cell width (cell_size_x).
#                 # Same deal for vertical, except y1, j, cell_size_y.  That gets
#                 # the first (top-left) corner.  Why's it x1, x2, y1, y2, not 
#                 # x1, y1, x2, y2?  Latter's easier.  Whatever, worry later.
#                 # Cell(win, x1+(cellsizex * i), x1+(cellsizex * (i+1))) etc.
#                 self._cells[i].append(Cell(
#                     self._win,
#                     self._x1 + self._cell_size_x * (i),
#                     self._x1 + self._cell_size_x * (i+1),
#                     self._y1 + self._cell_size_y * (j),
#                     self._y1 + self._cell_size_y * (j+1),
#                 ))
#         for i in range(self._num_cols):
#             for j in range(self._num_rows):
#                 # I don't feel like this should be a separate loop but the
#                 # guide is kind of implying it should happen after I the prior
#                 # loop is done.  (Guide doesn't really imply loops, that's me.)
#                 # Try it one way, then the other.
#                 self._draw_cell(i,j)

#     def _draw_cell(self, i, j):
#         # Wait a minute a lot of what this function is supposed to do is
#         # done already.  Unclear what's supposed to be going where here.
#         self._cells[i][j].draw()
#         self._animate()

#     def _animate(self):
#         self._win.redraw()
#         time.sleep(0.05)

# def main():
#     win = Window(800, 600)
#     # point1 = Point(0,0)
#     # point2 = Point(100,100)
#     # point3 = Point(0,100)
#     # point4 = Point(100,0)
#     # diag1 = Line(point1,point2)
#     # lowline = Line(point2, point3)
#     # win.draw_line(lowline)
#     # win.draw_line(diag1,"red")
#     # cell1 = Cell(win,5,105,5,105)
#     # cell2 = Cell(win,50,200,75,300)
#     # cell3 = Cell(win,400,450,400,450, False)
#     # win.draw_cell(cell1)
#     # win.draw_cell(cell2, "red")
#     # win.draw_cell(cell3)
#     # cell1.draw_move(cell2)

#     test= Maze(win,5,5, 10,10, 50,50)
    
#     win.wait_for_close()

# Okay in my grand 'complain about how the guided project is written' thing,
# this is actually a pretty good main() and I should've thought of calculating
# cell size rather than doing it by hand.
def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    # except this, this line was Too Long.
    maze = Maze(
        margin, margin,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win
        )

    win.wait_for_close()

main()