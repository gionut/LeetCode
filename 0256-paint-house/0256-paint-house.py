# [[17,17,2],[16,16,5],[14,3,19]]

# ('r', 2, 14)
# ('b', 2, 3)
# ('g', 2, 19)

# ('r', 1, 16 + 3 = 19)
# ('b', 1, 16 + 14 = 30)
# ('g', 1, 5 + 3 = 8)

# ('r', 0, 17 + 8 = 25)
# ('b', 0, 17 + 8 = 25)
# ('g', 0, 2 + 19 = 21)

# paint_cost = [0, 0 ,0]
# start from last house until the first one
# compute paint_cost
#     prev_paint_cost
#     for each color:
#         paint_cost[color] = costs[house][color] + min(prev_paint_cost[color+1%3], prev_paint_cost[color+2%3]) 

# return min_paint_color


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev_paint_cost = [0, 0, 0]
        paint_cost = [0, 0, 0]
        
        house = len(costs) - 1
        while house >= 0:
            
            for color in range(3):
                paint_cost[color] = costs[house][color] + \
                    min(prev_paint_cost[(color+1)%3], prev_paint_cost[(color+2)%3])
            
            prev_paint_cost = list(paint_cost)
            
            house = house - 1
            
        return min(paint_cost)