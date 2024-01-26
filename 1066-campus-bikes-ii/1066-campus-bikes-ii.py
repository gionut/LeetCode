class Solution:    
    min_dist = -1
    
    def dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def f(self, workers, bikes, visited, curr_dist):
        if self.min_dist != -1 and curr_dist >= self.min_dist:
            return
        if len(workers) == 0:
            if self.min_dist == -1 or curr_dist < self.min_dist:
                self.min_dist = curr_dist
            return
        
        for bike_idx in range(len(bikes)):
            if visited[bike_idx] == 0:
                visited[bike_idx] = 1
                self.f(workers[1:], bikes, visited, curr_dist + self.dist(workers[0], bikes[bike_idx]))
                visited[bike_idx] = 0
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        visited = [0] * len(bikes)
        self.f(workers, bikes, visited, 0)
        return self.min_dist