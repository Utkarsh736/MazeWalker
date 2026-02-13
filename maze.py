import random
from graphics import Cell
import time


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
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        
        # Seed random number generator for reproducible mazes
        if seed is not None:
            random.seed(seed)
        
        self.__cells = []
        
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)  # Start from top-left


    
    def __create_cells(self):
        # Create columns (i)
        for i in range(self.__num_cols):
            col = []
            # Create rows (j) in each column
            for j in range(self.__num_rows):
                col.append(Cell(self.__win))
            self.__cells.append(col)
        
        # Draw all cells
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        # Calculate position based on grid coordinates
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        
        # Draw the cell (will handle None window internally)
        self.__cells[i][j].draw(x1, y1, x2, y2)
        
        # Animate the drawing
        self.__animate()
    
    def __animate(self):
        # Only animate if window exists
        if self.__win is None:
            return
        
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        # Break entrance (top wall of top-left cell)
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        
        # Break exit (bottom wall of bottom-right cell)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        # Mark current cell as visited
        self.__cells[i][j].visited = True
        
        # Loop until we've explored all directions
        while True:
            # List to store unvisited adjacent cells
            to_visit = []
            
            # Check left neighbor (i-1, j)
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            
            # Check right neighbor (i+1, j)
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            
            # Check up neighbor (i, j-1)
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            
            # Check down neighbor (i, j+1)
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            
            # If no unvisited neighbors, we're done (backtrack)
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            
            # Pick a random direction
            next_i, next_j = to_visit[random.randrange(len(to_visit))]
            
            # Knock down walls between current and chosen cell
            # Moving right
            if next_i == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False
            # Moving left
            elif next_i == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False
            # Moving down
            elif next_j == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False
            # Moving up
            elif next_j == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False
            
            # Recursively visit the chosen cell
            self.__break_walls_r(next_i, next_j)

