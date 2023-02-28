class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = {}
        for candy in candyType:
            if candy not in types:
                types[candy] = 1
        canEat = len(candyType)//2
        differentTypes = len(types) 
        return canEat if differentTypes > canEat else differentTypes