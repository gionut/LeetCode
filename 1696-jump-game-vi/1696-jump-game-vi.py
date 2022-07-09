class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        last_index = len(nums) - 1
        
        next_k_monoqueue = deque()
        next_k_monoqueue.appendleft(last_index)
        
        for i in range(last_index - 1, -1, -1):
            max_reachable_score = nums[next_k_monoqueue[0]]
            
            current_score = nums[i] + max_reachable_score
            
            while next_k_monoqueue and current_score > nums[next_k_monoqueue[-1]]:
                next_k_monoqueue.pop()
            next_k_monoqueue.append(i)
            
            if next_k_monoqueue[0] >= i+k:
                next_k_monoqueue.popleft()
                
            nums[i] = current_score
        
        return nums[0]