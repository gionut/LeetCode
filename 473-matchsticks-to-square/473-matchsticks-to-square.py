class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        self.lengthsSum = sum(matchsticks)
        if self.lengthsSum % 4 != 0:
            return False
        
        self.side = self.lengthsSum / 4
        matchsticks.sort(reverse=True)
        
        if  matchsticks[0] > self.side:
            return False
        
        self.matchsticks = matchsticks
        sides = (0, 0, 0, 0)
        return self.rec(sides, 0)
    
    @cache
    def rec(self, sides, matchIndex) -> bool:
        if sum(sides) == self.lengthsSum:
            return True
        
        sides = list(sides)
        match = self.matchsticks[matchIndex]
        for i in range(len(sides)):
            sides[i] += match
            if sides[i] <= self.side and self.rec(tuple(sides), matchIndex+1):
                return True
            sides[i] -= match
            
        return False