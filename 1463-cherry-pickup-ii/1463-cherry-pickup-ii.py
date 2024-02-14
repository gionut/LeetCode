# i=0  r0 + R0 + MAX[(r0l,R0l), (r0l,R0d), (r0l,R0r), (r0d,R0l), (r0d,R0d), (r0d,R0r), (r0r,R0l), (r0r,R0d), (r0r,R0r)]
# i=1  r1 + R1 + MAX[(r0l,R0l), (r0l,R0d), (r0l,R0r), (r0d,R0l), (r0d,R0d), (r0d,R0r), (r0r,R0l), (r0r,R0d), (r0r,R0r)]
# ...
# i=n = rn+Rn

# crt_value = 0
# if robo1.pos == robo2.pos:
#     crt_value = robo1.pos.cherry
# else:
#     crt_val = robo1.pos.cherry + robo2.pos.cherry
    
# if i == rows:
#     return crt_val

# results = []
# for i in robo1.possible_moves():
#     for j in robo2.possible_moves():
#         if not memo[i, j]:
#             memo[i, j] = dp(i, j)
#         results.add(memo[i,j])
            
# return crt_val + max(results)

class Solution:
    def possible_moves(self, pos):
        # (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1)
        i = pos[0]
        j = pos[1]
        
        if i == len(self.grid) - 1:
            return []
        if j == 0:
            return [(i+1, j), (i+1, j+1)]
        if j == len(self.grid[i]) - 1:
            return [(i+1, j-1), (i+1, j)]
        return [(i+1, j-1), (i+1, j), (i+1, j+1)]
        
        
    
    def dp(self, robo1_pos, robo2_pos):
        crt_value = 0
        if robo1_pos == robo2_pos:
            crt_value = self.grid[robo1_pos[0]][robo1_pos[1]]
        else:
            crt_value = self.grid[robo1_pos[0]][robo1_pos[1]] +\
            self.grid[robo2_pos[0]][robo2_pos[1]]

        if robo1_pos[0] == len(self.grid) -1:
            return crt_value

        results = []
        
        for i in self.possible_moves(robo1_pos):
            for j in self.possible_moves(robo2_pos):
                if not (i, j) in self.memo:
                    self.memo[(i, j)] = self.dp(i, j)
                results.append(self.memo[(i,j)])
            
        return crt_value + max(results)
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.memo = {}
        return self.dp((0, 0), (0, len(grid[-1])-1))