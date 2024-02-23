class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [{} for i in range(n)]
        for (from_i, to_i, price_i) in flights:
            adj[from_i][to_i] = price_i
        # print(adj)
        min_dist = [math.inf] * n
        queue = deque()
        queue.append((src, 0))
        stops = 0
        while len(queue) != 0 and stops <= k:
            # print(queue, min_dist, stops)
            new_queue = deque()
            while len(queue) != 0:
                (node, dist) = queue.popleft()
                for (neighbour, price) in adj[node].items():
                    if dist+price <= min_dist[neighbour]:
                        new_queue.append((neighbour, dist+price))
                        min_dist[neighbour] = dist+price
                    # print("new_queue", new_queue)
            queue = new_queue
            stops += 1
            
        if min_dist[dst] != math.inf:
            return min_dist[dst]
            
        return -1
                
            