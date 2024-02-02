class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) == 1:
            return []
        validMoves = []
        
        step = 1
        while step < len(currentState):
            if currentState[step] == "+" and \
            currentState[step-1] == currentState[step]:
                newState = currentState[:step-1] + "--" + \
                currentState[step + 1:]
                    
                validMoves.append(newState)
            step+=1
        
        return validMoves