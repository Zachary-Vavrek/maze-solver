from tkinter import Tk, BOTH, Canvas

# Rearranging files to better match guided project expectations.
# Having stuff not all just sit in main dot whatever is good practice, but the
# project being under-specified yet requiring certain things is awkward.

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = ("How come it's a house of leaves?")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # I still don't know what the title is used for.
        self.__canvas = Canvas(
            self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        # I'm copying and pasting some of this from the project example because
        # it's boilerplate that I don't feel like retyping.

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

# Example has draw_line as part of the window class, but not draw_cell.
# The issue is that lines don't know what canvas they're on, but need to for
# being drawn.

# You know, I have this punchcard-influenced 80 character limit here, but I'm
# not sure what limit I should use for max lines before I realize a file is too
# complex.  Also 80?  A hundred?  Do I count comments?

# I think I'm worrying too much about this guided project and should worry more
# about the unguided personal project that comes after.  It's just annoying.
# (And so I write comments to vent.)

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
    # It's such a basic little function.  I guess it's done this way because
    # the canvas is a private variable?  Yeah, looking at the cell class, both
    # mine and the example, it's just a bunch of calls through .draw_line.

# Points and lines, that's what's left.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # I guess ... whoever put this together (Lane?) didn't want those
        # to be weird quasi-hidden variables.

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            fill=fill_color, width=2
        )
        canvas.pack()
