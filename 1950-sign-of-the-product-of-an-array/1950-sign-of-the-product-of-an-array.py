class Solution:
    def arraySign(self, nums: List[int]) -> int:
        multiple = 1
        for i in range(len(nums)):
            multiple *= nums[i]
        if multiple == 0:
            return 0
        elif multiple < 0:
            return -1
        else:
            return 1
