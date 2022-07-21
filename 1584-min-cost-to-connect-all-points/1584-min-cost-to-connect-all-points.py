class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        root = tuple(points[0])
        
        points = set(map(tuple, points))
        
        computeWeight = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        getNeighbours = lambda p1: points - set(p1)
        
        mst = []
        visited = set()
        
        min_cost = 0
        
        min_weight = [(0, (root, root))]
        
        while len(visited) < len(points):
            weight, (source, dest) = heappop(min_weight)
            if dest not in visited:
                min_cost += weight 
                visited.add(dest)
                new_source = dest
                neighbours = getNeighbours(new_source) - visited
                for neighbour in neighbours:
                    weight = (computeWeight(new_source, neighbour), (new_source, neighbour))
                    heappush(min_weight, weight)
        
        return min_cost