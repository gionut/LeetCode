class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)
        
        for (x, y, time) in meetings:
            adj[x].append((y, time))
            adj[y].append((x, time))
            
        # add Person 0 and firstPerson
        adj[0].append((firstPerson, 0))
        adj[firstPerson].append((0, 0))
        
        earliest = [math.inf for i in range(n)]
        earliest[0] = 0
        
        queue = deque()
        queue.append((0,0))
        
        while queue:
            (node, time) = queue.popleft()
            # print(node, time, adj[node])
            for (neighbour, t) in adj[node]:
                if t >= time and t < earliest[neighbour]:
                    earliest[neighbour] = t
                    queue.append((neighbour, t))
                    # print("add", neighbour, t, earliest)
        
        
        return [i for i in range(n) if earliest[i] < math.inf]
                