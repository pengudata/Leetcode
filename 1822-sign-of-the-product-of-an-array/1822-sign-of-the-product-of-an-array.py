class Solution:
    def arraySign(self, nums: List[int]) -> int:
        multiple = nums[0]
        for i in range(1, len(nums)):
            multiple *= nums[i]
        if multiple == 0:
            return 0
        elif multiple < 0:
            return -1
        else:
            return 1
