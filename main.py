from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    
    # Create maze with seed for reproducible testing
    maze = Maze(100, 60, 12, 15, 40, 40, win, seed=0)
    
    # Solve the maze!
    is_solveable = maze.solve()
    
    if is_solveable:
        print("Maze solved! 🎉")
    else:
        print("Maze cannot be solved 😢")
    
    win.wait_for_close()


main()
