class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        computeWeight = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        ans, n = 0, len(p)
        seen = set()
        vertices = [(0, (0, 0))]

        while len(seen) < n:
            # print(vertices, seen)
            w, (u, v) = heapq.heappop(vertices)            
            if v in seen: continue
            ans += w
            seen.add(v)
            for j in range(n):
                if j not in seen and j!=v:
                    heapq.heappush(vertices, (computeWeight(p[j], p[v]), (v, j)))
        
        return ans
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
        
