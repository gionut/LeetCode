[4,12,2,7,3,18,20,3,19]
10
2


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        climbs = []
        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb > 0:
                climbs.append((climb, i+1))
        # print(climbs)                
        sorted_climbs = sorted(climbs, key=lambda x: x[0])
        # print(sorted_climbs)
        def is_reachable(i, bricks, ladders):
            for climb in sorted_climbs:
                # print(climb, bricks, ladders)
                if climb[1] > i:
                    continue

                if bricks >= climb[0]:
                    # print("bricks ", climb[0])
                    bricks -= climb[0]
                elif ladders > 0:
                    # print("ladder")
                    ladders -= 1
                else:
                    # print("can't reach")
                    return False
            return True
        
        lo = 0
        hi = len(heights) - 1
        
        while lo < hi:
            mid = lo + (hi - lo + 1)//2
            # print("lo, hi, mid", lo, hi, mid)
            if is_reachable(mid, bricks, ladders):
                lo = mid
                # print("is_reachable", mid)
            else:
                hi = mid - 1 
                # print("is_not_reachable", mid)
        
        return lo
            