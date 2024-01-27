class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        table = {}
        for index in range(len(keyboard)):
            table[keyboard[index]] = index
        
        time = 0
        crt_key = keyboard[0] 
        for next_key in word:
            time = time + abs(table[crt_key] - table[next_key])
            crt_key = next_key
        return time
        