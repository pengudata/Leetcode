class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        not_zero = set([x for x in nums if x != 0])
        return len(not_zero)