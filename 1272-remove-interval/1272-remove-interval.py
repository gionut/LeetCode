
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        def isOutside(interval1, interval2):
            return interval2[1] <= interval1[0] or \
        interval1[1] <= interval2[0]
        
        def isInside(interval1, interval2):
            return interval1[0] < interval2[0] < interval2[1] < interval1[1]
        
        def isBoundedRight(interval1, interval2):
            return interval1[0] < interval2[0] < interval1[1] <= interval2[1]
        
        def isBoundedLeft(interval1, interval2):
            return interval2[0] <= interval1[0] < interval2[1] < interval1[1]
        
        result = []
        for interval in intervals:
            if isOutside(interval, toBeRemoved):
                result.append(interval)

            elif isInside(interval, toBeRemoved):
                result.append([interval[0], toBeRemoved[1]-1])
                result.append([toBeRemoved[1], interval[1]])

            elif isBoundedRight(interval, toBeRemoved):
                result.append([interval[0], toBeRemoved[0]])

            elif isBoundedLeft(interval, toBeRemoved):
                result.append([toBeRemoved[1], interval[1]])

        
        return result