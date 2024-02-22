
#                 0
#     1         2          3
#             4          5   6
#          10
# -----
# 0
# 0,1 -- 1 + 2 =3
#     1,2
#         2,3
#     1,4
#         4,5

# 1
# 1,0 -- 1
# 1,2 --
# 1,4

# 0: 1
# 1: 0,2,4
# 2: 3,1
# 3: 2
# 4: 1,5
# 5: 4
    

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        def depth(node, visited, max_path):
            
            distance = 0
            top1_distance, top2_distance = 0, 0
            visited[node] = True
            for n in tree[node]:
                if n not in visited:
                    distance = 1 + depth(n, visited, max_path)
                if distance > top1_distance:
                    top1_distance, top2_distance = distance, top1_distance
                elif distance > top2_distance:
                    top2_distance = distance
            
            crt_max_path = top1_distance + top2_distance
            if crt_max_path > max_path[0]:
                max_path.pop()
                max_path.append(crt_max_path)
                
            return top1_distance
                
        tree = {}
        for (node1, node2) in edges:
            if node1 not in tree:
                tree[node1] = []
            if node2 not in tree:
                tree[node2] = []
            
            tree[node1].append(node2)
            tree[node2].append(node1)
            
        if len(edges) == 0:
            return 0
        
        max_path = [0]
        visited = {}
        depth(0, visited, max_path)
        return max_path[0]
                