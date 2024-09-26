class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = []
        answer = 0
        for i in range(numOnes):
            nums.append(1)
        for i in range(numZeros):
            nums.append(0)
        for i in range(numNegOnes):
            nums.append(-1)
        for i in range(k):
            answer += nums[i]
        return answer