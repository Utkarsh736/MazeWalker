from graphics import Window, Cell


def main():
    win = Window(800, 600)
    
    # Create a row of cells
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(50, 50, 150, 150)
    
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell2.draw(150, 50, 250, 150)
    
    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.draw(250, 50, 350, 150)
    
    # Draw moves (red path)
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    
    # Create another set showing backtracking
    cell4 = Cell(win)
    cell4.has_bottom_wall = False
    cell4.draw(50, 200, 150, 300)
    
    cell5 = Cell(win)
    cell5.has_top_wall = False
    cell5.has_bottom_wall = False
    cell5.draw(50, 300, 150, 400)
    
    cell6 = Cell(win)
    cell6.has_top_wall = False
    cell6.draw(50, 400, 150, 500)
    
    # Draw path (red) then backtrack (gray)
    cell4.draw_move(cell5)
    cell5.draw_move(cell6)
    cell6.draw_move(cell5, undo=True)  # Backtrack in gray
    
    # Draw a diagonal move
    cell7 = Cell(win)
    cell7.draw(400, 200, 500, 300)
    
    cell8 = Cell(win)
    cell8.draw(550, 350, 650, 450)
    
    cell7.draw_move(cell8)  # Red diagonal line
    
    win.wait_for_close()


main()
