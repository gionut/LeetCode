# 0,1,2,3,4,5,6,7,8,9,10
# 1,4,1,5,7,3,6,1,9,9,3
# max(
#     max(i)*1 + dp[i-1],
#     max(i, i-1)*2 + dp[i-2], 
#     max(i, i-1, i-2)*3 + dp[i-3],
#     max(i ... i-k+1)*k + dp[i-k]
#

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        interim_sums = [arr[0]]
        for i in range(1, len(arr)):
            max_sum = 0;
            left_bound = i-k+1
            if left_bound < 0:
                left_bound = 0

            while left_bound <= i:
                precalculated_sum = 0
                if left_bound-1 >= 0:
                    precalculated_sum = interim_sums[left_bound-1]
                
                partial_sum = max(arr[left_bound:i+1])*(i-left_bound+1) + precalculated_sum
                
                if partial_sum > max_sum:
                    max_sum = partial_sum
                
                left_bound +=1
                
            interim_sums.append(max_sum)
            # inbound_max = arr[i]
            # max_sum = 0
            # steps_back = 1
            # while steps_back < k and i-steps_back >= 0:
            #     print(i, steps_back, interim_sums)
            #     if arr[i-steps_back+1] > inbound_max:
            #         inbound_max = arr[i-steps_back]
            #     partial_sum = inbound_max*(steps_back) + interim_sums[i-steps_back]
            #     if partial_sum > max_sum:
            #         max_sum = partial_sum
            #     steps_back +=1
            # interim_sums.append(max_sum)
        
        return interim_sums[-1]