class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        visited = set()
        heap = [(0, (0, 0))]
        
        min_cost = 0        

        while len(heap):
            cost, (src, dest) = heappop(heap)            
            
            if dest not in visited:
                visited.add(dest)
                min_cost += cost
                
                for neighbour in range(len(points)):
                    if neighbour not in visited and neighbour != dest:
                        heappush(heap, (manhattan(points[dest], points[neighbour]), (dest, neighbour)))
        
        return min_cost
#         computeWeight = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
#         getNeighbours = lambda p1: [p for p in range(len(points)) if p != p1 and p not in visited]
        
#         weights = []
#         for i in range(len(points)):
#             for j in range(i+1, len(points)):
#                 weight = computeWeight(points[i], points[j]) 
#                 weights[i] = weight
#                 weights[j][i] = weight
                
#         visited = set()

#         min_cost = 0
        
#         min_weight = [(0, (0, 0))]
        
#         while len(min_weight):
#             weight, (src, dest) = heappop(min_weight)
#             if dest not in visited:
#                 min_cost += weight 
#                 visited.add(dest)
#                 src = dest
#                 for dest in range(len(points)):
#                     if dest != src and dest not in visited:
#                         edge = (src, dest)
#                         weight = (weights[edge], edge)
#                         heappush(min_weight, weight)
        
#         return min_cost
        
