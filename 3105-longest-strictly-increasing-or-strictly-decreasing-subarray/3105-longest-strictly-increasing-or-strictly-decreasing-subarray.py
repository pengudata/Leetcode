class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        answer = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i-1] > nums[i]:
                dec += 1
                inc = 1
            else :
                dec = 1
                inc = 1
            answer = max(inc, dec, answer)
        return answer