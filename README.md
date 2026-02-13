# MazeWalker

A Python-based maze generator and solver that uses recursive backtracking algorithms to create perfect mazes and visualize the solving process in real-time. Built with Tkinter for graphical visualization and designed with clean, testable code following object-oriented principles.

![MazeWalker Demo](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Procedural Maze Generation**: Uses recursive backtracking (depth-first search) to create perfect mazes where exactly one path exists between any two cells
- **Real-Time Visualization**: Watch both the generation and solving algorithms work step-by-step with smooth animations
- **Smart Pathfinding**: Depth-first search solver with visual backtracking — red lines show exploration, gray lines show dead ends
- **Reproducible Results**: Optional seed parameter ensures the same maze is generated every time for testing and debugging
- **Fully Tested**: Comprehensive unit tests using Python's `unittest` framework
- **Modern Tooling**: Built with `uv` for fast dependency management and development workflow

## How It Works

### Maze Generation Algorithm
The maze starts as a complete grid of cells with all walls intact. Using **recursive backtracking**:
1. Start at the top-left cell and mark it as visited
2. Randomly choose an unvisited neighboring cell
3. Remove the wall between the current cell and chosen cell
4. Recursively visit the chosen cell
5. When no unvisited neighbors exist, backtrack to the previous cell
6. Continue until all cells have been visited

This creates a "perfect maze" — no loops, no isolated areas, and exactly one solution path.

### Maze Solving Algorithm
The solver uses **depth-first search with backtracking**:
1. Start at the entrance (top-left, top wall removed)
2. Mark current cell as visited and draw a red line
3. Try each direction (left, right, up, down) where there's no wall
4. Recursively explore each valid path
5. If a path leads to a dead end, draw a gray "undo" line and try another direction
6. Continue until reaching the exit (bottom-right, bottom wall removed)

The visual result shows red lines tracing the solution path with gray lines indicating explored dead ends.

## How to Run

### Prerequisites
- Python 3.10 or higher
- `tkinter` (usually included with Python)
- `uv` (optional but recommended for package management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/MazeWalker.git
   cd MazeWalker
   ```

2. **Run with uv (recommended):**
   ```bash
   uv run main.py
   ```

   **Or with standard Python:**
   ```bash
   python3 main.py
   ```

### Running Tests

```bash
# With uv
uv run python tests.py

# With standard Python
python3 tests.py
```

## Project Structure

```
mazewalker/
├── graphics.py       # Core graphics primitives (Window, Point, Line, Cell)
├── maze.py          # Maze generation and solving logic
├── main.py          # Entry point and demo configuration
├── tests.py         # Unit tests for maze functionality
├── .gitignore       # Python and environment exclusions
├── pyproject.toml   # Project metadata (uv)
├── .python-version  # Python version pinning
└── README.md        # This file
```

## Customization

### Maze Size and Position

Edit `main.py` to customize the maze:

```python
# Parameters: x, y, num_rows, num_cols, cell_width, cell_height, window, seed
maze = Maze(100, 60, 12, 15, 40, 40, win)

# Explanation:
# - (100, 60): Top-left corner position
# - 12 rows, 15 columns
# - 40x40 pixel cells
# - No seed = random maze each time
```

### Animation Speed

In `maze.py`, adjust the `__animate()` method:

```python
def __animate(self):
    if self.__win is None:
        return
    self.__win.redraw()
    time.sleep(0.05)  # Change this value (0.01 = faster, 0.1 = slower)
```

### Reproducible Mazes

Use a seed for consistent results:

```python
maze = Maze(100, 60, 12, 15, 40, 40, win, seed=42)  # Same maze every time
```

## Technologies Used

- **Python 3.10+**: Core programming language
- **Tkinter**: Built-in GUI library for canvas drawing and window management
- **unittest**: Standard library testing framework
- **uv**: Modern Python package manager (optional)
- **Git/GitHub**: Version control and collaboration

## Code Quality

- **Object-Oriented Design**: Clean separation of concerns (Window, Cell, Maze classes)
- **Testable Architecture**: Window parameter is optional, allowing headless testing
- **Name Mangling**: Private methods use Python's `__method` convention
- **Type Safety**: Clear parameter naming and logical structure
- **DRY Principle**: Reusable components throughout

## Future Improvements

### Algorithm Enhancements
- [ ] Implement **Breadth-First Search (BFS)** for shortest path finding
- [ ] Add **A\* algorithm** with heuristic optimization
- [ ] Compare algorithm performance with timing metrics
- [ ] Support for **Dijkstra's algorithm** visualization

### Visual Improvements
- [ ] Color-coded paths by algorithm type
- [ ] Customizable color schemes (dark mode, high contrast)
- [ ] Variable animation speeds (slow backtracking, fast exploration)
- [ ] Show statistics (path length, cells visited, time elapsed)
- [ ] Add a solution path highlight after completion

### User Experience
- [ ] GUI controls for maze size, speed, and algorithm selection
- [ ] Buttons to generate new maze, solve, reset
- [ ] Manual play mode (user controls movement with arrow keys)
- [ ] Race mode: user vs. algorithm
- [ ] Save/load maze configurations

### Advanced Features
- [ ] Multiple maze generation algorithms (Kruskal's, Prim's, Wilson's)
- [ ] 3D maze visualization
- [ ] Larger mazes with zoom/pan functionality
- [ ] Difficulty levels (more/fewer branches)
- [ ] Maze export to image or text format

## Learning Outcomes

This project demonstrates:
- **Recursive algorithms**: Backtracking for generation and solving
- **Data structures**: 2D grids, visited tracking
- **Graph theory**: DFS traversal, perfect maze properties
- **GUI programming**: Event loops, canvas drawing, animations
- **Software engineering**: Testing, modularity, version control
- **Problem decomposition**: Building complexity incrementally (Fastai/Solveit approach)

## License

MIT License - feel free to use this project for learning, teaching, or building upon!

## Acknowledgments

Built as part of a programming mentorship focusing on problem-solving, algorithmic thinking, and clean code practices. Inspired by classic maze generation techniques and the joy of watching algorithms come to life visually.

---

**Enjoy exploring the maze! 🎯**
