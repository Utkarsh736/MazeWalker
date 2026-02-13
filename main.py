from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    
    # Draw an X across the window
    line1 = Line(Point(0, 0), Point(800, 600))
    win.draw_line(line1, "black")
    
    line2 = Line(Point(800, 0), Point(0, 600))
    win.draw_line(line2, "red")
    
    # Draw a triangle
    line3 = Line(Point(400, 100), Point(200, 400))
    win.draw_line(line3, "blue")
    
    line4 = Line(Point(200, 400), Point(600, 400))
    win.draw_line(line4, "green")
    
    line5 = Line(Point(600, 400), Point(400, 100))
    win.draw_line(line5, "purple")
    
    win.wait_for_close()


main()
