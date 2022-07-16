class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        return self.f(digits)
    
    def f(self, digits):
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.letters[digits[0]]
        nextLetters = self.f(digits[1:])
        letters = self.letters[digits[0]]
        return [l + nextL for l in letters for nextL in nextLetters]