class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.EXPLORED = -1
        self.grid = grid
        
        maxArea = 0
                
        for row, rowCells in enumerate(grid):
            for col, cell in enumerate(rowCells):
                if cell == 1:
                    area = self.bfs(row, col)
                    
                    if area > maxArea:
                        maxArea = area
        
        return maxArea
                    
    def bfs(self, row, col):
        def inGrid(cell):
            row, col = cell
            return row >= 0 and row < len(self.grid) and col >= 0 and col < len(self.grid[row])
            
        def isUnexplored(cell):
            row, col = cell
            return not self.grid[row][col] == self.EXPLORED
        
        def isLand(cell):
            row, col = cell
            return self.grid[row][col] == 1
        
        area = 0
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        stack = deque()
        stack.append((row, col))
        
        while len(stack):
            row, col = stack.pop()
            
            if isUnexplored((row, col)):            
                self.grid[row][col] = self.EXPLORED
                area += 1
                
                for stepRow, stepCol in directions:
                    neighbour = (row + stepRow,  col + stepCol)
                    if inGrid(neighbour) and isLand(neighbour) and isUnexplored(neighbour):
                        stack.append(neighbour)
        
        return area