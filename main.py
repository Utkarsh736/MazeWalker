from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    
    # 15 cols x 12 rows, 40px cells
    # Creates a 600x480 maze centered with 100px, 60px margins
    maze = Maze(100, 60, 12, 15, 40, 40, win)
    
    win.wait_for_close()


main()
