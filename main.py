from graphics import Window, Cell


def main():
    win = Window(800, 600)
    
    # Cell with all walls (default)
    cell1 = Cell(win)
    cell1.draw(50, 50, 150, 150)
    
    # Cell with no left wall
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(200, 50, 300, 150)
    
    # Cell with no top wall
    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.draw(350, 50, 450, 150)
    
    # Cell with only left and top walls (corridor corner)
    cell4 = Cell(win)
    cell4.has_right_wall = False
    cell4.has_bottom_wall = False
    cell4.draw(50, 200, 150, 300)
    
    # Cell with no walls (completely open)
    cell5 = Cell(win)
    cell5.has_left_wall = False
    cell5.has_right_wall = False
    cell5.has_top_wall = False
    cell5.has_bottom_wall = False
    cell5.draw(200, 200, 300, 300)
    
    # Large cell with only right and bottom walls
    cell6 = Cell(win)
    cell6.has_left_wall = False
    cell6.has_top_wall = False
    cell6.draw(350, 200, 500, 350)
    
    win.wait_for_close()


main()
