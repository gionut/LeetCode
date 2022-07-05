
int candy(int* ratings, int ratingsSize) {
    if(ratingsSize == 1) return 1;
    
    int candies = 0;
    int candiesToLastChild = 0;
    int current = 0;
    while(current < ratingsSize-1) {
        int terrain = ratings[current+1] - ratings[current];
        int steps = stepsUntilChangeInTerrain(ratings, ratingsSize, current, terrain);
        current += steps-1; // elliminate the last step, since it will be used in the next iteration
        
        if(isPlateau(terrain)) {
            candies += steps - min(candiesToLastChild, 1);
            candiesToLastChild = 1;
        }
        else {
            candies += (steps+1)*steps/2 - min(candiesToLastChild, steps);
            candiesToLastChild = isAscending(terrain)? steps: 1;
        }
    }
    return candies;
}

int stepsUntilChangeInTerrain(int* array, int arraySize, int startingPosition, int terrain) {
    int steps = 1;
    int currentPosition = startingPosition+1;
    while(currentPosition < arraySize){
        int currentTerrain = array[currentPosition] - array[currentPosition-1];
        if(!((terrain == currentTerrain) && (terrain == 0) 
             || terrain*currentTerrain > 0))
            break;
        currentPosition++;
        steps++;
    }
    
    return steps;
}

int isPlateau(terrain) {
    return terrain == 0;
}

int isAscending(terrain) {
    return terrain > 0;
}

int min(int a, int b) {
    return a <= b? a: b; 
}