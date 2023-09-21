from cell import Cell
import random
import time

# This one is just wholesale "fine, I guess, whatever." because there's so
# much that's slightly different and based on slightly different initial
# assumptions.  It just throws off my whole sense of what is meant by a guided
# project.  It's a hard needle to thread!  This just feels like insufficient
# guidance given the requirements of later sections.  It felt like a fine
# amount of guidance until I got to parts that relied on those different
# assumptions.
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        directions = ['l', 'r', 'u', 'd']
        if i == 0:
            directions.remove('l')
        if j == 0:
            directions.remove('u')
        if i == self._num_cols - 1:
            directions.remove('r')
        if j == self._num_rows - 1:
            directions.remove('d')
        while True:
            dest = []
            for d in directions:
                if d == 'l' and not self._cells[i-1][j].visited:
                    dest.append([i-1,j])
                if d == 'r' and not self._cells[i+1][j].visited:
                    dest.append([i+1,j])
                if d == 'u' and not self._cells[i][j-1].visited:
                    dest.append([i,j-1])
                if d == 'd' and not self._cells[i][j+1].visited:
                    dest.append([i,j+1])
            if len(dest) == 0:
                self._draw_cell(i, j)
                return
            d = random.randrange(len(dest))
            #dest_i = dest[d][0]
            #dest_j = dest[d][1]
            if dest[d][0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1,j)
            elif dest[d][0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1,j)
            elif dest[d][1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i,j-1)
            elif dest[d][1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i,j+1)
            else:
                print("Weird error.")
    
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False
    
    # This class is getting kind of big.  Like, I'm sure there are huge classes
    # out there in the world, but I'm wondering now about subclasses, ways of
    # keeping individual files small and easily navigable (of course then there
    # is an issue of navigating collections of files ...)
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        neighbors = []
        # Left
        if (
            i > 0 and
            not (
                self._cells[i][j].has_left_wall or
                self._cells[i-1][j].visited
            )
        ):
            neighbors.append([i-1,j])
        # right
        if (
            i < self._num_cols-1 and
            not (
                self._cells[i][j].has_right_wall or
                self._cells[i+1][j].visited
            )
        ):
            neighbors.append([i+1,j])
        # Up
        if (
            j > 0 and
            not (
                self._cells[i][j].has_top_wall or
                self._cells[i][j-1].visited
            )
        ):
            neighbors.append([i,j-1])
        # Down
        if (
            j < self._num_rows-1 and
            not (
                self._cells[i][j].has_bottom_wall or
                self._cells[i][j+1].visited
            )
        ):
            neighbors.append([i,j+1])
        for n in neighbors:
            self._cells[i][j].draw_move(
                self._cells[n[0]][n[1]]
            )
            if self._solve_r(n[0],n[1]):
                return True
            self._cells[i][j].draw_move(
                self._cells[n[0]][n[1]], True
            )
        return False