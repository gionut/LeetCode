# "loveleetcode"
# l-2
# o-2
# v-1
# e-4
# t-1
# c-1
# d-1
    

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        sorted_keys = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        result = []
        for key in sorted_keys:
            result.append(key * freq[key])
        return ''.join(result)