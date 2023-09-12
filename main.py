from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title = ("Widget Title 37")
        self.tabula = Canvas(self.__root_widget, height=height, width=width)
        self.tabula.pack()
        self.window_running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()
    
    def close(self):
        self.window_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.tabula, fill_color)

    def draw_cell(self, cell, fill_color="black"):
        cell.draw(self.tabula, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x,
        self.point_b.y, fill=fill_color, width=2)
        canvas.pack()

class Cell:
    def __init__(self, x1, x2, y1, y2, win, lw=True, rw=True, tw=True, bw=True):
        self.has_left_wall = lw
        self.has_right_wall = rw
        self.has_top_wall = tw
        self.has_bottom_wall = bw
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self._c = Point((x1+x2)/2,(y1+y2)/2)

    def draw(self, canvas, fill_color="black"):
        if self.has_top_wall:
            topline = Line(Point(self._x1, self._y1),
                           Point(self._x2, self._y1))
            topline.draw(canvas, fill_color)
        if self.has_right_wall:
            rightline = Line(Point(self._x2, self._y1),
                             Point(self._x2, self._y2))
            rightline.draw(canvas, fill_color)
        if self.has_left_wall:
            leftline = Line(Point(self._x1, self._y1),
                            Point(self._x1, self._y2))
            leftline.draw(canvas, fill_color)    
        if self.has_bottom_wall:
            bottomline = Line(Point(self._x1, self._y2),
                              Point(self._x2, self._y2))
            bottomline.draw(canvas, fill_color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        path = Line(self._c, to_cell._c)
        path.draw(self._win.tabula, color)

def main():
    win = Window(800, 600)
    # point1 = Point(0,0)
    # point2 = Point(100,100)
    # point3 = Point(0,100)
    # point4 = Point(100,0)
    # diag1 = Line(point1,point2)
    # lowline = Line(point2, point3)
    # win.draw_line(lowline)
    # win.draw_line(diag1,"red")
    cell1 = Cell(5,105,5,105,win)
    cell2 = Cell(50,200,75,300,win)
    cell3 = Cell(400,450,400,450,win, False)
    win.draw_cell(cell1)
    win.draw_cell(cell2, "red")
    win.draw_cell(cell3)
    cell1.draw_move(cell2)
    
    win.wait_for_close()

main()