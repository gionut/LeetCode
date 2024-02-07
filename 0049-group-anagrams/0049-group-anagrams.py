class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            
            if sorted_s not in buckets:
                buckets[sorted_s] = []
            buckets[sorted_s].append(s)
        
        return buckets.values()