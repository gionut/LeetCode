class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        candidates = sorted(candidates)
        self.f(candidates, target, 0, [], solution)
        return solution
    
    def f(self, candidates, target, partialSum, partialSolution, solution):
        if partialSum==target:
            solution.append(partialSolution)
            return
        if len(candidates) == 0:
            return
        if candidates[0]+partialSum > target:
            return
        if candidates[0]+partialSum <= target:
            self.f(candidates, target, candidates[0]+partialSum, partialSolution + [candidates[0]], solution)
            self.f(candidates[1:], target, partialSum, partialSolution, solution)