from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    
    # No seed = different maze every time!
    maze = Maze(100, 60, 12, 15, 40, 40, win)
    
    win.wait_for_close()


main()
