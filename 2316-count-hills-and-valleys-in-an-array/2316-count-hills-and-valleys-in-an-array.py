class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        filtered = [nums[0]]
        answer = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                filtered.append(nums[i])
        for i in range(1, len(filtered)-1):
            if filtered[i-1] < filtered[i] > filtered[i+1]:
                answer += 1
            elif filtered[i-1] > filtered[i] < filtered[i+1]:
                answer += 1
        return answer