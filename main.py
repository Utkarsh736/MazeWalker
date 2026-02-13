from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        # Create root widget (the main window)
        self.__root = Tk()
        self.__root.title("MazeWalker")
        
        # Create canvas - the drawing surface
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        
        # Track if window is running
        self.__running = False
        
        # Connect close button to our close method
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        # Update the GUI - refresh all graphics
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        # Keep window alive and responsive
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        # Stop the main loop
        self.__running = False


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()
