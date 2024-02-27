class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        EXIT = 1
        ENTER = 0
        
        output = [-1] * n
        toEnter = deque()
        toExit = deque()
        previousMove = EXIT
        same_time = 0
        
        i = 0
        while i < n or toEnter or toExit:
            while i < n and arrival[i] == same_time:
                if state[i] == ENTER:
                    toEnter.append(i) 
                else:
                    toExit.append(i)
                i += 1
            
            if previousMove == EXIT:
                if toExit:
                    output[toExit.popleft()] = same_time
                elif toEnter:
                    output[toEnter.popleft()] = same_time
                    previousMove = ENTER
            
            else:
                if toEnter:
                    output[toEnter.popleft()] = same_time
                elif toExit:
                    output[toExit.popleft()] = same_time
                    previousMove = EXIT
                else:
                    previousMove = EXIT
            same_time += 1
                    
        return output
                
            
                
        