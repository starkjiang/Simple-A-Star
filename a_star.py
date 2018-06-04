import heapq

class Cell(object):
    def __init__(self, x, y, movable):
        """We have to initialize new cell

        x: cell x coordinate
        y: cell y coordinate
        r: the cost to move from any starting cell to this cell
        v: estimation of the cost to move from this cell to the
           terminal cell
        q: q = r + v
        """

        self.movable = movable
        self.x = x
        self.y = y
        self.parent = None
        self.r = 0
        self.v = 0
        self.q = 0


class Astar(object):
    def __init__(self):
        # open list
        self.open = []
        heapq.heapify(self.open)
        # visited cells list
        self.visited = set()
        # 2D grid cells
        self.cells = []
        self.grid_height = None
        self.grid_width = None

    def init_grid(self, width, height, obstacles, start, terminal):
        """Obtain grid open cells, obstacles



        width: 2D grid's width
        height: 2D grid's height
        obstacles: list of obstacle x, y tuples
        start: grid starting point x, y tuples
        terminal: grid terminal point x, y tuples
        """

        self.grid_height = height
        self.grid_width = width
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in obstacles:
                    movable = False
                else:
                    movable = True

                    self.cells.append(Cell(x, y, movable))
        self.start = self.get_cell(*start)
        self.terminal = self.get_cell(*terminal)

    def get_heuristic(self, cell):
        """Calculate the heuristic value v for a cell



        Distance between this cell and the terminal cell multiplied by 1
        (In this case, diagonal moving is not used due to its larger cost)
        We use Manhattan norm as the heuristic function

        return heuristic value v
        """


        return 1 * (abs(cell.x - self.terminal.x) + abs(cell.y - self.terminal.y))

    def get_cell(self, x, y):
        """Return a cell from the cells list



        x: cell x coordinate
        y: cell y coordinate
        return: cell
        """

        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell):
        """Return adjacent cells to a cell


        Clockwise starting from the one on the right

        cell: get adjacent cells
        return: adjacent cells list
        """

        cells = []
        if cell.x < self.grid_width-1:
            cells.append(self.get_cell(cell.x+1, cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y-1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1, cell.y))
        if cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x, cell.y+1))
        return cells

    def get_path(self):
        cell = self.terminal
        path = [(cell.x, cell.y)]
        while cell.parent is not self.start:
            cell = cell.parent
            path.append((cell.x, cell.y))

        path.append((self.start.x, self.start.y))
        path.reverse()
        return path

    def update_cell(self, adj, cell):
        """Update adjacent cell


        adj: adjacent cell to current cell
        cell: current cell being processed
        """

        adj.r = adj.r + 1
        adj.v = self.get_heuristic(adj)
        adj.parent = cell
        adj.q = adj.r + adj.v

    def solve(self):
        """Solve 2D grids, find path to the terminal cell

        returns path or None if not found
        """

        # Add starting cell to open heap queue
        heapq.heappush(self.open, (self.start.q, self.start))
        while len(self.open):
            # pop cell from heap queue
            q, cell = heapq.heappop(self.open)
            # add cell to obstacle list such that we don't have to use it twice times
            self.visited.add(cell)
            # if terminal cell, return path found
            if cell is self.terminal:
                return self.get_path()
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.movable and adj_cell not in self.visited:
                    if (adj_cell.q, adj_cell) in self.open:
                        # if adjacent cell is in the open list, check if current path
                        # is better than the previous one
                        if adj_cell.r > cell.r + 1:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        # add adjacent cell to the open list
                        heapq.heappush(self.open, (adj_cell.q, cell))
