#define EXPLORED 0;

struct Island{
    int** grid;
    int gridSize;
    int* gridColSize;
};

int isLand(struct Island* island, int row, int col) {
    return row >= 0 && row < island->gridSize &&
        col >= 0  && col < island->gridColSize[row];
}

int isUnexploredLand(struct Island* island, int row, int col) {
    return isLand(island, row, col) && island->grid[row][col] != EXPLORED;
}

int explore(struct Island* island, int row, int col) {
    if (isUnexploredLand(island, row, col)) {
        island->grid[row][col] = EXPLORED;
        
        return 1 + explore(island, row-1, col) + explore(island, row, col-1) +
            explore(island, row+1, col) + explore(island, row, col+1);
    }
    return 0;
}

int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize){
    struct Island island;
    island.grid = grid;
    island.gridSize = gridSize;
    island.gridColSize = gridColSize;
    
    int maxArea = 0;
    for(int row = 0; row < gridSize; row++) 
        for(int col = 0; col < gridColSize[row]; col++) {
           if (isLand(&island, row, col)) {
               int area = explore(&island, row, col);
               if(area > maxArea)
                   maxArea = area;
           }
        }
    
    return maxArea;
}

