# output = []
# toEnter = []
# toExit = []
# at each time:
#     who wants to enter: crt time + toEnter
#     who wants to exit: crt time + toExit
#     what was the previous move
#     who has priority
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        EXIT = 1
        ENTER = 0
        
        output = [-1] * n
        toEnter = []
        toExit = []
        previousMove = EXIT
        same_time = 0
        
        i = 0
        while i < n or toEnter or toExit:
            while i < n and arrival[i] == same_time:
                if state[i] == ENTER:
                    heapq.heappush(toEnter, i) 
                else:
                    heapq.heappush(toExit, i)
                i += 1
            
            # print(toEnter, toExit)
            
            if previousMove == EXIT:
                if toExit:
                    output[heapq.heappop(toExit)] = same_time
                elif toEnter:
                    output[heapq.heappop(toEnter)] = same_time
                    previousMove = ENTER
            
            else:
                if toEnter:
                    output[heapq.heappop(toEnter)] = same_time
                elif toExit:
                    output[heapq.heappop(toExit)] = same_time
                    previousMove = EXIT
                else:
                    previousMove = EXIT
            same_time += 1
                    
        return output
                
            
                
        